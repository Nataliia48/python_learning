def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice", 25) 
greet("Bob", 30)


def sum_numbers(*numbers):
    total = sum(numbers)
    print(f"Sum: {total}")

sum_numbers(1, 2, 3)
sum_numbers(5, 10, 15, 20)