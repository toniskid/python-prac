def main():
    gradebook = {}

    while True:
        show_menu()
        choice = input("Choose 1-4: ")

        try:
            if choice == "1":
                name = input("Student name: ").strip()
                add_student(gradebook, name)
                print("Added", name)

            elif choice == "2":
                name = input("Student name: ").strip()
                score = float(input("Score (0-100): "))
                add_score(gradebook, name, score)
                print("Score saved")

            elif choice == "3":
                print_report(gradebook)

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Please type 1, 2, 3 or 4")

        except ValueError as error:
            print("Problem:", error)


main()
    