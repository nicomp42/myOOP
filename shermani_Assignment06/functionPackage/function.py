# functions.py

import csv
def read_CSV_file(file_name):
    '''
    Read from a CSV file into a list
    @param
    file_name The CSV file to read. It should have a header row, which will be skipped
    @return
    the list containing all the rows except the header row
    '''
    csv_data = []
    with open(file_name, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
    #   csv_data.append(header) # We don't want the header row.
        for row in reader:
            csv_data.append(row)
    #print(csv_data)
    print (type(csv_data)) # It's a list of lists!
    return csv_data