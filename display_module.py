def display_all_records(records_list):

    print("\nDISPLAY ALL RECORD MENU:")

    if not records_list:
        print("\nNo records available.")
        input("Press Enter to continue...")
        return


    for index, record in enumerate(records_list, 1):
        print(f"{index}. Student No.: {record.get('Student No.',)}")
        print(f"   First Name: {record.get('First Name',)}")
        print(f"   Last Name: {record.get('Last Name',)}")
        print(f"   Age: {record.get('Age',)}")
        print(f"   Course: {record.get('Course',)}")

    print("\n======== End of Records ========")
    input("Press Enter to continue...")
