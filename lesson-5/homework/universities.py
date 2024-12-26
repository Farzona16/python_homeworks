universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stats():
    university=[]
    students=[]
    tuition=[]
    for i in range(len(universities)):
        if universities[i][0] not in university:
            university.append(universities[i][0])
            students.append(universities[i][1])
            tuition.append(universities[i][2])
            total_student=sum(students)
            total_tuition=sum(tuition)
    students.sort()
    tuition.sort()
    for k in range(len(students)):
        student_mean=total_student/len(students)
        tuition_mean=total_tuition/len(tuition)
    if len(students)%2==1:
       student_median=students[int(len(students)/2)] 
    else: 
        student_median=(students[int(len(students)/2)]+students[int(len(students)/2)-1])/2
    if len(tuition)%2==1:
       tuition_median=tuition[int(len(tuition)/2)] 
    else: 
        tuition_mean=(tuition[int(len(tuition)/2)-1]+tuition[int(len(tuition)/2)])/2
    print(f"Total students: {total_student}")
    print(f"Total tuition: {total_tuition}")
    print(f"Student mean: {student_mean:0.2f}")
    print(f"Student median: {student_median:0.2f}")
    print(f"Tuition mean: {tuition_mean:0.2f}")
    print(f"Tuition median: {tuition_median:0.2f}")
enrollment_stats()