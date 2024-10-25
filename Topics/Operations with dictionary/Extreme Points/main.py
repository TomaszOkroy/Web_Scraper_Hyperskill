# The following line creates a dictionary from the input. Do not modify it, please
import operator

test_dict = json.loads(input())

min_value = min(test_dict, key=test_dict.get)
max_value = max(test_dict, key=test_dict.get)
print(f"min: {min_value}")
print(f"max: {max_value}")

# Work with the 'test_dict'