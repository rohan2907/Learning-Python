## Calculate Salary, weekly working hours given in a list

work_hours = [int(x) for x in input('Enter hours per day in entire week, seperated by space: ').split()]

hourly_wages = int(input('Enter hourly wages: '))

total_hours= (sum(work_hours))

salary = total_hours * hourly_wages

print('Salary is: ',salary)

