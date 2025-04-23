# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# Write your code below this line 👇

print("Welcome to the tip calculator!")  # Welcome message

# Ask the user to enter a bill amount
bill = float(input("What is the bill amount: $"))

# Ask the user to enter a tip amount
tip = float(input("Please enter the tip amount, $10, $12, 15, or more: $"))

# Ask the user to enter the number of people splitting the bill
number_of_people = int(input("How many people are splitting the bill: "))

# divide the tip amount by 100 to get the tip percentage
tip_percentage = tip / 100

# calculate the tip plus bill amount
bill_plus_tip = bill * tip_percentage

# calculate the total bill per person
total_bill = bill_plus_tip + bill

# divide the total bill among five people
amount_per_person = total_bill / number_of_people

# round amount per person to 2 decimal places
final_amount = round(amount_per_person, 2)

# print how much each person should pay
print(f"\nEach person should pay: ${final_amount: .2f}")
