print("The CD Calculator")

amount = float(input("Enter the initial deposit amount: "))
annual_percentage_yield = float(input("Enter annual percentage yield: "))
number_of_months = int(input("Enter maturity period (number of months): "))

print("Month CD")
CD_worth = 0
for i in range(0, number_of_months):
    CD_worth = amount * (1 + annual_percentage_yield/1200)**(i+1)
    CD_worth = "{:,.2f}".format(CD_worth)
    print(str(i+1), " $", CD_worth, sep = "")