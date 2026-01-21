# -------------------------------
# Grade Calculator Program
# -------------------------------

def calculate_grade(marks):
    """
    This function determines the grade based on marks.
    """

    # Business rule: valid marks range
    if marks < 0 or marks > 100:
        return "❌ Invalid marks! Please enter marks between 0 and 100."

    # Nested conditions (real business rules)
    if marks >= 90:
        if marks >= 95:
            return "Grade A+ 🏆 (Outstanding Performance)"
        else:
            return "Grade A ⭐ (Excellent Performance)"

    elif marks >= 75 and marks < 90:
        return "Grade B 👍 (Very Good)"

    elif marks >= 60 and marks < 75:
        return "Grade C 🙂 (Good)"

    elif marks >= 40 and marks < 60:
        return "Grade D ⚠️ (Pass)"

    else:
        return "Grade F ❌ (Fail)"


# -------------------------------
# Main Program
# -------------------------------

try:
    marks = float(input("Enter your marks (0–100): "))
    result = calculate_grade(marks)
    print("\nResult:", result)

except ValueError:
    print("❌ Invalid input! Please enter numeric marks only.")