def count_digit(nmr):
    temp=nmr
    count=0
    
    while (temp>0):
        r=temp%10
        if(r!=0 and nmr%r==0):
            count+=1
        temp=temp//10
    return count

res=count_digit(420)    # 420 ek classic case hai jisme 0 se divide karne par zero division error aata hai aur crash ho jata hai is liye r!=0 condition dena para....
print(res)