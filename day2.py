# Day 2 – Conditions and Loops
# Topics: if-else, for loop, while loop
# Author: Veshal


# Program 1: Positive, Negative or Zero
n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


# Program 2: Print numbers from 1 to 5
for i in range(1, 6):
    print(i)


# Program 3: Sum of first n numbers
n = int(input("Enter n: "))
total = 0
i = 1

while i <= n:
    total += i
    i += 1

print("Sum =", total)

