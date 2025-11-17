def grade_score(score: int) -> str:

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Example Usage:
print(f"Score 95: {grade_score(95)}") # A
print(f"Score 80: {grade_score(80)}") # B
print(f"Score 65: {grade_score(65)}") # D
print(f"Score 45: {grade_score(45)}") # F
