def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year%4==0):
        if(year%100!=0 or year%400==0 ):
            leap=True
            print(" Given year is a leap year")
    return leap

year=int(input("Enter the year: "))
is_leap(year)