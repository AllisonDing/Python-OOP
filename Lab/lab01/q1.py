# Print the program title
print("This program sums a sequence of product prices.")

# Get the number of product prices
num_of_prices = int(input("Enter the number of prices: "))

# A loop for getting prices one at a time
sum = 0
for i in range(num_of_prices):
    price = float(input("Enter price " + str(i+1) + ": "))
    sum += price

print("The sum is $" + "{:,.2f}".format(sum))


