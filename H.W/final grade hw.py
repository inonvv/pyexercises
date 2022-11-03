def final_grade(exam,hw):
    grade=0
    if exam>=50 and not hw>exam+25:
        grade=round((exam*0.75)+(hw*0.25))
    else:
        grade=exam
    return grade
print(final_grade(90,79.4))

