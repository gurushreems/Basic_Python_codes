n = int(input("number of student ::"))
student_marks = {}
for i in range(n):
    name = input("name::")
    maths = int(input("marks in maths :: "))
    chem = int(input("marks in chemistry :: "))
    phys = int(input("marks in physics :: "))
    scores = [maths, chem, phys]
    student_marks[name] = scores
print(student_marks)
query_name = input("name of the student")
output = list(student_marks[query_name])
per = sum(output)/len(output)
print(round(per, 2))
