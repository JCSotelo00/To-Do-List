# greet user
print("Welcome to the To-Do List app! \n 1. Add a task \n 2. View tasks \n 3. Remove a task \n 4. Exit")

choice = input("Enter your choice: ")

# prompt user for add/view/remove tasks or exit
while True:
    if choice == "1":
        add_task = input("would you like to enter a task? ") # anything but yes gives infinity loop. find a way to fix that
        break
        if add_task == "yes":   
            added_task = input("Add your task here: ") # add task to a list
            break
    elif choice == "2":
        print("you chose to view your current tasks!") # call a viewtask program
        break
    elif choice == "3":
        print("you chose to remove a task!") # call a removetask program
        break
    elif choice == "4":
        print("Bye!")
        break
    else:
        print("Please enter a listed number.") # find a way to ask again
        break


# later find a way to ignore capitalizations/lowercases

# the essence that makes something the kind of thing it is when you homegenize a city you destroy its feeling of urbanity. ms schulman said, referring to the banks and drugstores and chains retailers steadily
# wallpapering over the cities indespensible quiddies. New your times( feb 25 2020) quiddity can refer to the essence of something or to a trivial distraction