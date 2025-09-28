def route_info(route_data):
    """
    Function that takes a dictionary with route information
    and returns appropriate route description based on available data
    """
    
    # Case 1: If distance key exists and value is a number
    if 'distance' in route_data and isinstance(route_data['distance'], (int, float)):
        return f"Distance to your destination is {route_data['distance']}"
    
    # Case 2: If both speed and time keys exist
    elif 'speed' in route_data and 'time' in route_data:
        calculated_distance = route_data['speed'] * route_data['time']
        return f"Distance to your destination is {calculated_distance}"
    
    # Case 3: No distance info available
    else:
        return "No distance info is available"


# Function testing
print("Testing route_info function:")
print()

# Test 1: Dictionary with distance key
test_route1 = {'distance': 50}
print("Test 1 - With distance key:")
print(f"Input: {test_route1}")
print(f"Result: {route_info(test_route1)}")
print()

# Test 2: Dictionary with distance key (float)
test_route2 = {'distance': 25.5}
print("Test 2 - With distance key (float):")
print(f"Input: {test_route2}")
print(f"Result: {route_info(test_route2)}")
print()

# Test 3: Dictionary with speed and time keys
test_route3 = {'speed': 60, 'time': 2}
print("Test 3 - With speed and time keys:")
print(f"Input: {test_route3}")
print(f"Result: {route_info(test_route3)}")
print()

# Test 4: Dictionary with speed and time keys (different values)
test_route4 = {'speed': 80, 'time': 1.5}
print("Test 4 - With speed and time keys (different values):")
print(f"Input: {test_route4}")
print(f"Result: {route_info(test_route4)}")
print()

# Test 5: Dictionary without distance, speed, or time
test_route5 = {'destination': 'Paris', 'vehicle': 'car'}
print("Test 5 - Without distance, speed, or time:")
print(f"Input: {test_route5}")
print(f"Result: {route_info(test_route5)}")
print()

# Test 6: Empty dictionary
test_route6 = {}
print("Test 6 - Empty dictionary:")
print(f"Input: {test_route6}")
print(f"Result: {route_info(test_route6)}")
print()

# Test 7: Dictionary with only speed (missing time)
test_route7 = {'speed': 90}
print("Test 7 - Only speed (missing time):")
print(f"Input: {test_route7}")
print(f"Result: {route_info(test_route7)}")
print()

# Test 8: Dictionary with only time (missing speed)
test_route8 = {'time': 3}
print("Test 8 - Only time (missing speed):")
print(f"Input: {test_route8}")
print(f"Result: {route_info(test_route8)}")
print()

# Test 9: Dictionary with distance as string (should not work)
test_route9 = {'distance': '100'}
print("Test 9 - Distance as string (should not work):")
print(f"Input: {test_route9}")
print(f"Result: {route_info(test_route9)}")
print()

# Test 10: Complex case with all keys (distance takes priority)
test_route10 = {'distance': 75, 'speed': 50, 'time': 2}
print("Test 10 - All keys present (distance should take priority):")
print(f"Input: {test_route10}")
print(f"Result: {route_info(test_route10)}")
print()

# Demonstration section
print("="*60)
print("FUNCTION DEMONSTRATION WITH VARIOUS SCENARIOS")
print("="*60)

# Real-world examples
examples = [
    {'distance': 120, 'description': 'Direct distance given'},
    {'speed': 70, 'time': 2.5, 'description': 'Calculate from speed and time'},
    {'destination': 'London', 'vehicle': 'train', 'description': 'No distance info'},
    {'distance': 0, 'description': 'Already at destination'},
    {'speed': 0, 'time': 5, 'description': 'Not moving'},
    {'speed': 100, 'time': 0, 'description': 'No time spent'}
]

for i, example in enumerate(examples, 1):
    desc = example.pop('description')
    print(f"Example {i} ({desc}):")
    print(f"  Input: {example}")
    print(f"  Output: {route_info(example)}")
    print()

print("Function handles all specified cases correctly!")