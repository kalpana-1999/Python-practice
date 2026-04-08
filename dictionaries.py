# Dictionaries: A dictionary is an unorderd collection of keys and values. It is defined using curly braces and can contain elements of different
# data types. Each key is unique and maps to a value. Dictionaries are mutable, meaning you can change their content after creation.

# Banana
student = {
    "name": "Priya",
    "age": 21,
    "marks": 95,
    "city": "Patna"
}

# Access
print(student["name"])        # Priya
print(student.get("age"))     # 21 (safe way)
print(student.get("phone", "Not found"))  # Not found

# Add / Update
student["email"] = "priya@gmail.com"  # add
student["age"] = 22                    # update

# Delete
del student["city"]
student.pop("marks")

# Loop
for key, value in student.items():
    print(f"{key}: {value}")

# Keys aur Values alag
print(student.keys())    # dict_keys(['name', 'age', ...])
print(student.values())  # dict_values(['Priya', 22, ...])

# Nested Dictionary (AI/ML mein common)
dataset = {
    "train": {"size": 8000, "accuracy": 0.95},
    "test":  {"size": 2000, "accuracy": 0.91}
}
print(dataset["train"]["accuracy"])  # 0.95