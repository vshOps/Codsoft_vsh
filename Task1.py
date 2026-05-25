# TO-DO LIST APPLICATION

# Empty list to store tasks
tasks = []

# Function to show menu
def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

# Main program loop
while True:

    # Show menu options
    show_menu()

    # Take user choice
    choice = input("Enter your choice (1-4): ")

    # OPTION 1 → View Tasks
    if choice == "1":

        # Check if task list is empty
        if len(tasks) == 0:
            print("No tasks found.")

        else:
            print("\nYour Tasks:")

            # Display tasks one by one
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    # OPTION 2 → Add Task
    elif choice == "2":

        # Take new task input
        task = input("Enter new task: ")

        # Add task to list
        tasks.append(task)

        print("Task added successfully!")

    # OPTION 3 → Remove Task
    elif choice == "3":

        # Check if list is empty
        if len(tasks) == 0:
            print("No tasks to remove.")

        else:
            print("\nYour Tasks:")

            # Show all tasks
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            # Take task number to remove
            task_num = int(input("Enter task number to remove: "))

            # Check valid task number
            if 1 <= task_num <= len(tasks):

                # Remove task
                removed_task = tasks.pop(task_num - 1)

                print(f"'{removed_task}' removed successfully!")

            else:
                print("Invalid task number.")

    # OPTION 4 → Exit
    elif choice == "4":
        print("Exiting program...")
        break

    # Invalid input
    else:
        print("Invalid choice. Please try again.")