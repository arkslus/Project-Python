student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

for student, score in student_scores.items():
    if score >= 91:
        print(f'{student} received an outstanding grade.')
    elif score >= 81:
        print(f'{student} Exceeds Expectations.')
    elif score >= 71:
        print(f'{student} received an Acceptable grade.')
    elif score <= 70:
        print(f'{student} failed the course.')
