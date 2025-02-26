def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    return lines

file_path = 'sample.txt'
lines_list = read_file(file_path)
print("Lines from file:", lines_list)