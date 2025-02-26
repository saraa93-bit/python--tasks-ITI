# 4. Use the created Package in python code that takes
# input operand from User : 0->sum , 1->subtract ,
# 2->divide , 3 ->Multiple.
# a. If one of the two numbers is zero and operand
# is subtract raise Value Error with message “
# subtracting zero from Number “.
# b. If one of the two numbers is zero and operand
# is divide raise Zero division Error with message
# “ can’t divide with zero “.
# c. If one of the two numbers is zero and operand
# is Multiply raise Value Error with message “
# Multiply with Zero “.

# from Calculator import my_functions

# def main():
#     try:
#         a = int(input("Enter first number: "))
#         b = int(input("Enter second number: "))

#         print("Choose an operation:")
#         print("0 -> Sum")
#         print("1 -> Subtract")
#         print("2 -> Divide")
#         print("3 -> Multiply")
        
#         choice = int(input("Enter your choice from(0-3): "))

#         if choice == 0:
#             result = my_functions.sum_numbers(a, b)
#             print(f"Sum: {result}")

#         elif choice == 1:
#             result = my_functions.subtract_numbers(a, b)
#             print(f"Subtraction: {result}")

#         elif choice == 2:
#             result = my_functions.divide_numbers(a, b)
#             print(f"Division: {result}")

#         elif choice == 3:
#             result = my_functions.multiply_numbers(a, b)
#             print(f"Multiplication: {result}")

#         else:
#             print("Invalid choice!")

#     except ValueError as ve:
#         print("ValueError:", ve)

#     except ZeroDivisionError as zde:
#         print("ZeroDivisionError:", zde)

# if __name__ == "__main__":
#     main()

from find import find

original = "eueiieo"
modified = "iieoedue"

result = find(original, modified)

print(f"The extra character is: '{result}'")
