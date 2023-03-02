import pandas as pd
import sys
import re


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
    data.to_csv('output.csv', index=False)
    # Read the CSV file and extract the column names and content
    df = pd.read_csv('output.csv')
    columns = df.columns.tolist()
    content = df.values.tolist()

    # Loop through the column names and content and convert them to valid XML tags
    xml_rows = []
    for row in content:
        xml_row = []
        for i, value in enumerate(row):
            # Remove any non-alphanumeric characters and replace spaces with underscores
            xml_column = re.sub('[^0-9a-zA-Z]+', '', columns[i]).replace(' ', '_')
            # Add opening and closing XML tags to the column name and content
            xml_column = '<{0}>{1}</{0}>'.format(xml_column, value)
            xml_row.append(xml_column)
            xml_rows.append(''.join(xml_row))

    # Write the XML tags and content to a new file
    with open('output.xml', 'w') as f:
        f.write('<root>\n')
        for xml_row in xml_rows:
            f.write(xml_row + '\n')
        f.write('</root>')
    

print('Output file saved successfully!')
