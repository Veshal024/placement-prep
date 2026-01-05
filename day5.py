# Day 5 – Dictionaries
# Topics: dictionary, keys, values, looping
# Author: Veshal
# Program 1: Dictionary basics
student = {
    "name": "Veshal",
    "age": 21,
    "course": "B.Tech AI"
}

print(student)
# Program 2: Access values
print(student["name"])
print(student["age"])
# Program 3: Add and update
student["college"] = "SRM"
student["age"] = 22

print(student)
# Program 4: Loop through dictionary
for key, value in student.items():
    print(key, ":", value)
# Program 5: Marks dictionary
marks = {
    "Maths": 85,
    "AI": 90,
    "Python": 88
}

total = 0
for subject in marks:
    total += marks[subject]

print("Total marks =", total)
print("Average =", total / len(marks))
