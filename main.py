import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

df = pd.read_csv('jobss.csv')

# overview i te dhenave
print(df.head())

print("\n------------------------------------------------------------------------------------------------------------\n")

# Tipet e te dhenave
print(df.dtypes)

print("\n------------------------------------------------------------------------------------------------------------\n")

# Numri i te dhenave te plota
print(df.info())

print("\n------------------------------------------------------------------------------------------------------------\n")

# Numri i te dhenave null
print(df.isnull().sum())

print("\n------------------------------------------------------------------------------------------------------------\n")

# Trajtimi i te dhenave te zbrazeta
df = df.rename(columns={'sal': 'Salary'})

df = df.replace('vide', '')
df = df.drop(['Unnamed: 1', 'Longitude', 'Latitude'], axis=1)
df['Key Skills'] = df['Key Skills'].apply(lambda x: '/'.join(set(x.split('|'))))

avg_length_of_role = df['Role'].str.len().mean()
mask_for_role = df['Role'].str.len() > avg_length_of_role * 2
df = df[~mask_for_role]

avg_length_of_role_category = df['Role Category'].str.len().mean()
mask_for_role_category = df['Role Category'].str.len() > avg_length_of_role_category * 2
df = df[~mask_for_role_category]

df = df.dropna(subset=['Industry', 'Role'])
print(df.isnull().sum())

df.to_csv('cleaned_jobss_dataset.csv', index=False)

# print(df['Industry'].value_counts())

df_subset_recrutment_staffing = df[df['Industry'] == 'Recruitment, Staffing']

print("\n------------------------------------------------------------------------------------\n")

def discretize_age_ranges(age_range):
    min_age, max_age = age_range.split('-')
    min_age = ''.join(filter(str.isdigit, min_age))
    max_age = ''.join(filter(str.isdigit, max_age))
    mid_point = (int(min_age) + int(max_age)) // 2
    return int(round(mid_point))

df_subset_recrutment_staffing['Experience'] = df_subset_recrutment_staffing['Job Experience Required'].apply(discretize_age_ranges)
df_subset_recrutment_staffing = df_subset_recrutment_staffing.sort_values('Experience')
df_subset_recrutment_staffing = df_subset_recrutment_staffing[df_subset_recrutment_staffing['Experience'] < 10]

plt.scatter(df_subset_recrutment_staffing['Experience'], df_subset_recrutment_staffing['Salary'])
plt.show()