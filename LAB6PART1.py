import pandas as pd

def function1():
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

def function2():
    # Read CSV
    df = pd.read_csv("Data/Lab6Data.csv")

    # print original number of features and observations
    print(
        f"Number of observations in the original CSV file: {df.shape[0]}\nNumber of features in the original CSV file: {df.shape[1]}")

    # Begin checking values in columns ---------------------------------------------

    # all whole numbers, no missing values
    # print(df.iloc[:, [0]].value_counts(dropna=False))

    # Check if workclass and workclass_1 are equal
    # All values equal the documentation expectation
    # print(df.iloc[:, [1]].value_counts(dropna=False))
    # print(df.iloc[:, [10]].value_counts(dropna=False))
    # print(df.query('workclass != workclass_1'))
    # Each columns' values equal each other so column workclass will be chosen
    df = df.drop(columns='workclass_1')
    # Drop rows that do not contain an expected value from documentation
    df = df.drop(df[df['workclass'] == ' ?'].index)
    # print(df.iloc[:, [1]].value_counts(dropna=False))

    # all whole numbers, no missing values
    # print(df.iloc[:, [2]].value_counts(dropna=False))

    # Check if education and education_1 are equal
    # print(df.iloc[:, [3]].value_counts(dropna=False))
    # print(df.iloc[:, [8]].value_counts(dropna=False))
    # print(df.query('education != education_1')[['education', 'education_1']])
    # Each columns' values equal each other so column education_1 will be chosen
    # because it matches the expected value from the documentation
    df = df.drop(columns='education')
    # Move education_1 column to correct location according to expected spot in documentation
    df.insert(3, 'education_1', df.pop('education_1'))

    # all whole numbers, no missing values
    # print(df.iloc[:, [4]].value_counts(dropna=False))
    # Drop NA rows
    df = df.dropna(subset=['educ_num'])
    # print(df.iloc[:, [4]].value_counts(dropna=False))

    # all values match expected values in documentation
    # print(df.iloc[:, [5]].value_counts(dropna=False))

    # Check if occupation and occupation_1 are equal
    # print(df.iloc[:, [6]].value_counts(dropna=False))
    # print(df.iloc[:, [8]].value_counts(dropna=False))
    # print(df.query('occupation != occupation_1')[['occupation', 'occupation_1']])
    # Each columns' values equal each other so column education_1 will be chosen
    # because it matches the expected value from the documentation
    df = df.drop(columns='occupation_1')
    # Drop rows that do not contain an expected value from documentation
    df = df.drop(df[df['occupation'] == ' ?'].index)
    # print(df.iloc[:, [6]].value_counts(dropna=False))

    # all values match expected values in documentation
    # print(df.iloc[:, [7]].value_counts(dropna=False))

    # all values match expected values in documentation
    # print(df.iloc[:, [8]].value_counts(dropna=False))

    # all values match expected values in documentation
    # print(df.iloc[:, [9]].value_counts(dropna=False))

    # There are not any missing values
    # print(df.iloc[:, [10]].value_counts(dropna=False))

    # There are not any missing values
    # print(df.iloc[:, [11]].value_counts(dropna=False))

    # There are not any missing values
    # print(df.iloc[:, [12]].value_counts(dropna=False))

    # print(df.iloc[:, [13]].value_counts(dropna=False))
    # Drop rows that do not contain an expected value from documentation
    df = df.drop(df[df['native-country'] == ' ?'].index)
    # print(df.iloc[:, [13]].value_counts(dropna=False))

    # There are not any missing values
    # print(df.iloc[:, [14]].value_counts(dropna=False))

    # Drop duplicate rows
    df = df.drop_duplicates(keep='last')

    #print(df.columns.values)
    # Make clean header column
    df.columns = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation",
              "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "salary"]
    #print(df.columns.values)

    # print final number of features and observations
    print(
        f"Number of observations in the final CSV file: {df.shape[0]}\nNumber of features in the final CSV file: {df.shape[1]}")

    # create the new CSV file
    df.to_csv("Data/censusIncomeData.csv")


answer = int(input(
    "Please enter the number of the function you would like to do.\nFunction 1: Combining the datasets together\nFunction 2: Clean the dataset\n"))
if answer == 1:
    function1()
elif answer == 2:
    function2()
else:
    print("You did not enter 1 or 2")
