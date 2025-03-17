CONVERTING EXCEL TO JSON

#import the pandas library

import pandas as pd

# Read the excel file
df = pd.read_excel('europe.xlsx')


# Convert the dataframe to json
df.to_json('europe.json', orient='records')


