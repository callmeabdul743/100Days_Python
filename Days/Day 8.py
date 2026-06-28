# def life_in_weeks(age):
#     weeks_left = (90 - age) * 52
#     print(f"You have {weeks_left} weeks left.")

# life_in_weeks(56)

# def calculate_love_score(name1, name2):
#     name = (name1 + name2).lower()
#     true_find = name.count("t")+ name.count("r")+ name.count("u")+ name.count("e")
#     love_find = name.count("l")+ name.count("o")+ name.count("v")+ name.count("e")
#     print(f"{true_find}{love_find}")

# calculate_love_score("Kanye West", "Kim Kardashian")


print(r"""
  ____                               ____ _       _               
 / ___|__ _  ___  ___  __ _ _ __    / ___(_)_ __ | |__   ___ _ __ 
| |   / _` |/ _ \/ __|/ _` | '__|  | |   | | '_ \| '_ \ / _ \ '__|
| |__| (_| |  __/\__ \ (_| | |     | |___| | |_) | | | |  __/ |   
 \____\__,_|\___||___/\__,_|_|      \____|_| .__/|_| |_|\___|_|   
                                           |_|                    
""")
alphabet = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z"
]
print("-"*70)
direction = input("Type 'e' for the encryption, and 'd' for the decryption: \n").lower()
msg = input("Enter you message: \n").lower()
shift = int(input("The amount of number you want to shift: \n"))
msg_list = list(msg)
print("-"*70)


def encrypt(shift, msg_list):   
    print(r"""
=========================================
          ENCRYPT CIPHER
=========================================
    """)

    encoded_text = ""

    for character in msg_list:
        if character == " ":
            encoded_text += " "
        else:
            index_new = (alphabet.index(character) + shift) % 26
            encoded_text += alphabet[index_new]

    print(f"The Encoded message is:\n{encoded_text}")

def decrypt(shift, msg_list):
    print(r"""
=========================================
          DECRYPT CIPHER
=========================================
    """)
        
    decrypted_text = ""

    for character in msg_list:
        if character == " ":
            decrypted_text += " "
        else:
            index_new = (alphabet.index(character) - shift) % 26
            decrypted_text += alphabet[index_new]

    print(f"The Decrypted message is:\n{decrypted_text}")

if direction == 'e':
  encrypt(shift , msg_list )
else:
  decrypt(shift , msg_list )


