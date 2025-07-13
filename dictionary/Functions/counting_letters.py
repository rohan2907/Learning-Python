# Count upper case and lower case letters in a string
def count(phrase):
    upper_count = sum(1 for char in phrase if char.isupper())
    lower_count = sum(1 for char in phrase if char.islower())
    return upper_count, lower_count

counts = count("Hello World")
print(f"Upper case letters: {counts[0]}, Lower case letters: {counts[1]}.")
# Example usage:
# Upper case letters: 2, Lower case letters: 8.
