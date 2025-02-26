
# Fill an array of 5 elements from the user, Sort it in
# descending and ascending orders then display the
# output .
numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Original List:", numbers)
print("Ascending Order:", ascending)
print("Descending Order:", descending)
