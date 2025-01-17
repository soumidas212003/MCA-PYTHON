#A company decides to give 5% bonus to male workers and 10% bonus to female workers on salary. If the salary is lessthan 10000, employee will get extra 2% bonus on salary. Calculate the salary and bonus of employees.
salary=int(input("Enter the salary: "))
gender=input("Enter your gender either M or F: ")
if(salary>10000):
    if(gender=='M'):
        bonus=(salary*5)/100
        salary=salary+bonus
        print(salary)
    else:
        bonus=(salary*10)/100
        salary=salary+bonus
        print(salary)
else:
    if(gender=='M'):
        bonus=(salary*7)/100
        salary=salary+bonus
        print(salary)
    else:
        bonus=(salary*12)/100
        salary=salary+bonus
        print(salary)