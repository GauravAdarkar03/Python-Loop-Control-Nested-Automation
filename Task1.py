school_data = [
    ["Alice", 85, 92, 78],      # Class A: [name, math, science, english]
    ["Bob", 72, 68, 81],
    ["Charlie", 95, 88, 91],
    ["Diana", 63, 59, 67],
    ["Eve", 88, 91, 85]
]

print("----- Task 1: Grade Analysis -----")

for student in school_data:
    name = student[0]
    total = 0
    count = 0

    for score in student[1:]:
        total += score
        count +=1

    average = total/count
    if average < 70:
        continue

    average = total/count

print(f"{name}: Average = {average:.2f} - PASS")