# Write a function that accepts two arguments (length,
# start) to generate an array of a specific length filled
# with integer numbers increased by one from start.

def generate_array(length, start):
    return [start + i for i in range(length)]

length = int(input("Enter the length of the array: "))
start = int(input("Enter the starting number: "))

result = generate_array(length, start)
print("Generated Array:", result)
