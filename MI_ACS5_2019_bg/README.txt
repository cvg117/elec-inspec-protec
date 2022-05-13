American Community Survey (ACS) Select Variables for Michigan for the years 2015-2019 at the Block Group level (shapefile)

##Redistricting Data Hub (RDH) Retrieval Date
12/18/20

##Sources
ACS data retrieved using the Census API: https://api.census.gov/data/2019/acs/acs5
Boundary shapefile retrieved from the Census Cartographic Boundary File website: https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.2019.html

##Fields
    Field Name                                                                                                                    Description
0        GEOID                                                                                                              Unique identifier
1         NAME                                                                                        Full Geographic Name of the Block Group
2        STATE                                                                                                              Name of the State
3       COUNTY                                                                                                             Name of the County
4     TOTPOP19                                                                                         Total population estimate(B01003_001E)
5    TOTPOPMOE                                                                                 Total population margin of error (B01003_001M)
6     N_HISP19                                                                  Total Not Hispanic or Latino population estimate(B03003_002E)
7    N_HISPMOE                                                           Total Not Hispanic or Latino population margin of error(B03003_002M)
8     WHT_NH19                                                                     White alone, Not Hispanic or Latino estimate (B03002_003E)
9    WHT_NHMOE                                                              White alone, Not Hispanic or Latino margin of error (B03002_003M)
10    BLK_NH19                                                 Black or African American alone, Not Hispanic or Latino estimate (B03002_004E)
11   BLK_NHMOE                                           Black or African American alone, Not Hispanic or Latino margin of error(B03002_004M)
12      HISP19                                                                      Total Hispanic or Latino population estimate(B03003_003E)
13     HISPMOE                                                              Total Hispanic or Latino population margin of error (B03003_003M)
14     WHT_H19                                                                          White alone, Hispanic or Latino estimate(B03002_013E)
15    WHT_HMOE                                                                  White alone, Hispanic or Latino margin of error (B03002_013M)
16     BLK_H19                                                     Black or African American alone, Hispanic or Latino estimate (B03002_014E)
17    BLK_HMOE                                              Black or African American alone, Hispanic or Latino margin of error (B03002_014M)
18   BLK_ALL19                          Black or African American alone or in combination with one or more other races estimate (B02009_001E)
19  BLK_ALLMOE                   Black or African American alone or in combination with one or more other races margin of error (B02009_001M)
20   AIA_ALL19                  American Indian and Alaska Native alone or in combination with one or more other races estimate (B02010_001E)
21  AIA_ALLMOE           American Indian and Alaska Native alone or in combination with one or more other races margin of error (B02010_001M)
22   ASN_ALL19                                              Asian alone or in combination with one or more other races estimate (B02011_001E)
23  ASN_ALLMOE                                       Asian alone or in combination with one or more other races margin or error (B02011_001M)
24   NHP_ALL19         Native Hawaiian and Other Pacific Islander alone or in combination with one or more other races estimate (B02012_001E)
25  NHP_ALLMOE  Native Hawaiian and Other Pacific Islander alone or in combination with one or more other races margin of error (B02012_001M)
26   OTH_ALL19                                    Some Other Race alone or in combination with one or more other races estimate (B02013_001E)
27  OTH_ALLMOE                             Some Other Race alone or in combination with one or more other races margin of error (B02013_001M)
28     STATEFP                                                                                                                State FIPS Code
29    COUNTYFP                                                                                                               County FIPS Code
30     TRACTCE                                                                                                                     Tract Code

##Processing
ACS data for Michigan was retrieved with a python script from the Census. 
The data is available at the county level. The script extracted the data for all counties in Michigan. 
The selected variables were extracted from the ACS Census API. 
Each field represents either an estimate or margin of error for a particular variable. 
The fields were renamed to fit character length requirements. 
The shapefile was zipped into a folder with supporting geospatial files and this README. 
Processing was primarily completed using the pandas library.
The tabular data for Michigan was joined with geospatial data from Census TIGER files on the unique identifier field (GEOID) and extracted as a shapefile. 
Processing for the join used pandas and geopandas libraries.

##Additional Notes
For more information on variables available in the Census API and the particular table numbers see: https://api.census.gov/data/2019/acs/acs5/variables.html. 
These variables were selected because of their potential relevance to redistricting.
For more information on the geospatial data, please refer to the Census Cartographic Boundary link above. 
The ACS shapefile for Michigan is available in NAD83 projection.