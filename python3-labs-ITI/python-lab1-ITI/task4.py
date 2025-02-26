# 
# Write a function that takes a number as an
# argument and if the number divisible by 3 return
# "Fizz" and if it is divisible by 5 return "buzz" and if is
# is divisible by both return "FizzBuzz"
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return (number)

num = int(input("Enter a number: "))
result = fizz_buzz(num)
print("Result:", result)
