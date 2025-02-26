# 3️ Create and print list of squares from 1 to 30
def square_list():
    squares = [x**2 for x in range(1, 31)]
    print(squares)

square_list()