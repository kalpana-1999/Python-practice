def sub_product_sum(x):
    temp=x
    sum=0
    product=1

    while temp>0:
        r=temp%10
        sum=sum+r
        product=product*r
        temp=temp//10
    print(f"sum {sum} and product is {product}")

    return product-sum

res=sub_product_sum(345)
print(res)