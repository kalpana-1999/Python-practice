arr=[23,34,12,67,87,10,10,12,23]
rev=[]
for i in range(len(arr)-1,-1,-1):
    rev.append(arr[i])

print(rev)

#reverse through slicing method
rev1=arr[::-1]
print(rev1)
arr.reverse()
print(arr)

#find numbers of element in the array which is divisible by 2
count=0
for i in range (len(arr)):
	if arr[i]%2==0:
	    count=count+1
print("total even number is ",count)

#find the unique element
