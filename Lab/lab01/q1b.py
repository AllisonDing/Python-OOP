# Print the program title
print("This program sums a sequence of product prices.")

# Get the number of product prices
price_list = input("Enter a list of prices: ")
price_list = price_list.split(" ") # coverts a string into a list (array)
print(price_list)

sum = 0
for i in range(1, len(price_list)):
    price = float(price_list[i])
    sum += price

print("The sum is $" + "{:,.2f}".format(sum))


