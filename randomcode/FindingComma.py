import pandas as pd

# Read the XLSX file
df = pd.read_excel('/Users/shailendra0408/Desktop/leads-data-sample-1.xlsx')

# Count the number of commas in each cell in the column
df['commas'] = df['keypress'].str.count(',')

# Print the total number of commas in the column
print(df['commas'].sum())