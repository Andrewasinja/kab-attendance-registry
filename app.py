from roster import create_student, log_check_in, today_summary

def main():
    while True:
        print("\n=== KAB Attendance Registry ===")
        print("1. Register Student")
        print("2. Check-In Student (Present/Late)")
        print("3. View Today's Check-Ins")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == "1":
            sid = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            create_student(sid, name)
        elif choice == "2":
            sid = input("Enter Student ID: ")
            status = input("Status (Present/Late): ").capitalize()
            log_check_in(sid, status)
        elif choice == "3":
            today_summary()
        elif choice == "4":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()