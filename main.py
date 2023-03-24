#To do list app
listToDo = []
userOption = ""
userTask = ""

print("Welcome in to do list app!")

try:
    while userOption != "4":
        print("\nWhat you want to do?(to choose enter action number.")
        print("1. Add task to list")
        print("2. Print all tasks in list")
        print("3. Remove task from list")
        print("Enter \"4\" to close app.")
        print("Choose action: ")

        userOption = input()

        if userOption == "1":
                print("Write task to do: ")
                userTask = input()
                listToDo.append(userTask)
        elif userOption == "2":
                taskNumber = 1
                for i in listToDo:
                    print(str(taskNumber) + ". " + i)
                    taskNumber+=1
                if taskNumber == 1:
                    print("List is empty!")
        elif userOption == "3":
                print("\nEnter number of task to remove it from task list.\n")
                taskNumber = 1
                for i in listToDo:
                    print(str(taskNumber) + ". " + i)
                    taskNumber+=1
                if taskNumber == 1:
                    print("List is empty!\n")
                else:
                    print("Remove: ")
                    taskToRemove = int(input())
                    listToDo.pop(taskToRemove - 1)
        elif userOption == "4":
            print("App is closed.")
        else:
            print("Wrong data!")
except:
    print("An exception occurred")
