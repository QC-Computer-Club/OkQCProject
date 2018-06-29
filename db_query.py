# Paul DeRubeis
# 5/4/2018
# Database Query Module
# modified by Simon Yip

import sys
import xlrd

# Initialize Spreadsheet data
database = 'Prof Progs Schedule Fall2016.xlsx'
book = xlrd.open_workbook(database)
sheet = book.sheet_by_index(0)

# Assign Column Titles to a List
col_list = sheet.row_values(rowx = 0,
                            start_colx = 0,
                            end_colx = 14)

# Method for Title Case Conversion
def convert(listToConvert):
    return [x.title() for x in listToConvert]

# Convert List to Title Case
col_list = convert(col_list)

"""for testing"""
print(col_list)

# Main for testing purposes
def main():

    # Read in User Input and set to Title case
    subject = input("Which class are you inquiring about?: ").title()
    predicate = input("What would you like to know?: ").title()

    # Created List of all Classes 
    col_data = sheet.col_values(colx = 5,
                                start_rowx = 1,
                                end_rowx = 217)

    # Convert List to Title Case
    col_data = convert(col_data)

    # Attempt to find Class name in list
    try :
        col_data.index(subject)
    except ValueError:
        print("Class Not Found")
        #sys.exit(0)

    # Attempt to find data associated with class
    try :
        c_index = col_list.index(predicate)
    except ValueError:
        print("Data Not Found")
        #sys.exit(0)

    # Print all data out based on user entry
    """(col_data must be enumerated so it can be looped through)"""
    for r_index, result in enumerate(col_data) :
        if result == subject :
            """Indicies are off by one because, in Python,
                ranges are non-inclusive on the high end,
                thus requiring a +1"""
            result_list = sheet.row_values(rowx = r_index + 1,
                                   start_colx = c_index,
                                   end_colx = c_index + 1)

            # Convert to Title Case
            result_list = convert(result_list)
            # Convert to a Set
            result_set = set(result_list)
            # Convert List to Tuple
            result_tuple = tuple(result_set)

            print(result_tuple)

def search(classname, query):
    # Class Name stored as User/Voice Input
    subject = classname.title()
    predicate = query.title()

    # List of all Classes 
    col_data = sheet.col_values(colx = 5,
                                start_rowx = 1,
                                end_rowx = 217)

    # Convert List to Title Case
    col_data = convert(col_data)

    # Attempt to find Class name in list
    try :
        print(subject)
        col_data.index(subject)
    except ValueError:
        print("Class Not Found")
        #sys.exit(0)

    try :
        c_index = col_list.index(predicate)
    except ValueError:
        print("Data Not Found")
        #sys.exit(0)

    # Print all data out based on user entry
    """(col_data must be enumerated so it can be looped through)"""
    for r_index, result in enumerate(col_data) :
        if result == subject :
            # Create Result List
            """Indicies are off by one because, in Python,
                ranges are non-inclusive on the high end,
                thus requiring a +1"""
            result_list = sheet.row_values(rowx = r_index + 1,
                                   start_colx = c_index,
                                   end_colx = c_index + 1)
    # Created List of all Classes 
    col_data = sheet.col_values(colx = 5,
                                start_rowx = 1,
                                end_rowx = 217)

    # Convert List to Title Case
    col_data = convert(col_data)

    # Attempt to find Class name in list
    try :
        col_data.index(subject)
    except ValueError:
        print("Class Not Found")
        #sys.exit(0)

    # Attempt to find data associated with class
    try :
        c_index = col_list.index(predicate)
    except ValueError:
        print("Data Not Found")
        #sys.exit(0)

    # Print all data out based on user entry
    """(col_data must be enumerated so it can be looped through)"""
    
    result_tuple_list = []
    
    for r_index, result in enumerate(col_data) :
        if result == subject :
            """Indicies are off by one because, in Python,
                ranges are non-inclusive on the high end,
                thus requiring a +1"""
            result_list = sheet.row_values(rowx = r_index + 1,
                                   start_colx = c_index,
                                   end_colx = c_index + 1)

            # Convert to Title Case
            result_list = convert(result_list)
            print("result_list:",result_list)
            # Convert to a Set
            result_set = set(result_list)
            print("result_set:",result_set)
            # Convert List to Tuple
            result_tuple = tuple(result_set)
            print("result_tuple:",result_tuple)
            
            result_tuple_list.append(result_tuple)
            
    for num_index, result in enumerate(result_tuple_list):
        print("result_tuple_list:", result)
    
    return result_tuple_list


if __name__ == '__main__':
    main()
