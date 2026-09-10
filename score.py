#we're creating a subject score analyzer
print("--- Subject Score Analyzer ---")

# Ask for 4 subject scores
math = float(input("Math: "))
english = float(input("English: "))
science = float(input("Science: "))
computer = float(input("Computer: "))

# Check that scores are valid
while math < 0 or math > 100:
    print("Invalid score. Enter a score between 0 and 100.")
    math = float(input("Math: "))

while english < 0 or english > 100:
    print("Invalid score. Enter a score between 0 and 100.")
    english = float(input("English: "))

while science < 0 or science > 100:
    print("Invalid score. Enter a score between 0 and 100.")
    science = float(input("Science: "))

while computer < 0 or computer > 100:
    print("Invalid score. Enter a score between 0 and 100.")
    computer = float(input("Computer: "))

# Calculate total and average
total = math + english + science + computer
average = total / 4

# Determine pass or fail
if average >= 50:
    result = "PASS"
else:
    result = "FAIL"

# Determine letter grade
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Print the results
print()
print("Total:", total)
print("Average:", average)
print("Result:", result)
print("Letter grade:", grade)