def add_record(records_list):
    print("\nADD RECORD MENU:")


    while True:
        student_no = input("Enter Student No.: ").strip()
        if not student_no.isdigit():
            print("Invalid input. Student No. must be numeric.")
            input("Press Enter to continue...")
            continue


        if any(record['Student No.'] == student_no for record in records_list):
            print(f"\nStudent No. already exists.")
            continue
        break

    firstname = input("Enter First Name: ").strip()
    lastname = input("Enter Last Name: ").strip()

    while True:
        age_input = input("Enter Age: ").strip()
        if age_input.isdigit():
            age = int(age_input)
            break
        print("Invalid input. Age must be a number.")

    course = input("Enter Course: ").strip().upper()

    new_record = {
        'Student No.': student_no,
        'First Name': firstname,
        'Last Name': lastname,
        'Age': age,
        'Course': course
    }

    records_list.append(new_record)
    print("\nRecord has been successfully added.")
    input("Press Enter to continue...")
