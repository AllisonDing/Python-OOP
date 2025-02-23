print("A simple Payroll program")

# define some constants
PAY_RATE = 14.5
NUM_EMPLOYEES = 2
TAX_RATE = 0.28
REGULAR_HOURS = 40

# loop for each employee
for i in range(NUM_EMPLOYEES):
    work_hours = int(input("Enter the number of work hours for employee " + str(i+1) + ": "))

    # Calculate the gross pay
    if work_hours <= 40:
        gross_pay = work_hours * PAY_RATE
    elif work_hours <= 45:
        gross_pay = REGULAR_HOURS * PAY_RATE + (work_hours - 40) * (1.5 * PAY_RATE)
    else:
        gross_pay = REGULAR_HOURS * PAY_RATE + (45 - 40) * (1.5 * PAY_RATE) + (work_hours - 45) * (2 * PAY_RATE)

    # Calculate the tax and net pay
    income_tax = gross_pay * TAX_RATE
    net_pay = gross_pay - income_tax

    # Print the results
    print("Employee " + str(i+1) + ": ")
    print("Gross Pay is $", gross_pay, sep = "")
    print("Income Tax is $", income_tax, sep = "")
    print("Net Pay is $", net_pay, sep = "")


