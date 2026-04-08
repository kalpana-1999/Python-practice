# Set: A set is an unordered collection of unique items. It is defined using curly braces and can contain elements of different data types. 

set_1={
    3,"Hello Kalpan",True,5.3,45,"Laila",67,8.9
}
print(set_1)

# duplicate values automatically removes from set
set_2={4,6,7,3,4,5,6,7,8,1,2,3,4}
print(set_2)

a={4,3,4,5,6,7}
b={3,5,2,1}

#operations on sets
print(a|b)  # union(values from both sets)
print(a&b)  # intersection(values common to both sets)
print(a-b)  # difference(values in a but not in b)
print(b-a)  # difference(values in b but not in a)

# Use case (NLP me automatically unique words nikal dete hai)
message="Hello Kalpana, Tum kaisi ho Kalpana?"
unique_words=set(message.split())
print(unique_words)