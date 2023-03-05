import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.read_csv('2015_Street_Tree_Census_-_Tree_Data.csv')

# print(df)
# print(df.columns)

tree_census_subset = df[['tree_id','tree_dbh', 'stump_diam',
    'curb_loc', 'status', 'health', 'spc_latin', 'steward',
    'sidewalk', 'root_stone','root_grate', 'root_other', 'trunk_wire',
    'trnk_light', 'trnk_other','brch_light', 'brch_shoe', 'brch_other']]

# print(tree_census_subset)
# print(tree_census_subset.isna().sum())
# print(tree_census_subset[tree_census_subset['health'].isna()])

# print(tree_census_subset.describe())
# print(tree_census_subset.dtypes)

# print(tree_census_subset.hist(bins=60, figsize=(20,10)))
# print(tree_census_subset[tree_census_subset['tree_dbh'] > 50])

