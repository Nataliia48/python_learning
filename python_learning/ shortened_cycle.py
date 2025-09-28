print("TASK 1: Dictionary with string values converted to uppercase")
print("="*60)

original_dict = {
    'name': 'john',
    'city': 'london',
    'country': 'england',
    'job': 'developer',
    'hobby': 'programming'
}

print(f"Original dictionary: {original_dict}")

uppercase_dict = {key: value.upper() for key, value in original_dict.items() if isinstance(value, str)}

print(f"Uppercase dictionary: {uppercase_dict}")
print()

print("TASK 2: Filter strings longer than 3 characters")
print("="*50)

string_list = ['cat', 'elephant', 'dog', 'butterfly', 'ant', 'tiger', 'bee', 'crocodile']

print(f"Original list: {string_list}")

filtered_list = [word for word in string_list if len(word) > 3]

print(f"Filtered list (length > 3): {filtered_list}")
print()

print("ADDITIONAL EXAMPLES")
print("="*40)

print("Task 1 - Mixed data types:")
mixed_dict = {
    'name': 'alice',
    'age': 25,
    'city': 'paris',
    'active': True,
    'email': 'alice@example.com'
}

print(f"Original: {mixed_dict}")
uppercase_mixed = {key: value.upper() for key, value in mixed_dict.items() if isinstance(value, str)}
print(f"Uppercase strings only: {uppercase_mixed}")
print()

print("Task 2 - Various string lengths:")
various_strings = ['a', 'ab', 'abc', 'abcd', 'abcde', 'hello', 'world', 'python', 'code']

print(f"Original: {various_strings}")
long_strings = [s for s in various_strings if len(s) > 3]
print(f"Length > 3: {long_strings}")

print("\nBoth tasks completed using shortened cycles (list/dict comprehensions)!")