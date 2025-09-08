def roundGrade(grade: int) -> int:
    if grade < 38: return grade
    else:
        nextGrade = grade + ((5 - (grade % 5)) % 5)
        if (nextGrade - grade) < 3:
            return nextGrade
        else:
            return grade

print(roundGrade(37))
