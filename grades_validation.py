def validate_marks(marks):
    if marks < 0 or marks > 100:
        return False
    return True


def calculate_category(avg):

    if avg >= 80:
        return "A"

    elif avg >= 70:
        return "B"

    elif avg >= 60:
        return "C"

    elif avg >= 50:
        return "D"

    else:
        return "F"

