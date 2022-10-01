# hha-data-cleaning
HHA-507 Assignment#2

#.py script is in the Scripts folder

# Downloaded published dataset from healthdata.gov called “School Learning Modalities” - https://healthdata.gov/National/School-Learning-Modalities/aitj-yx37

#Place thte .csv file in the sub-folder dataset

#Create a Cleaning.py script 

#imported import pandas as pd
import datetime as dt
import uuid 
import numpy as np

#loaded the dataset into python through relative path of the .csv file

#printed the count of columns and rows 

#provided a print out of column names

#cleaned the column name by removing all special characters, white spaces and replacing all white spaces with an underscore

#cleaned strings that might existed within the columns by assigning all string data to variable strings_column and removing all special characters, white spaces and eplacing all white spaces with an underscore

#assessed white space or special characters by checking if it is not a letter, a number or a whitespace

#converted the column type to the correct type

#removed duplicate rows

#assessed missingness

#created a new column called modality_inperson that contained a binary value of true and false. The function took over the old column "Learning_Modality" and recoded the value for a specific row to true, if the learning modality value is ‘in-person’, and recodes it to false if the values either ‘remote’ or ‘hybrid’ 
