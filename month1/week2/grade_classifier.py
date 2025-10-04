def grade_classifier(score: int) -> str:
    """Return a letter grade for 0-100, or error message if out of range."""
    if score >= 80 and score <= 100:
        return "A"
    elif score >= 60 and score < 80:
        return "B"
    elif score >= 40 and score < 60:
        return "C"
    elif score >= 20 and score < 40:
        return "D"
    elif score >= 0 and score < 20:
        return "F"
    else:
        return "Invalid number (out of range)"


# --- GATE starts here ---
if __name__ == "__main__":
    # This part only runs if you execute:  python grade_classifier.py
    num_num = int(input("Enter a number 0-100: "))
    print(grade_classifier(num_num))
