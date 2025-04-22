# check whether the string is palindrome or not

s1 = input("Enter a string: ").replace(' ','').lower()
rev_s1 = s1[ : :-1]

if s1 == rev_s1:
    print('string is palindrome')
else:
    print('Not a palindrome')    
