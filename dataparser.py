import pandas as pd
import sys


print(pd.__version__)

# Get command line arguments
file_name = sys.argv[1]
output_format = sys.argv[2]

# Read data from file
data = pd.read_csv(file_name, delimiter='\t')

data = data.rename(columns={'Home State': 'Home_State'})

# Convert to the desired format
if output_format == '-c':
    data.to_csv('output.csv', index=False)
elif output_format == '-j':
    data.to_json('output.json', orient='records')
elif output_format == '-x':
    data.to_xml('output.xml')

print('Output file saved successfully!')
