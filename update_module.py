def update_record(records_list):
    print("\nUPDATE RECORD MENU:")
    if not records_list:
        print("\nNo records available.")
        input("Press Enter to continue...")
        return

    student_no_to_update = input("\nEnter the student no. of the record to update: ").strip()

    target_record = None
    for record in records_list:
        if record['Student No.'] == student_no_to_update:
            target_record = record
            break

    if target_record is None:
        print(f"\nNo Record found.")
        input("Press Enter to continue...")
        return

    full_name = f"{target_record['First Name']} {target_record['Last Name']}"

    print(f"Student No.: {target_record['Student No.']}")
    print(f"Name: {full_name}")
    print(f"Age: {target_record['Age']}")
    print(f"Course: {target_record['Course']}")
    print("-" * 20)

    print("\nWhich specific record would you like to update?")
    print("[1] – First Name")
    print("[2] – Last Name")
    print("[3] – Age")
    print("[4] – Course")
    print("[5] – Exit")

    update_choice = input("Select option to perform: ").strip()

    if update_choice == '1':
        new_firstname = input(f"Enter corrected First Name: ").strip()
        target_record['First Name'] = new_firstname
        print("\nFirst Name has been successfully changed.")
        input("Press Enter to continue...")

    elif update_choice == '2':
        new_lastname = input(f"Enter corrected Last Name: ").strip()
        target_record['Last Name'] = new_lastname
        print("\nLast Name has been successfully changed.")
        input("Press Enter to continue...")

    elif update_choice == '3':

        while True:
            new_age_input = input(f"Enter corrected Age: ").strip()
            if new_age_input.isdigit():
                target_record['Age'] = int(new_age_input)
                print("\nAge updated successfully!")
                input("Press Enter to continue...")
                break
            print("Invalid input. Age must be a number.")

    elif update_choice == '4':
        new_course = input(f"Enter corrected Course: ").strip().upper()
        target_record['Course'] = new_course
        print("\nCourse updated successfully!")
        input("Press Enter to continue...")

    elif update_choice == '5':
        print("\nUpdate process cancelled by selecting Exit.")
    else:
        print("\nInvalid choice. Update aborted.")
