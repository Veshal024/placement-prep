# Day 6 – Strings
# Topics: string basics, indexing, slicing, methods
# Author: Veshal
# Program 1: String basics
text = "Python Programming"
print(text)
print(type(text))
# Program 2: Indexing and length
word = "Python"
print(word[0])     # P
print(word[3])     # h
print(word[-1])    # n
print(len(word))
# Program 3: String slicing
print(word[0:3])   # Pyt
print(word[2:])    # thon
print(word[:4])    # Pyth
# Program 4: String methods
msg = " hello world "

print(msg.upper())
print(msg.lower())
print(msg.strip())
print(msg.replace("world", "Python"))
# Program 5: Count vowels in a string
s = input("Enter a string: ")
count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

print("Vowel count =", count)
