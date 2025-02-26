# Problems
# ●
# Write a function in Python that accepts two string parameters. The ﬁrst parameter will be a string of characters,
# and the second parameter will be the same string of characters, but they’ll be in a different order and have one
# extra character. The function should return that extra character.
# ○
# For example, if the ﬁrst parameter is “eueiieo” and the second is “iieoedue,” then the function should
# return “d.”
# ●
# Import the above function in another program ( ﬁle) and call it .

# find_extra.py

def find(str1, str2):
    
    sum1 = sum(ord(char) for char in str1)
    sum2 = sum(ord(char) for char in str2)
    
    extra_char = chr(abs(sum2 - sum1))
    return extra_char

if __name__ == "__main__":
    original = "eueiieo"
    modified = "iieoedue"
    print(f"Extra character: {find(original, modified)}")
