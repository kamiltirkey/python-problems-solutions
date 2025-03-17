
'''You have an Excel file named europe_data.xlsx containing data that you need to convert to a CSV file format for easier data manipulation and sharing. 
# The goal is to write a Python script that reads the Excel file and converts it to a CSV file named europe_data.csv.
'''

import pandas as pd

df = pd.read_excel('europe_data.xlsx')

df.to_csv('europe_data.csv', index=False)