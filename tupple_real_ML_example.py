#Tupple: tupples are immutable and ordered collection of items. They are defined using parnenthesis and can contain elements of different data types.
student1=(80,70,5,1)
student2=(79,70,6,1)
student3=(56,45,"Patna",0)

# Unpacking with meaningful names ........................Aise unpacking karne se ek ek line khud likhni padti hai but it is more readable and easy to understand
marks,attendance,study_hour,result=student3
marks,attendance,City,result=student3
print(f"City:{City}")

# f"" ek formatted string hai jo text aur value ko likhne me aasan banata hai aru agr value likhni hai to {} ke andar likh sakte hai ye new way hai "
print(f"Marks: {marks}, Attendance: {attendance}%, Study Hours: {study_hour}, Result: {'Pass' if result == 1 else 'Fail'}")


# Ab ek ML ka example lete hai ki kaise ML me bahut sare data ka result kaise alag alag karte hai

# dataset - list of tuples
dataset=[
    (80,70,5,1),
    (79,70,6,1),
    (56,45,2,0),
    (90,80,7,1),
    (60,50,3,0)
]
# Separate features and labels---------------------ek tarika ya hai 
"""
features=[(marks,attendance,study_hour) for marks,attendance,study_hour,result in dataset]
labels=[result for marks,attendance,study_hour,result in dataset]
print("Features:", features)
print("Labels:", labels)

"""
# Dusra tarika ya hai
X=[]
Y=[]
for *features,labels in dataset:
    X.append(features)
    Y.append(labels)

print(f"Features: {X} \n Labels:{Y}")