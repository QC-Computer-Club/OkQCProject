import xlrd
from collections import Counter # Creates Dictionary with object counts

# Initialize Spreadsheet data
book = xlrd.open_workbook('Prof Progs Schedule Fall2016.xlsx')
sheet = book.sheet_by_index(0)

# Assign Column Titles to a List
col_list = sheet.row_values(rowx = 0, start_colx = 0, end_colx = 14)
col_list = list(map(lambda x : x.lower(), col_list))

# Read in User Input
search_term1 = input("Search Term 1: ").lower()
search_term2 = input("Search Term 2: ").lower()

# Discern index value based on subject of search
try:
    col_index = col_list.index(search_term1)
except ValueError:
    print("Col Not Found")
    

# Creates a List of Data to be searched based on the first seach term
col_data = sheet.col_values(colx = col_index, start_rowx = 1, end_rowx = 217)
col_data = list(map(lambda x : x.lower(), col_data))

for i, found in enumerate(col_data) :
    if found == search_term2 :
        print(sheet.row_values(rowx = i + 1, start_colx = 0, end_colx = 14))



