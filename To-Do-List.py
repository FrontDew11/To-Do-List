
tasks = []

print("Welcome to the to do list app")

while True:
    user_input = input("Would you like to : 1.add task 2. delete task 3. show tasks 4. Exit app:")

    if user_input == "1":
        task_name = input("Enter name of the task:")
        tasks.append(task_name)
    elif user_input == "2":
        task_to_remove = int(input("Enter number of task you want to delete:"))
        try:
            tasks.pop(task_to_remove - 1)
        except IndexError:
            print("Such task is not existing")
    elif user_input == "3":
        if tasks == []:
            print("Courently you don't have any tasks")
        else:
            for i, task in enumerate(tasks,start=1):
                print (f"{i} . {task}")
    elif user_input == "4":
        break
    else:
        print("Please enter a valid choice!")
print("Thank you for using to do list app")
