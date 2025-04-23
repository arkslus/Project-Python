# love score calculator 
def calculate_love_score(name1, name2):
    combined_name = name1.lower() + name2.lower()
    lower_name = combined_name.lower()

    t = lower_name.count('t')
    r = lower_name.count('r')
    u = lower_name.count('u')
    e = lower_name.count('e')
    first_digit = int(str(t) + str(r) + str(u) + str(e))
  
    l = lower_name.count('l')
    o = lower_name.count('o')
    v = lower_name.count('v')
    e = lower_name.count('e')
   
    second_digit = int(str(l) + str(o) + str(v) + str(e))

    score = first_digit + second_digit
    print(f"Your love score is {score}.")

    if score < 10 or score > 90:
        print("Your love score is very special!")
    elif score >= 40 and score <= 50:
        print("Your love score is sweet!")
    elif score >= 60 and score <= 70:
        print("Your love score is moderate!")
    else:
        print("Your love score is not that great!")

calculate_love_score("true", "love")