print("Welcome To My To-Do List")
To_Do = []

while True:
    user_choice = int(input("Select 1 to add:\n"
                            "Select 2 to update:\n"
                            "Select 3 to delete:\n"
                            "Select 4 to view list:\n"
                            "Select 5 to exit:\n"))
    
    # Comparing user's choice
    if user_choice == 1:
        activity = input("enter activity you want to add: \n")
        To_Do.append(activity)
        print(f"{activity} added successfully")
    elif user_choice == 2:
        if not To_Do:
            print("Nothing to update, Kindly add an activity")
        else:
            index = int(input("Enter the index of the activity to update: "))
            if 0 <= index < len(To_Do):
                new_update = input("Enter update: \n")
                To_Do[index] = new_update
                print(f"'{new_update}' updated successfully")
            else:
                print("Invalid index")
    elif user_choice == 3:
        if not To_Do:
            print("Nothing to delete, Kindly select an activity to delete")
        else:
            index = int(input("Enter the index of the activity to delete: "))
            if 0 <= index < len(To_Do):
                deleted_activity = To_Do.pop(index)
                print(f"'{deleted_activity}' deleted successfully")
            else:
                print("Invalid index")
    elif user_choice == 4:
        print(To_Do)
    elif user_choice == 5:
        exit(1)
    else:
        print("Kindly Select an option between 1 - 5")