'''
CAPP30122 W'22: Building decision trees

Cole von Glahn & Evelyn Siu
'''

import math
import sys
import pandas as pd


def go(training_filename, testing_filename):
    '''
    Construct a decision tree using the training data and then apply
    it to the testing data.

    Inputs:
      training_filename (string): the name of the file with the
        training data
      testing_filename (string): the name of the file with the testing
        data

    Returns (list of strings or pandas series of strings): result of
      applying the decision tree to the testing data.
    '''

    classified_rows = []
    table = pd.read_csv(training_filename)
    test_data = pd.read_csv(testing_filename)
    root_node = DecisionNodes(table)

    model = trainer(root_node)
    for _, row in test_data.iterrows():
        classified_rows += tester(model, row)

    return classified_rows


def trainer(node):
    '''
    Trains a decision tree model for classifying followup testing data.

    args:
        node (DecisionNode): Structure containing data and key elements of
                            decisionmaking process.
    output:
        node (DecisionNode): A decision tree composed of node objects with
                            classifier information.
    '''
    # Base Case
    if node.leaf or len(node.data.columns) < 2:
        return node

    # Find and apply split value to create child nodes
    split_to = get_greedy(node)
    node.add_split(split_to)
    node.build_children()
    for child in node.children:
        trainer(child)

    return node


def tester(node, row):
    '''
    Apply the training model to the testing data for classification.

    args:
        node (DecisionNode): A decision tree composed of node objects with
                            classifier information.
        row (pandas Series): One row of the test data to be classified.

    output:
        all_rows (list): The classifications of each row in indexed order
    '''

    classifications = []
    # Base case
    if node.leaf:
        return [str(node.label)]

    split_val = node.split_column
    for i, child in enumerate(node.children):
        # Send the row into the appropriately categorized child node
        if row[split_val] == child.edge:
            classifications += tester(child, row)
            break
        # If the row's split category does not exist categorize per this node.
        if row[split_val] != child.edge and i == len(node.children) - 1:
            return [str(node.label)]

    return classifications


class DecisionNodes:
    '''
    Class for representing the nodes of a data classification Decision Tree.

    Arguments and attributes in __init__ docstring below
    '''


    def __init__(self, data, edge=None):
        '''
        args:
            data (pandas DF): The data being trained with or tested on.
            edge (None or str): The category for data sorted into this node

        attributes:
            self.data (pandas DF): The data being trained with or tested on.
            self.target (pandas series): The classification value of interest
                                        must be binary.
            self.size (int): The size of the data.
            self.label (string): The most prevalent target value in the data.
                                Break ties with lower value string.
            self.children (list): The nodes created by the column split.
            self.split_column (string): Name of the column with the highest
                                        gain ratio.
            self.leaf (bool): Whether or not this is a leaf node.
            self.edge (None or str): The category for data sorted into this node

        '''
        self.data = data
        self.target = self.data.iloc[:,-1]
        self.size = len(data)
        self.label = self.get_target()
        self.split_column = ''
        self.children = []
        self.leaf = self.check_leaf()
        self.edge = edge


    def add_split(self, attr):
        '''
        Adds a split column after it has been determined by gain calculations.

        args:
            attr (string): The name of the attribute heading the split column

        returns:
            None
        '''
        self.split_column = attr


    def get_target(self):
        '''
        Determines the most prevalent value in the target column. Sets the
        node's label to that value. Breaks ties on lower string value.
        '''
        split_dict = {}
        # Counts all values in target column
        for c in self.data[self.target.name]:
            split_dict[c] = split_dict.get(c, 0) + 1

        # Selects key based on largest count of values and breaks ties.
        most = max(split_dict, key=split_dict.get)
        for cat in split_dict:
            if split_dict[cat] == split_dict[most]:
                most = min(cat, most)

        return most


    def check_leaf(self):
        '''
        Determines whether or not this is a leaf node of the tree based on two
        conditions:
            Is there only one value in the target column?
            Are all of the remaining row attributes identical?

        outputs:
            bool of leaf node status.
        '''
        # Subset dataset without target column
        attr_only = self.data.iloc[:,0:-1]

        # Are all target values the same?
        if len(self.target.unique()) == 1:
            return True

        # Are all rows the same?
        for i in range(self.size):
            if (attr_only.iloc[0] == attr_only.iloc[i]).all():
                is_leaf = True
            else:
                is_leaf = False
                break

        if is_leaf:
            return True

        return False


    def build_children(self):
        '''
        Constructs the children of the current node based on
        split column determination.

        outputs:
            None
        '''
        for cat in self.data[self.split_column].unique():
            # Subset current data on split column for new node
            child_set = self.data.loc[self.data[self.split_column] == cat]
            child = DecisionNodes(child_set, cat)
            # Remove split column from child
            child.data = child.data.drop(self.split_column, axis=1)
            self.children.append(child)


def get_greedy(parent):
    '''
    Calculates the gini indices for the gain value and normalizes with
    split info to find gain ratio. Selects attribute with largest gain ratio
    as split column.
    '''
    gain_dict = {}
    parent_gini = gini(parent.data[parent.target.name])

    # Set up componenents for calculation of a single attribute
    for attr in parent.data.columns[:-1]:
        child_gini = 0
        split_info = 0
        plan = parent.data[attr]

        # Calculate components of gain ratio formula
        for attribute in plan.unique():
            subset = parent.data.loc[parent.data[attr] == attribute, parent.target.name]
            sub_rat = (subset.count() / parent.size)
            child_gini += gini(subset) * sub_rat
            split_info += sub_rat * math.log(sub_rat, 2)

        # Prevent division by zero
        if split_info == 0:
            continue

        # Finalize and record gain values for comparison
        gain_split = (parent_gini - child_gini) / (-split_info)
        gain_dict[attr] = gain_split

    # Selects key based on largest gain ratio and breaks ties.
    new_node = max(gain_dict, key=gain_dict.get)
    for challenger in gain_dict:
        if gain_dict[challenger] == gain_dict[new_node]:
            new_node = min(challenger, new_node)

    return new_node


def gini(data):
    '''
    Calculates the gini index for a dataset.

    args:
        data (pandas DF): The dataset to compute.

    outputs:
        (float) the gini score
    '''
    class_dict = {}
    denom = 0

    # Record counts by category
    for c in data:
        class_dict[c] = class_dict.get(c, 0) + 1
        # iterate denominator for ratio
        denom +=1

    all_pc = 0

    # Take child count/parent size and add to overall value
    for cat in class_dict:
        pc = (class_dict[cat] / denom)**2
        all_pc += pc

    return 1 - all_pc


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python3 {} <training filename> <testing filename>".format(
            sys.argv[0]))
        sys.exit(1)

    for result in go(sys.argv[1], sys.argv[2]):
        print(result)