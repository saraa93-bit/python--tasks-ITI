import json
import os
from datetime import datetime

PROJECTS_FILE = "database/projects.json"

def load_projects():
    if not os.path.exists(PROJECTS_FILE):
        return []
    with open(PROJECTS_FILE, "r") as file:
        return json.load(file)

def save_projects(projects):
    with open(PROJECTS_FILE, "w") as file:
        json.dump(projects, file, indent=4)

def create_project(user):
    projects = load_projects()
    
    title = input("Enter Project Title: ")
    details = input("Enter Project Details: ")
    target = input("Enter Fundraising Target Amount (EGP): ")

    try:
        target = float(target)
    except ValueError:
        print("Invalid amount .")
        return
    
    start_date = input("Enter Start Date (YYYY-MM-DD): ")
    end_date = input("Enter End Date (YYYY-MM-DD): ")

    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        if end_date <= start_date:
            print(" End date must be after start date!")
            return
    except ValueError:
        print(" Invalid date format!")
        return

    project = {
        "id": len(projects) + 1,
        "title": title,
        "details": details,
        "target": target,
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
        "owner": user["email"]
    }
    
    projects.append(project)
    save_projects(projects)
    print(" Project created successfully..")

def view_projects():
    projects = load_projects()
    if not projects:
        print("No projects available.")
        return

    for project in projects:
        print(f"\n🔹 {project['title']} - {project['details']} (Target: {project['target']} EGP)")
        print(f"Start: {project['start_date']} - End: {project['end_date']}")

def delete_project(user):
    projects = load_projects()
    project_id = int(input("Enter Project ID to delete: "))
    
    for project in projects:
        if project["id"] == project_id and project["owner"] == user["email"]:
            projects.remove(project)
            save_projects(projects)
            print(" Project deleted successfully.")
            return
    
    print(" Project not found or you don't have permission to delete it.")

def search_project_by_date():
    search_date = input("Enter a date (YYYY-MM-DD) to search for projects: ")
    
    try:
        search_date = datetime.strptime(search_date, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        print("Invalid date format!")
        return

    projects = load_projects()
    found_projects = [p for p in projects if p["start_date"] <= search_date <= p["end_date"]]

    if not found_projects:
        print("No projects found on this date.")
        return

    for project in found_projects:
        print(f"\n🔹 {project['title']} - {project['details']} (Target: {project['target']} EGP)")
        print(f"Start: {project['start_date']} - End: {project['end_date']}")
