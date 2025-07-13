# the pangram function checks if a given sentence contains every letter of the alphabet at least once.
def pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sentence_set = set(sentence.lower())
    return alphabet.issubset(sentence_set)
# Example usage:
sentence = "The quick brown fox jumps over the lazy dog"
is_pangram = pangram(sentence)
print(f"The sentence is a pangram: {is_pangram}.")
# Example usage:
# The sentence is a pangram: True.

