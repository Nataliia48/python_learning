def image_info(image_data):
    """
    Function that takes a dictionary with image information
    and returns a formatted string with description
    """
    # Check if required keys exist
    if 'image_id' not in image_data:
        raise TypeError("Missing required key: 'image_id'")
    
    if 'image_title' not in image_data:
        raise TypeError("Missing required key: 'image_title'")
    
    # Format and return the string
    return f"Image '{image_data['image_title']}' has id {image_data['image_id']}"


# Function testing
print("Testing image_info function:")
print()

# Test 1: Valid data
test_data1 = {
    'image_id': 5136,
    'image_title': 'my cat'
}

print("Test 1 - Valid data:")
print(f"Input data: {test_data1}")
result1 = image_info(test_data1)
print(f"Result: {result1}")
print()

# Test 2: Additional keys (don't affect functionality)
test_data2 = {
    'image_id': 1234,
    'image_title': 'sunset',
    'size': '1920x1080',
    'format': 'jpg'
}

print("Test 2 - With additional keys:")
print(f"Input data: {test_data2}")
result2 = image_info(test_data2)
print(f"Result: {result2}")
print()

# Test 3: Missing image_id
print("Test 3 - Missing image_id:")
test_data3 = {
    'image_title': 'beach photo'
}
print(f"Input data: {test_data3}")
try:
    result3 = image_info(test_data3)
    print(f"Result: {result3}")
except TypeError as e:
    print(f"Error: {e}")
print()

# Test 4: Missing image_title
print("Test 4 - Missing image_title:")
test_data4 = {
    'image_id': 9999
}
print(f"Input data: {test_data4}")
try:
    result4 = image_info(test_data4)
    print(f"Result: {result4}")
except TypeError as e:
    print(f"Error: {e}")
print()

# Test 5: Empty dictionary
print("Test 5 - Empty dictionary:")
test_data5 = {}
print(f"Input data: {test_data5}")
try:
    result5 = image_info(test_data5)
    print(f"Result: {result5}")
except TypeError as e:
    print(f"Error: {e}")
print()

# Demonstration of proper usage
print("="*50)
print("FUNCTION DEMONSTRATION")
print("="*50)

# Examples of different images
images = [
    {'image_id': 5136, 'image_title': 'my cat'},
    {'image_id': 1001, 'image_title': 'vacation photo'},
    {'image_id': 2022, 'image_title': 'birthday party'},
    {'image_id': 3456, 'image_title': 'mountain landscape'}
]

for i, img in enumerate(images, 1):
    print(f"Image {i}: {image_info(img)}")

print()
print("Function successfully handles all cases according to requirements!")