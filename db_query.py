import sys
import xlrd

def main():
# Initialize Spreadsheet data
    book = xlrd.open_workbook(xls_book())
    sheet = book.sheet_by_index(0)

# Assign Column Titles to a List
    col_list = sheet.row_values(rowx = 0, start_colx = 0, end_colx = 13)

# Read in User Input
    subject = input("Which class are you inquiring about?: ")
    predicate = input("What would you like to know?: ")

# List of all Classes 
    col_data = sheet.col_values(colx = 5, start_rowx = 1, end_rowx = 217)

# Attempt to find Class name in list
    try :
        col_data.index(subject)
    except ValueError:
        print("Class Not Found")
        sys.exit(0)

    try :
        c_index = col_list.index(predicate)
    except ValueError:
        print("Data Not Found")
        sys.exit(0)

# Print all data out based on user entry
    for r_index, result in enumerate(col_data) :
        if result == subject :
            print(sheet.row_values(rowx = r_index + 1, start_colx = c_index, end_colx = c_index + 1))

# For queue

def xls_book():
    """Define Excel Spreadsheet to read from here"""
    return('Prof Progs Schedule Fall2016.xlsx')

def who(classname):
# Initialize Spreadsheet data
    book = xlrd.open_workbook(xls_book())
    sheet = book.sheet_by_index(0)

# Assign Column Titles to a List
    col_list = sheet.row_values(rowx = 0, start_colx = 0, end_colx = 13)

# Read in User Input
#    subject = input("Which class are you inquiring about?: ")
#    predicate = input("What would you like to know?: ")
# Class Name stored as User/Voice Input
    subject = classname.title()
    predicate = "LAST"

# List of all Classes 
    col_data = sheet.col_values(colx = 5, start_rowx = 1, end_rowx = 217)

# Attempt to find Class name in list
    try :
        print(subject)
        col_data.index(subject)
    except ValueError:
        print("Class Not Found")
        sys.exit(0)

    try :
        c_index = col_list.index(predicate)
    except ValueError:
        print("Data Not Found")
        sys.exit(0)

# Print all data out based on user entry
    for r_index, result in enumerate(col_data) :
        if result == subject :
            print(sheet.row_values(rowx = r_index + 1, start_colx = c_index, end_colx = c_index + 1))

def what(classname):
# Initialize Spreadsheet data
    book = xlrd.open_workbook(xls_book())
    sheet = book.sheet_by_index(0)

# Assign Column Titles to a List
    col_list = sheet.row_values(rowx = 0, start_colx = 0, end_colx = 13)

# Read in User Input
#    subject = input("Which class are you inquiring about?: ")
#    predicate = input("What would you like to know?: ")
# Class Name stored as User/Voice Input
    subject = classname.title()
    predicate = "CODE"

# List of all Classes 
    col_data = sheet.col_values(colx = 5, start_rowx = 1, end_rowx = 217)

# Attempt to find Class name in list
    try :
        print(subject)
        col_data.index(subject)
    except ValueError:
        print("Class Not Found")
        sys.exit(0)

    try :
        c_index = col_list.index(predicate)
    except ValueError:
        print("Data Not Found")
        sys.exit(0)

# Print all data out based on user entry
    for r_index, result in enumerate(col_data) :
        if result == subject :
            print(sheet.row_values(rowx = r_index + 1, start_colx = c_index, end_colx = c_index + 1))

def search(classname, query):
# Initialize Spreadsheet data
    book = xlrd.open_workbook(xls_book())
    sheet = book.sheet_by_index(0)

# Assign Column Titles to a List
    col_list = sheet.row_values(rowx = 0, start_colx = 0, end_colx = 13)

# Read in User Input
#    subject = input("Which class are you inquiring about?: ")
#    predicate = input("What would you like to know?: ")
# Class Name stored as User/Voice Input
    subject = classname.title()
    predicate = query

# List of all Classes 
    col_data = sheet.col_values(colx = 5, start_rowx = 1, end_rowx = 217)

# Attempt to find Class name in list
    try :
        print(subject)
        col_data.index(subject)
    except ValueError:
        print("Class Not Found")
        sys.exit(0)

    try :
        c_index = col_list.index(predicate)
    except ValueError:
        print("Data Not Found")
        sys.exit(0)

# Print all data out based on user entry
    for r_index, result in enumerate(col_data) :
        if result == subject :
            print(sheet.row_values(rowx = r_index + 1, start_colx = c_index, end_colx = c_index + 1))


if __name__ == '__main__':
    main()
