def is_palindrome(s):
    return s == s[::-1]

text = input("Enter a string: ")
if is_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")