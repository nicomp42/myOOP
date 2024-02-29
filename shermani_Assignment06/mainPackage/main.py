#main.py
# main.py
# Name: Nosagie Sherman
# email: shermani@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 2/22/2024
# Course/Section:  IS 4030 - 002
# Semester/Year: Spring 2024
# Brief Description of the assignment: This is the required documentation for Assignment 05. Where you use a function provide by you to import a csv file's data into a list. Then you find the max value with and without using list Comprehnsion. Then you print the first 5 items.
# Citations:
# Anything else that's relevant: The reason my code did not work was a typo in my function package

from functionPackage.function import *


if __name__ == "__main__":
    import_data = read_CSV_file("Iowa_Lottery_Weekly_Sales_by_Game_Type.csv")
    
    #max without list comp
    max_SalesAmount= 0
    for row in import_data:
        num_string = row[2]
        if num_string == "":
            num = 0
        else:
            num = float(num_string)
            if num>max_SalesAmount:
                max_SalesAmount=num
    print("The maximum sales value is ", max_SalesAmount)
    
    # with List Comprehension
    max_SalesAmount= max(float(row[2]) for row in import_data if row[2] != "")
    print("The max value is:",max_SalesAmount)
    
    data_set = {row[1] for row in import_data}
    setlen = len(data_set)
    print("The length of the data set is ", setlen)
    data_list = list(data_set)[:5]
    print("The first five values of the set is ",data_list)
            