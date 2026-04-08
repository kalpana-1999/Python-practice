# Function for square       -----------------------This is single line comment
def square(num):
    sqr=num*num
    print(sqr)
square(6)
square(11)



"""
Function 
for         ----------------------------This is multiline comment
Leap year
"""
def leap(year):
    if (year%4==0):
        if(year%100!=0 or year%400==0):
            print("Given year is a leap year:",year)
    else:
        print("Given year is NOT a leap year:",year)

leap(2035)
leap(2044)