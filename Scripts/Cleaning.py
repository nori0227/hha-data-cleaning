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

