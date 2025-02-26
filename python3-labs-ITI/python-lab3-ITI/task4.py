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


def triangle(a, b, c):
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if triangle(a, b, c):
    print("This is a right triangle.")
else:
    print("This is NOT a right triangle.")
