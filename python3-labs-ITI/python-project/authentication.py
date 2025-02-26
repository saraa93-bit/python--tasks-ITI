import json
import re
import os
from utils import hash_password, validate_egyptian_phone

USER_FILE = "database/users.json"

def load_users():
    """to get users from JSON """
    if not os.path.exists(USER_FILE):
        return []
    with open(USER_FILE, "r") as file:
        return json.load(file)

def save_users(users):
    """ to post users in JSON """
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)

def register():
    users = load_users()

    email = input("Enter Email: ")
    if any(user["email"] == email for user in users):
        print(" Email already exists. Try logging in.")
        return

    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")

    password = input("Enter Password: ")
    confirm_password = input("Confirm Password: ")
    if password != confirm_password:
        print(" Passwords do not match!")
        return

    phone = input("Enter Mobile Number: ")
    if not validate_egyptian_phone(phone):
        print(" Invalid Egyptian phone number format!")
        return

    hashed_password = hash_password(password)
    users.append({"first_name": first_name, "last_name": last_name, "email": email, "password": hashed_password, "phone": phone})

    save_users(users)
    print(" Registration Successful..You can now log in.")

def login():
    users = load_users()
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    for user in users:
        if user["email"] == email and user["password"] == hash_password(password):
            print(f" Welcome {user['first_name']} > You are now logged in.")
            return user
    print(" Invalid email or password!")
    return None
