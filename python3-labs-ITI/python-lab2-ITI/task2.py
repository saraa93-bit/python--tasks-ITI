# 2️ Convert two lists into a dictionary
def lists_to_dict(list1, list2):
    return dict(zip(list1, list2))

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
print(lists_to_dict(list1, list2))