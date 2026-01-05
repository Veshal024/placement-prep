# Program 1: Simple function
def greet():
    print("Hello, welcome to Python functions!")

greet()
# Program 2: Function with parameters
def add(a, b):
    print("Sum =", a + b)

add(10, 20)
add(5, 7)
# Program 3: Function with return value
def square(n):
    return n * n

result = square(4)
print("Square =", result)
# Program 4: Function with user input
def even_or_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

num = int(input("Enter a number: "))
even_or_odd(num)
