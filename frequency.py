arr=[4,6,7,8,3,5,4,4,7]

dict={}
for i in arr:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)