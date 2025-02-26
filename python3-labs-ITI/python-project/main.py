from authentication import register, login
from projects import create_project, view_projects, delete_project, search_project_by_date

def main():
    print(" Welcome to the Crowd-Funding App")
    
    while True:
        print("\n1️- Register\n2️- Login\n3️- Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                while True:
                    print("\n Project Management:")
                    print("1️ Create Project\n2️ View Projects\n3️ Delete Project\n4️ Search by Date\n5️ Logout")
                    proj_choice = input("Enter your choice: ")

                    if proj_choice == "1":
                        create_project(user)
                    elif proj_choice == "2":
                        view_projects()
                    elif proj_choice == "3":
                        delete_project(user)
                    elif proj_choice == "4":
                        search_project_by_date()
                    elif proj_choice == "5":
                        break
        elif choice == "3":
            print(" Goodbye!")
            break

if __name__ == "__main__":
    main()
