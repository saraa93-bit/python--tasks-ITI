# Write a Python function that checks whether a
# passed string is palindrome or not.Note: A
# palindrome is a word, phrase, or sequence that
# reads the same backward as forward, e.g., madam
# or nurses run {ignoring the spaces }.

def is_palindrome(s):
    clean_s = s.replace(" ", "").lower()
    
    return clean_s == clean_s[::-1]

text = input("Enter a string: ")

if is_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
