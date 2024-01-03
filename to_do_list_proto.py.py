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
            old_activity = input("Enter the Activity to Update: ")
            new_activity = input("Enter the Updated Activity: ")
            if old_activity in To_Do:
                index = To_Do.index(old_activity)
                To_Do[index] = new_activity
                print("Activity Updated Successfully")
            else:
                print("Activity Not Found.")
    elif user_choice == 3:
        activity_to_delete = input("Enter the Activity to Delete: ")
        if activity_to_delete in To_Do:
            To_Do.remove(activity_to_delete)
            print(f"Activity '{activity_to_delete}' deleted Successfully!")
        else:
            print("Activity Not Found.")
    elif user_choice == 4:
        print(To_Do)
    elif user_choice == 5:
        exit(1)
    else:
        print("Kindly Select an option between 1 - 5")