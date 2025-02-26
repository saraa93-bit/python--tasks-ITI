# 4️  List operations on [3,6,4,0,8]
def modify_list():
    my_list = [3, 6, 4, 0, 8]  

    my_list.pop()          
    my_list.insert(1, 'R')   

    print("Current List:", my_list)
    
    to_remove = input("Enter a number to remove from the list: ")

    if to_remove.isdigit():
        to_remove = int(to_remove)

    if to_remove in my_list:
        my_list.remove(to_remove)
    else:
        print("Element not found.")

    print("Updated List:", my_list)

modify_list()
