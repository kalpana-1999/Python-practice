# Tuple: Tuple is an ordered (ordered ka matlb jis index pe aapne jo value di hai wo hamesha usi index pe rahegi) and immutable 
# (immutable ka matlb aap usme se kisi bhi value ko change nahi kar sakte) collection of items. They are defined using parentheses 
# and can contain elements of different data types.

tuple_1=(5,"Hello Rahul",3.14,True,[1,2,3],(4,5,6))
print(tuple_1)
# tuple_1[0]=10 # ye error dega kyuki tuple immutable hota hai
print(tuple_1[0]) # ye 5 print karega kyuki tuple immutable hota hai
print(tuple_1[-1]) # ye (4,5,6) print karega kyuki tuple immutable hota hai
print(tuple_1[4]) # ye [1,2,3] print karega kyuki tuple immutable hota hai


tuple_2=(45,56,75,34,23,55,67,89,90)

first,*middle,last=tuple_2   #(tupple unpacking karne ka tarika agr *lagane se sab ek list me aa jata hai first likhne pe pehla element, last likhne pe last element aur *middle likhne par sab ek list me aa jata hai)
print(f"First:{first},Middle:{middle},Last:{last}")
# Tuple ko aise jagh use karna chahiye jaha aapko data ko change nahi karna ho aur aapko data ke order ki zarurat ho jaise ki coordinates, RGB values, etc. 

