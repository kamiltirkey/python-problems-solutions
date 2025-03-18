
# Importing the required libraries
import pandas as pd

# Reading the data from the Excel file
input_data = pd.read_excel('Input.xlsx')

print(input_data)

# Calculating the total for each row
input_data['Total'] = input_data['Price'] * input_data['Quantity']

# Saving the updated data to a new Excel file
input_data.to_excel('Output.xlsx', index=False)


print(input_data)
