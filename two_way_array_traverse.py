arr=[10,34,45,56,23,33]
def reverse_array(arr):
    l=0
    r=len(arr)-1
    
    while l<=r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    
    print(arr)
       
reverse_array(arr)