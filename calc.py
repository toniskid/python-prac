#Grade calculator with feedback
def get_number_of_subjects():
    while True:
        raw = input("How many subjects do you want to enter? ")
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("Please enter a whole number greater than 0.")


def get_valid_score(subject_number):
    while True:
        raw = input(f"Enter score for subject {subject_number}: ")
        try:
            score = float(raw)
        except ValueError:
            print("That's not a number. Please try again.")
            continue

        if score < 0 or score > 100:
            print("Score must be between 0 and 100. Please try again.")
            continue

        return score


def get_grade_band(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def main():
    print("=== Grade Calculator with Feedback ===\n")

    num_subjects = get_number_of_subjects()

    scores = []
    for i in range(1, num_subjects + 1):
        score = get_valid_score(i)
        scores.append(score)

    total = sum(scores)
    average = total / len(scores)
    highest = max(scores)
    lowest = min(scores)
    below_50_count = sum(1 for s in scores if s < 50)
    grade_band = get_grade_band(average)
    pass_fail = "PASS" if average >= 50 else "FAIL"

    print("\n=== Report ===")
    print(f"Total score: {total:.1f}")
    print(f"Average score: {average:.2f}")
    print(f"Result: {pass_fail}")
    print(f"Grade band: {grade_band}")
    print(f"Highest score: {highest:.1f}")
    print(f"Lowest score: {lowest:.1f}")
    print(f"Subjects below 50: {below_50_count}")


if __name__ == "__main__":
    main()
