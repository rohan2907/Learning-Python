## Invert a dictionary
# This function takes a dictionary and returns a new dictionary with keys and values inverted.

# before - {'a': 1, 'b': 2, 'c': 3}
# after - {1: 'a', 2: 'b', 3: 'c'}

def invert_dict(original_dict, /):
    inverted_dict = {}
    for key, value in original_dict.items():
        inverted_dict[value] = key
    return inverted_dict

# Example usage
original = {'a': 1, 'b': 2, 'c': 3}
inverted = invert_dict(original)
print(f"Original dictionary: {original}")
print(f"Inverted dictionary: {inverted}")

