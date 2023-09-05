# greet user
print("Welcome to the To-Do List app! \n 1. Add a task \n 2. View tasks \n 3. Remove a task \n 4. Exit")



def add_task():
    addtask = input("Would you like to add a task? ") # anything but yes gives infinity loop. find a way to fix that
    if addtask == "yes":   
        added_task = input("Add your task here: ") # add task to a list
    # make else to return to menu

def view_task():
    print("you chose to view your tasks!")

def remove_task():
    print("you chose to remove a task!")

def exit():
    print("Goodbye!")



# prompt user for add/view/remove tasks or exit
while True:
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
        break
    elif choice == "2":
        view_task()
        break
    elif choice == "3":
        remove_task()
        break
    elif choice == "4":
        exit()
        break
    else:
        print("Invalid answer. Please pick a listed number.")

# later find a way to ignore capitalizations/lowercases