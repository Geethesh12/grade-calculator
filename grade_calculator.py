# Task 3: Conditional Statements & Logical Flow
# Python Developer Internship

# Taking input from the user
marks = input("Enter your marks (0 - 100): ")

# Check if the input is a number
if marks.isdigit():
    marks = int(marks)

    # Validate marks range
    if marks < 0 or marks > 100:
        print("Invalid marks! Please enter marks between 0 and 100.")

    else:
        # Grade calculation using if-elif-else
        if marks >= 90:
            grade = "A+"
            message = "Excellent performance!"

        elif marks >= 80 and marks < 90:
            grade = "A"
            message = "Very good job!"

        elif marks >= 70 and marks < 80:
            grade = "B"
            message = "Good performance."

        elif marks >= 60 and marks < 70:
            grade = "C"
            message = "You can do better."

        elif marks >= 50:
            grade = "D"
            message = "Needs improvement."

        else:
            grade = "F"
            message = "You have failed. Work harder."

        # Nested condition (Business rule example)
        if grade == "A+" or grade == "A":
            print("You are eligible for scholarship consideration.")

        # Final output
        print(f"Grade: {grade}")
        print(message)

else:
    print("Invalid input! Please enter only numeric values.")