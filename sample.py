import os
import time

projects = [
    {
        "id": 1,
        "name": "SchoolOS",
        "technology": ["Next.js", "React", "TypeScript", "Prisma", "PostgreSQL"],
        "status": "In Progress"
    },
    {
        "id": 2,
        "name": "Yatra Nepal",
        "technology": ["React", "Python", "Django", "MySQL", "Gemini"],
        "status": "Completed"
    },
    {
        "id": 3,
        "name": "Portfolio Website",
        "technology": ["Next.js", "React", "TypeScript", "CSS"],
        "status": "In Progress"
    }
]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_projects():
    print("\n========== MY PROJECTS ==========\n")

    if not projects:
        print("No projects available.")
        return

    for project in projects:
        print(f"ID       : {project['id']}")
        print(f"Name     : {project['name']}")
        print(f"Technology: {', '.join(project['technology'])}")
        print(f"Status   : {project['status']}")
        print("-" * 35)


def add_project():
    print("\n========== ADD PROJECT ==========")

    name = input("Project name: ")

    technologies = input(
        "Technologies (separate with comma): "
    ).split(",")

    technologies = [
        technology.strip()
        for technology in technologies
    ]

    status = input("Status: ")

    new_id = max(
        [project["id"] for project in projects],
        default=0
    ) + 1

    projects.append({
        "id": new_id,
        "name": name,
        "technology": technologies,
        "status": status
    })

    print("\nProject added successfully!")


def search_project():
    print("\n========== SEARCH PROJECT ==========")

    keyword = input("Enter project name: ").lower()

    found = False

    for project in projects:
        if keyword in project["name"].lower():
            print("\nProject Found!")
            print(f"ID: {project['id']}")
            print(f"Name: {project['name']}")
            print(f"Technology: {', '.join(project['technology'])}")
            print(f"Status: {project['status']}")
            found = True

    if not found:
        print("\nProject not found.")


def update_project():
    print("\n========== UPDATE PROJECT ==========")

    try:
        project_id = int(input("Enter project ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for project in projects:

        if project["id"] == project_id:

            print(f"\nCurrent name: {project['name']}")

            new_name = input(
                "New name (press Enter to keep current): "
            )

            if new_name:
                project["name"] = new_name

            print(f"Current status: {project['status']}")

            new_status = input(
                "New status (press Enter to keep current): "
            )

            if new_status:
                project["status"] = new_status

            print("\nProject updated successfully!")
            return

    print("\nProject not found.")


def delete_project():
    print("\n========== DELETE PROJECT ==========")

    try:
        project_id = int(input("Enter project ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for project in projects:

        if project["id"] == project_id:

            confirm = input(
                f"Delete '{project['name']}'? (y/n): "
            ).lower()

            if confirm == "y":
                projects.remove(project)
                print("\nProject deleted successfully!")
            else:
                print("\nDelete cancelled.")

            return

    print("\nProject not found.")


# ==============================
# MAIN PROGRAM
# ==============================

while True:

    clear_screen()

    print("""
╔══════════════════════════════════════╗
║       SUJAN'S PROJECT MANAGER        ║
╠══════════════════════════════════════╣
║  1. Show Projects                    ║
║  2. Add Project                      ║
║  3. Search Project                   ║
║  4. Update Project                   ║
║  5. Delete Project                   ║
║  6. Exit                             ║
╚══════════════════════════════════════╝
""")

    choice = input("Choose an option: ")

    clear_screen()

    if choice == "1":
        show_projects()

    elif choice == "2":
        add_project()

    elif choice == "3":
        search_project()

    elif choice == "4":
        update_project()

    elif choice == "5":
        delete_project()

    elif choice == "6":
        print("Thank you for using Sujan's Project Manager!")
        time.sleep(2)
        break

    else:
        print("Invalid choice. Please try again.")

    input("\nPress Enter to continue...")