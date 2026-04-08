# finding max number via *args in function

def find_max(*num):
    max=num[0]
    for i in range(len(num)):
        if num[i]>max:
            max=num[i]
    print(max)
"""
def find_max(*num):
    max=num[0]
    for i in num:
        if(i>max):
            max=i
    print(max)   
"""
find_max(78,43,23,12,45,98,987) 