def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                text = input("Task: ")
                priority = input("Priority (high/medium/low): ")
                add_task(tasks, text, priority)
                print("Task added.")

            elif choice == "2":
                view_tasks(tasks)

            elif choice == "3":
                view_tasks(tasks)
                number = int(input("Task number to mark done: "))
                mark_done(tasks, number - 1)
                print("Marked done.")

            elif choice == "4":
                print("Pending tasks:", count_pending(tasks))

            elif choice == "5":
                print("Goodbye!")
                break

            elif choice == "6":
                view_tasks(tasks)
                number = int(input("Task number to delete: "))
                delete_task(tasks, number - 1)
                print("Task deleted.")

            elif choice == "7":
                priority = input("Priority (high/medium/low): ").strip().lower()
                view_tasks(tasks, priority)

            else:
                print("Please choose a number from 1 to 7.")

        except ValueError as error:
            print("Problem:", error)


main()