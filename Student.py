# Student Profile Card

name = input("Name: ")
age =int(input("Age: "))
course = input("course: ")
city = input("city: ")
goal = input("Goal: ")

# Bonus 1: Validate age
if age < 0 or age > 120:
    print("Error: Age must be between 0 and 120")
else:
    # Calculate birth year and years until 30
    birth_year = 2026 - age
    years_until_30 = 30 - age

    print("\n================================")
    print("        STUDENT PROFILE")
    print("================================")
    print(f"Name:    {name}")
    print(f"Age:     {age} years old")
    print(f"Course:  {course}")
    print(f"City:    {city}")
    print(f"Goal:    {goal}")
    print(f"Born:    ~{birth_year}")

    if years_until_30 > 0:
        print(f"Years until 30: {years_until_30}")
    elif years_until_30 == 0:
        print("Years until 30: You are 30!")
    else:
        print(f"Years since 30: {abs(years_until_30)}")

    print("================================")

    # Bonus 2: GPA / Dean's List
    gpa = float(input("\nEnter your GPA: "))

    if gpa >= 3.5:
        print("Dean's List: Yes")
    else:
        print("Dean's List: No")


