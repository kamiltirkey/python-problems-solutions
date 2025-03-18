
# Importing the required libraries
import openpyxl
import pandas as pd


# Reading the data from the Excel file
employee_data = pd.read_excel('employee_data.xlsx')


print(employee_data)

# Calculating the bonus for each employee
employee_data['Bonus'] = employee_data['Salary'] * 0.1

# Saving the updated data to a new Excel file
employee_data.to_excel('employee_data_with_bonus.xlsx', index=False)


print(employee_data)