print("A simple Hotel Checkout Program")

ONE_PERSON_RATE = 155
TWO_PERSON_RATE = 160
THREE_PERSON_RATE = 165
TAX_RATE = 0.12

number_of_nights = int(input("Enter the number of nights: "))
number_of_people = int(input("Enter the number of people in the room: "))
meal_charges = float(input("Enter the meal charges from the restaurant: "))

bill = 0
if number_of_people == 1:
    bill = (ONE_PERSON_RATE * number_of_nights + meal_charges) * (1 + TAX_RATE)
elif number_of_people == 2:
    bill = (TWO_PERSON_RATE * number_of_nights + meal_charges) * (1 + TAX_RATE)
elif number_of_people >= 3:
    bill = (THREE_PERSON_RATE * number_of_nights + meal_charges) * (1 + TAX_RATE)

print("The bill is $", "{:,.2f}".format(bill), sep="")
