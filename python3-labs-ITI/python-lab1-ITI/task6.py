# Write a function that takes a string and prints the
# longest alphabetical ordered substring occured. For
# example, if the string is 'abdulrahman' then the
# output is: Longest substring in alphabetical order is:
# abdu

def longest_alphabetical_substring(s):
    longest = ''
    current = ''

    for char in s:
        if not current or char >= current[-1]: 
            current += char
        else:
            current = char 
        
        if len(current) > len(longest):
            longest = current

    print("Longest substring in alphabetical order is:", longest)

text = input("Enter a string: ")
longest_alphabetical_substring(text)

