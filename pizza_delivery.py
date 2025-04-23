# This program build an automatic pizza order system
# Welcome the user to the Pizza deliveries system
print("Welcome to the Pizza Deliveries System!")
# Ask the user what size of pizza they want (small, medium, or large)
size = input("What size pizza do you want (small(S), medium(M), or large(L))? ")
# Ask if the user wants a pepperoni on their pizza
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# Ask the user if they want extra cheese on their pizza
extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ")

small_size_price = 15
medium_size_price = 25
large_size_price = 35
pepperoni_price = 3

total_price = 0  # Total price
if size.upper() == "S":
    total_price += small_size_price
    if pepperoni.upper() == "Y":
        total_price += pepperoni_price
elif size.upper() == "M":
    total_price += medium_size_price
    if pepperoni.upper() == "Y":
        total_price += pepperoni_price
elif size.upper() == "L":
    total_price += large_size_price
    if pepperoni.upper() == "Y":
        total_price += pepperoni_price
else:
    print("Invalid size. Please choose S, M, or L.")

if extra_cheese.upper() == "Y":
    total_price += 1
print("________________________________________________________________")
print(f"\nYour total cost is:, ${ total_price}")
print("________________________________________________________________")
