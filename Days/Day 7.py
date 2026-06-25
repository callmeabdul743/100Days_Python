import random

stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

word_list= ["apple","banana","computer"]

random_word = random.choice(word_list)

place_holder = ""

for random in random_word:
    place_holder += "_"

print(place_holder)
print(random_word)

display = ""
start= 0

while place_holder != "_":
    user_guess = input("Guess the letter: ").lower()
    for letter in random_word:
        if letter == user_guess:
            display += letter
        else:
            display += "_"

    if letter == user_guess:
        print(stages[start])
    else:
        # print(stages[start])
        start -= 1

print(display)