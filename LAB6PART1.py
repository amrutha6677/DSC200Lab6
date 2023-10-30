import pandas as pd

# Datasets into DataFrames
df1 = pd.read_csv('dataset1.csv')
df2 = pd.read_csv('dataset2.csv', low_memory=False)
df3 = pd.read_csv('dataset3.csv')

# Reset the index for each DataFrame
df1 = df1.reset_index(drop=True)
df2 = df2.reset_index(drop=True)
df3 = df3.reset_index(drop=True)

# Rename columns for each dataset
mapping_df1 = {
    'Case Number': 'Case Number',
    'ID': 'ID',
    'Date': 'Date',
    'Primary Type': 'Offense',
    'Block': 'Address',
    'Latitude': 'Latitude',
    'Longitude': 'Longitude',
}

mapping_df2 = {
    'INCIDENT_NO': 'Case Number',
    'INSTANCEID': 'ID',
    'DATE_FROM': 'Date',
    'OFFENSE': 'Offense',
    'LOCATION': 'Address',
    'LATITUDE_X': 'Latitude',
    'LONGITUDE_X': 'Longitude',
}

mapping_df3 = {
    'Case_Number': 'Case Number',
    'Case_NumberAlt': 'ID',
    'Occurred_Date': 'Date',
    'Offense_Category': 'Offense',
    'Address': 'Address',
    'Latitude': 'Latitude',
    'Longitude': 'Longitude',
    'Offense': 'Offense1'
}

df1.rename(columns=mapping_df1, inplace=True)
df2.rename(columns=mapping_df2, inplace=True)
df3.rename(columns=mapping_df3, inplace=True)

# Wanted columns in each DataFrame
wanted_columns = ["Case Number", "ID", "Date", "Offense", "Address", "Latitude", "Longitude"]

# Empty DataFrame with the wanted columns
# merged_df = pd.DataFrame(columns=wanted_columns)
df2.to_csv('df2.csv')
df1 = df1[wanted_columns]
df2 = df2[wanted_columns]
df3 = df3[wanted_columns]
df2.to_csv('df2.csv')
df3.to_csv('df3.csv')
# Concatenate the DataFrames
merged_df = pd.concat([df1, df2, df3], ignore_index=True)

# merged_df = pd.concat([merged_df1, df3], ignore_index=True)

# Reset the index for the merged DataFrame
merged_df.reset_index(drop=True, inplace=True)

# Merged dataset
merged_df.to_csv('merged_dataset.csv', index=False)


