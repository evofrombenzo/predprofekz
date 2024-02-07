class Students:
    id = 0
    fio = ""
    id_project = 0
    clas = ""
    score = 0

f = open("students.csv")
students = []
j = 0
skip = f.readline()

for i in f:
    s = i.split(',')
    if int(s[3][:-1]) == 10:
        students.append(Students())
        students[j].fio = s[1]
        students[j].score = int(s[4])
        j += 1

for i in range(len(students)):
    j = 1
    t = students[i]
    while j > 0 and students[j-1].score > t.score:
        students[j] = students[j-1]
        j -= 1
    students[j] = t

print("10 класс:")
print(f'1 место: {students[0].fio[0]}.{students[0].fio.split()[0]}')
print(f'1 место: {students[1].fio[0]}.{students[1].fio.split()[0]}')
print(f'1 место: {students[2].fio[0]}.{students[2].fio.split()[0]}')