import random

random_num = random.randint(1, 3)
print("***********************")
print("Welcome to the game")
ui = int(input("Enter 1 for scissor, 2 for rock, 3 for paper:\n"))
ci = None
if random_num == 1:
    ci = "Scissor"
elif random_num == 2:
    ci = "Rock"
else:
    ci = "Paper"

if ui == 1 and ci == "Scissor":
    print(f"The match is Draw, User:{ui} Computer:{ci}")
elif ui == 1 and "Rock":
    print(f"Computer won, User:{ui} Computer:{ci}")
elif ui == 1 and ci == "Paper":
    print(f"User won, User:{ui} Computer:{ci}")

elif ui == 2 and ci == "Scissor":
    print(f"User won, User:{ui} Computer:{ci}")
elif ui == 2 and ci == "Rock":
    print(f"The match is Draw, User:{ui} Computer:{ci}")
elif ui == 2 and "Paper":
    print(f"Computer won, User:{ui} Computer:{ci}")

elif ui == 3 and ci == "Scissor":
    print(f"Computer won, User:{ui} Computer:{ci}")
elif ui == 3 and ci == "Rock":
    print(f"Computer Won, User:{ui} Computer:{ci}")
elif ui == 3 and "Paper":
    print(f"The match is Draw, User:{ui} Computer:{ci}")

print("***********************")