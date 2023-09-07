tasklist = []

def add_task():
    while True:
        addtask = input("Would you like to add a task? ")
        if addtask.lower() == "yes":   
            added_task = input("Add your task here: ")
            tasklist.append(added_task)
            print(f'Task added. Updated tasks: {tasklist}')
        elif addtask.lower() == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def view_task():
    while True:
        view_tasks = input("Would you like to view your current tasks? ")
        if view_tasks.lower() == "yes":
            if tasklist:
                print(tasklist)
            else:
                print("No tasks availiable.")
            break
        elif view_tasks.lower() == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def remove_task():
    while True:
        print(tasklist)
        delete_task = input("Would you like to remove a task? ")
        if delete_task.lower() == "yes":
            delete_this_task = input("Please enter a task you would like to remove: ")
            tasklist.remove(delete_this_task)
            print(f'Task removed. Updated tasks: {tasklist}')
            break
        elif delete_task.lower() == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def exit_program():
    print("Goodbye!")


# greet user
print("Welcome to this To-Do List program! \n 1. Add a task \n 2. View tasks \n 3. Remove a task \n 4. Exit")


# prompt user for add/view/remove tasks or exit
while True:
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        exit_program()
        break
    else:
        print("Invalid answer. Please pick a listed number.")