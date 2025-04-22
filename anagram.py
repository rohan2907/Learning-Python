# Get set of 2 strings and compare them if they are anagrams or not

s1 = input("Enter a string: ").lower()
s2 = input("Enter a string: ").lower()

for x in s1:
    if x.isalpha():
        if s1.count(x) != s2.count(x):
            print('Not Anagrams')
            break
else:
    print('It is Anagram')        