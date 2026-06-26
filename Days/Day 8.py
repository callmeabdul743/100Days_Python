# def life_in_weeks(age):
#     weeks_left = (90 - age) * 52
#     print(f"You have {weeks_left} weeks left.")

# life_in_weeks(56)

def calculate_love_score(name1, name2):
    name = (name1 + name2).lower()
    true_find = name.count("t")+ name.count("r")+ name.count("u")+ name.count("e")
    love_find = name.count("l")+ name.count("o")+ name.count("v")+ name.count("e")
    print(f"{true_find}{love_find}")

calculate_love_score("Kanye West", "Kim Kardashian")
