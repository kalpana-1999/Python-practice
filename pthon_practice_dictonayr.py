student={
    "name": "Priya",
    "age":21,
    "gender":"Female"
    }

print(student["age"])
print(student["name"])
print(student["gender"])

for x in student:
    print(x)

x=student.keys()
print(x)

student["marks"]=95
print(student)