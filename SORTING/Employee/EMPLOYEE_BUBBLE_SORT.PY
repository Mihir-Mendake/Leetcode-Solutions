# Read the data from the file “employee.txt” and sort on salary usingbubble / insertion
# sort. Write the sorted data to another file “newemp.txt”

# Expected Input (employee.txt):
# John Manager 50000
# Alice Engineer 40000
# Bob Clerk 30000
# Eve Analyst 45000

# Expected Output (newemp.txt):
# ~Vaibhav Bandgar
# Bob Clerk 30000
# Alice Engineer 40000
# Eve Analyst 45000
# John Manager 50000


with open("employee.txt","r") as f:
    employees = [line.strip().split() for line in f]

for emp in employees:
    emp[2] = int(emp[2])

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j][2] > arr[j+1][2]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

with open("newemp.txt","w") as f:
    for emp in employees:
        f.write(f"{emp[0]} {emp[1]} {emp[2]}\n")
    