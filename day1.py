# Program 1: Print name
print("My name is Veshal")

# Program 2: Add two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)

# Program 3: Even or Odd
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Program 4: Area of rectangle
length = float(input("Length: "))
breadth = float(input("Breadth: "))
print("Area =", length * breadth)

# Program 5: Simple Interest
p = float(input("Principal: "))
t = float(input("Time: "))
r = float(input("Rate: "))
si = (p * t * r) / 100
print("Simple Interest =", si)