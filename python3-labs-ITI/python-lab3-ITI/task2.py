# 2. Create a list of strings , Add to it yourname then
# Write the list to a new File .

my_list = ["Hello", "saraa", "talat", "iti"]

my_list.append("talat")

def write_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(item + '\n')

new_file = 'output.txt'
write_file(new_file, my_list)
print(f"List written to {new_file}")
