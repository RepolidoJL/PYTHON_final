def delete_record(records_list):
    print("\nDELETE RECORD MENU:")
    if not records_list:
        print("\nNo record/s available.")
        input("Press Enter to continue...")
        return


    student_no_to_delete = input("Enter the student no. of the record to delete: ").strip()


    target_index = -1
    target_record = None
    for i, record in enumerate(records_list):
        if record['Student No.'] == student_no_to_delete:
            target_index = i
            target_record = record
            break

    if target_record is None:
        print(f"\nNo record found.")
        input("Press Enter to continue...")
        return


    print(f"\nStudent No.: {target_record['Student No.']}")
    print(f"First Name: {target_record['First Name']}")
    print(f"Last Name: {target_record['Last Name']}")
    print(f"Age: {target_record['Age']}")
    print(f"Course: {target_record['Course']}")

    confirmation = input(
        "\nAre you sure you want to delete this record?\n"
        "Press [Y/y] – Yes || [N/n] – No: "
    ).strip().upper()

    if confirmation == 'Y':
        records_list.pop(target_index)
        print(f"\nRecord for Student No. {student_no_to_delete} deleted successfully!")
        input("Press Enter to continue...")
    elif confirmation == 'N':
        print("\nDeletion cancelled by the user.")
    else:
        print("\nInvalid confirmation input. Deletion cancelled.")
