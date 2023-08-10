'''Getting Started with Pandas'''
import pandas as pd

# print(pd.__version__)

# mydataset = {
#     'cars': ["BMW", "Volvo", "Ford"],
#     'passings': [3, 7, 2]
# }

# myvar = pd.DataFrame(mydataset)

# print(myvar)

# For installing python libraries
# python -m pip install <command>


'''Pandas Series'''
# a = [1, 7, 2]

# myvar = pd.Series(a)

# #print(myvar)

# #returning the first value of the series:
# print(myvar[0])


'''LABELS'''
# Creating Labels

# a = [1, 7, 2]

# myvar = pd.Series(a, index = ["x", "y", "z"])

# #print(myvar)

# # Accessing an item in a label.
# print(myvar["y"])


'''KEY/VALUE OBJECTS AS SERIES'''
# Dictionaries can be used when creating a Series

# in line  47, we named our own indexes.
# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories)

# print(myvar)

# # You can also access a particular item in a dictionary using the index argument and specify the item in the series.
# myvar = pd.Series(calories, index = ["day1", "day2"])
# print(myvar)


'''DATA FRAMES'''
# ''' Series is like a column, a DataFrame is the whole table.'''

# data = {
#       "calories": [420, 380, 390],
#       "duration": [50, 40, 45]
# }

# myvar = pd.DataFrame(data)

# print(myvar)
 
'''LOCATE ROW'''
# loc attribute is used to return one or more specified row(s)
# refer to the code on line 64.
# df = pd.DataFrame(data)
# print(df.loc[0])

# OR

# Using a list of indexes:
#print(df.loc[[0, 1]])

# we'll name our own indexes again.
# df = pd.DataFrame(data, index=["day1", "day2", "day3"])

# print(df)

# we could also locate a named index.
# print(df.loc["day3"])

'''LOADING FILES INTO A DATAFRAME'''
# Only if you have created the csv file.
# df = pd.read_csv('data.csv')

# print(df)

'''PANDAS READ CSV'''
# Reading CSV files.
'''CSV stands for Comma-seperated Value Files.'''
# df = pd.read_csv('data.csv')

# this is used to print the entire DataFrame.
# print(df.to_string())

'''MAX_ROWS'''
# pd.options.display.max_rows = 9999

# df = pd.read_csv('data.csv')

# print(df)

'''READ JSON'''
'''JSON stands for JavaScript Object Notation.'''
# df = pd.read_json('data.csv')

# print(df.to_string())

'''ANALYZING DATAFRAMES'''
'''VIEWING THE DATA'''
# This views rows starting from the top.
# df = pd.read_csv('data.csv')

# # print(df.head())

# # This views rows starting from the bottom.
# # print(df.tail())

# # You could also get info about the Data you're viewing.
# print(df.info())

# Null Values is where we ended. remember to clear this comment.
