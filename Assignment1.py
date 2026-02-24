
employees = [
    {"id": 101, "name": "Amit Sharma","department": "IT","skills":["Python","SQL","AWS"]},
    {"id": 102, "name": "Neha Verma","department": "HR","skills":["Communication","Recruitment"]},
    {"id": 103, "name": "Ravi Kumar","department": "IT","skills":["Python","Docker"]},
    {"id": 104, "name": "Sneha Iyer","department": "Finance","skills":["Excel","Accounting"]}
]


#1 Print all employee name in uppercase.
for emp in employees:
    name = emp["name"]
    uppcase_name = ""
    for ch in name:
        if 'a' <= ch <= 'z':
            uppcase_name += chr(ord(ch)-32)
        else:
            uppcase_name += ch
    print(uppcase_name)             

#2 Find all employees who belong to the IT department.
for emp in employees:
    if emp["department"] == "IT":
        print(emp["name"])

#3 Create a set of all unique skills across employees.
uni_set = set()
for emp in employees:
    for skill in emp["skills"]:
            uni_set.add(skill)
print(uni_set)

#4 Count how many employees know Python.
count = 0
for emp in employees:
    for ski in emp["skills"]:
        if ski == "Python":
            count += 1
print(f"Employees Knowing Py:{count}")        
    
#5 Create a dictionary showing number of employees per department.
department_count = {}
for emp in employees:
    dept = emp["department"]
    if dept in department_count:
        department_count[dept] += 1
    else:
        department_count[dept] = 1
print(department_count)            

#6 Sort employees by name alphabetically.
for i in range(4):
    for j in range(0,4-i-1):
        if employees[j]["name"] > employees[j+1]["name"]:
            temp = employees[j]
            employees[j] = employees[j+1]
            employees[j+1] = temp    
for emp in employees:
    print(emp["name"])     
