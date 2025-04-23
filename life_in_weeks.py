# Life in weeks program until 90 years old
def life_in_weeks():
    age = int(input("Enter your age: "))
    weeks_in_year = 52
    weeks_left = (90 - age) * weeks_in_year
    print(f"You have {weeks_left} weeks left in your 90-year life.")

# call the function 
life_in_weeks()