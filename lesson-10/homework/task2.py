import csv
import os

my_file="grades.csv"

if not os.path.exists(my_file):
    with open(my_file, 'w', newline='') as f:
        writer=csv.writer(f)
        writer.writerow(['Name','Subject', 'Grade'])
        writer.writerow(['Alice','Math', '85'])
        writer.writerow(['Bob','Science', '78'])
        writer.writerow(['Carol','Maths', '92'])
        writer.writerow(['Dave','History', '74']) 

grades=[]
with open(my_file,'r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        row["Grade"]=int(row["Grade"])
        grades.append(row)

subjects_grades={}
for row in grades:
    subject=row["Subject"]
    grade=row["Grade"]
    if subject not in subjects_grades:
        subjects_grades[subject]=[]
    subjects_grades[subject].append(grade)

avarage_grades={}
for subject,grades in subjects_grades.items():
    avarage_grades[subject]=sum(grades)/len(grades)

with open('avarage_grades.csv', 'w') as f:
    writer=csv.writer(f)
    writer.writerow(["Subject","Avarage grades"])
    for subject,avarage_grade in avarage_grades.items():
        writer.writerow([subject, round(avarage_grade,1)])
