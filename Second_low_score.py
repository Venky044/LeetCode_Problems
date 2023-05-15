"""
Given the names and grades for each student in a class of  students, 
store them in a nested list and print the name(s) of any student(s) 
having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.

I/P) 
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.20], ['Akriti', 41], ['Harsh', 39]]

O/P)
Berry
Harry
"""

records = []
    
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name,score])

records_2 = sorted([[j,i] for i,j in records])


first_low_score = records_2[0][0]
i = 0
for score,name in records_2:
    if score == first_low_score:
        i += 1

secord_low_score = records_2[i][0]

for score, name in records_2:
    if score == secord_low_score:
        print(name)