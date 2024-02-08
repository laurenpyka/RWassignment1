import csv

employees = open('employee_data.csv', 'r')

csv_file = csv.reader(employees)
next(csv_file)

HE_people = []
IE_people = []
emp_40 = []
emp_30 = []
emp_20 = []

for line in csv_file:
    name = line[1]
    age = int(line[2])
    hours_worked = int(line[4])
    productivity = int(line[5])
    efficiency = productivity / hours_worked

    if efficiency > 2:
        HE_people.append(name)
    if efficiency < 1:
        IE_people.append(name)
   
    if age >= 40:
        emp_40.append(name)
    elif age >= 30:
        emp_30.append(name)
    else:
        emp_20.append(name)

print("\nHighly Efficient Individuals:")
for i in HE_people:
    print(i)

print("\nLow Efficiency Individuals:")
for i in IE_people:
    print(i)

print("\nEmployees in their 40s")
for i in emp_40:
    print(i)
print("\nTotal number of employees in their 40s: ", len(emp_40))
print()

print("\nEmployees in their 30s")
for i in emp_30:
    print(i)
print("\nTotal number of employees in their 30s: ", len(emp_30))
print()

print("\nEmployees in their 20s")
for i in emp_20:
    print(i)
print("\nTotal number of employees in their 20s: ", len(emp_20))
print()