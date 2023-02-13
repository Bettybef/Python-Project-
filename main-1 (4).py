# I made a calculation to get a net_pay for 10 employees and put that in a table.
from tabulate import tabulate

table = [['Employee Name','Hours Worked','Pay Rate','Regular Pay','OT Pay','Gross Pay','Fed Tax','state Tax','FICA',
'Net Pay']]
i=1;
while i < 11:
    e_name = input(f"\nEnter Employee_name:")
    pay_rate = float(input("Enter Pay Rate:$"))
    hours = float(input("Enter Hours: "))
    overtime = 0
 # Regualr pay Calculation
    regular_pay = hours * pay_rate
# Gross pay and overtime calculation
    if hours > 40:
        overtime =(hours - 40)*(1.5 * pay_rate)
        gross_pay = regular_pay + overtime
    else:
        gross_pay= regular_pay
 # Tax calculation
    fed_tax = gross_pay * 0.1
    state_tax = gross_pay * 0.06
    fica = gross_pay * 0.03
# Net pay calcualtion
    net_pay = gross_pay -(fed_tax + state_tax + fica)
    table.append([e_name,hours, pay_rate,regular_pay,overtime,gross_pay,fed_tax,state_tax,fica,net_pay])
    i= i+1
print(tabulate(table,headers='firstrow',tablefmt='fancy_grid'))
