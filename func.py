# first function
def add_number(a, b):
    return a + b

add = add_number(4, -7)
print(add)

# second function
def greet(name="Jhon"):
    return f"Hi, {name}!"

your_name = greet("Jhon")
print(your_name)

#third function:
def max_of_three(a, b, c):
    number = (a, b, c)
    return max(number)

numbers = max_of_three(2, 6, 8)
print(numbers)

# fourth function:
def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply_all(3, 6, 8))
print(multiply_all())
