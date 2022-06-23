#Practice program 2 for pr4

salary = float(input("Enter the employee salary: "))

if (salary<1500):
    hra = salary * 10/100
    da = salary * 90/100

elif(salary>=1500):
    hra=500
    da= salary * 90/100

gSalary=salary+hra+da

print("\nHRA of employee salary is: Rs. ",hra) 
print("DA of employee salary is: Rs. ",da)
print("Gross Salary of an employee is: Rs. ",gSalary)