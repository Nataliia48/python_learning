def dict_to_list(dictionary):
    result = []
    
    for key, value in dictionary.items():
        if isinstance(value, int):
            result.append((key, value * 2))
        else:
            result.append((key, value))
    
    return result


def filter_list(input_list, filter_type):
    result = []
    
    for item in input_list:
        if isinstance(item, filter_type):
            result.append(item)
    
    return result


print("TASK 1: dict_to_list function")
print("="*40)

test_dict1 = {'a': 10, 'b': 'hello', 'c': 5, 'd': True}
print(f"Input dictionary: {test_dict1}")
result1 = dict_to_list(test_dict1)
print(f"Result: {result1}")
print()

test_dict2 = {'name': 'John', 'age': 25, 'score': 100, 'active': False}
print(f"Input dictionary: {test_dict2}")
result2 = dict_to_list(test_dict2)
print(f"Result: {result2}")
print()

test_dict3 = {'x': 3.14, 'y': 7, 'z': 'text'}
print(f"Input dictionary: {test_dict3}")
result3 = dict_to_list(test_dict3)
print(f"Result: {result3}")
print()

print("TASK 2: filter_list function")
print("="*40)

test_list = [35, True, 'abc', 10]
print(f"Input list: {test_list}")
result_int = filter_list(test_list, int)
print(f"filter_list({test_list}, int) = {result_int}")
print()

print("Additional tests:")

result_str = filter_list([1, 'hello', 2.5, 'world', True], str)
print(f"Filter strings: {result_str}")

result_float = filter_list([1, 2.5, 'text', 3.14, True], float)
print(f"Filter floats: {result_float}")

result_bool = filter_list([1, True, 'text', False, 3.14], bool)
print(f"Filter booleans: {result_bool}")

result_empty = filter_list([], int)
print(f"Filter from empty list: {result_empty}")

result_none = filter_list([1, 2, 3], str)
print(f"Filter type not in list: {result_none}")

print()

print("COMPREHENSIVE DEMONSTRATION")
print("="*50)

complex_dict = {
    'count': 42,
    'name': 'Python',
    'version': 3.9,
    'active': True,
    'users': 1000000,
    'description': 'Programming language'
}

print("Task 1 - Complex dictionary:")
print(f"Input: {complex_dict}")
complex_result = dict_to_list(complex_dict)
print(f"Output: {complex_result}")
print()

mixed_list = [1, 'hello', 3.14, True, [1, 2], {'a': 1}, None, 42, 'world']

print("Task 2 - Mixed data types:")
print(f"Original list: {mixed_list}")
print(f"Integers: {filter_list(mixed_list, int)}")
print(f"Strings: {filter_list(mixed_list, str)}")
print(f"Floats: {filter_list(mixed_list, float)}")
print(f"Booleans: {filter_list(mixed_list, bool)}")
print(f"Lists: {filter_list(mixed_list, list)}")
print(f"Dictionaries: {filter_list(mixed_list, dict)}")

print("\nBoth functions work correctly with for loops as required!")