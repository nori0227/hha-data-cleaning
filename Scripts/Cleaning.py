import pandas as pd
import datetime as dt
import uuid 
import numpy as np

""" step 1. load data into python """
df= pd.read_csv('data/dataset/School_Learning_Modalities.csv')
df #print csv

""" Step 2. Print count of the number of columns and rows """ 
countColumns, countRows = df.shape #### get a count of the number of columns and rows
df.shape

""" Step 3. Print column names """
column_names = list(df)

""" Step 4. clean the column names """ 
list(df) ### list columns
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_') ## regex #### remove all special characters and whitespace ' ' from column names
list(df)
df.columns = df.columns.str.replace(' ', '_') ## regex ### replace all whitespace in column names with an underscore
list(df)

"""Step 5. clean strings that might exist within each column"""

strings_columns = df.select_dtypes(object).columns # Assign all string data type to variable strings_columns
df[strings_columns] = df[strings_columns].apply(lambda x: x.str.replace(' ', '_')) # replace all whitespace in strings with an underscore
df[strings_columns] = df[strings_columns].apply(lambda x: x.str.replace('[^A-Za-z0-9]+', '_')) ## regex #### remove all special characters and whitespace ' ' from column names
list(df[strings_columns])

"""" Step 6. Assess white space or special characters """
if not ("!".isalpha() or "!".isdigit() or "!".isspace()):
        print("It is a special character")
    
""" Step 7. Convert column type to correct type """
df = df.astype("int64", errors='ignore')
df.head()
df.info()

"""" Step 8. Look for duplicate rows and remove duplicate rows """"
df.drop_duplicates() # Remove duplicates

""" Step 9. Assess missingness (count of missing values per column)"""
# replacing blank, empty cells with NaN
df.replace(to_replace='', value=np.nan, inplace=True)
df.replace(to_replace=' ', value=np.nan, inplace=True)
df.isnull().sum() # get a count of missing values in each column

""" Step 10. New data field """
df['modality_inperson'] = (df['Learning_Modality'].apply(lambda x: 'true' if x == 'in_person' else 'false')) 
df.to_csv('data/dataset/School_Learning_Modalities.csv')



















