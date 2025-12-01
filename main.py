from add_module import add_record
from delete_module import delete_record
from update_module import update_record
from display_module import display_all_records

student_records = []


def display_main_menu():
    print("\nMAIN MENU:\n")
    print("1. Add Record")
    print("2. Delete Record")
    print("3. Update Record")
    print("4. Display All Records")
    print("5. Exit")



def main():
    while True:
        display_main_menu()

        try:
            choice = input("Select option to perform: ")

            if choice == '1':
                add_record(student_records)
            elif choice == '2':
                delete_record(student_records)
            elif choice == '3':
                update_record(student_records)
            elif choice == '4':
                display_all_records(student_records)
            elif choice == '5':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select an option between 1 and 5.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

