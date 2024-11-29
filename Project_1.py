# Data tabulky
data = {
    "user", "password",
    "bob", "123",
    "ann", "pass123",
    "mike", "password123",
    "liz", "pass123",
}

'''
# Nastavení oddělovače
ODDELOVAC = "+------+-------------+"

# Výpis tabulky
print(ODDELOVAC)
for index, (user, password) in enumerate(data):
    if index == 0:  # Hlavička tabulky
        print(f"| {user: ^4} | {password: ^11} |")
        print(ODDELOVAC)  # Oddělovač pod hlavičkou
    else:
        print(f"| {user: <4} | {password: <11} |")
print(ODDELOVAC)
'''

# Oddělovač
line = "-" * 35

# Texty k analýze
TEXTS = [
    '''
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley.
    ''',
    '''
    At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.
    ''',
    '''
    The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.
    '''
]

# Přihlašovací údaje
username = input('username: ')
password = input('password: ')

# Ověření uživatele
if (username, password) in data:
    print(line)
    print(f"Welcome to the app, {username}!")
    print("We have 3 texts to be analyzed.")
    print(line)
    
    # Výběr textu
    print("Enter a number between 1 and 3 to select a text:")
    text_choice = input()
    
    if text_choice.isnumeric():
        text_choice = int(text_choice)
        if 1 <= text_choice <= 3:
            print(line)
            print(f"Text {text_choice} selected:")
            selected_text = TEXTS[text_choice - 1]
            print(selected_text)
            print(line)
            
            # Analýza textu
            words = [word.strip(".,") for word in selected_text.split()]
            word_count = len(words)
            titlecase_count = sum(1 for word in words if word.istitle())
            uppercase_count = sum(1 for word in words if word.isupper() and word.isalpha())
            lowercase_count = sum(1 for word in words if word.islower())
            numeric_strings = [int(word) for word in words if word.isnumeric()]
            numeric_count = len(numeric_strings)
            numeric_sum = sum(numeric_strings)
            
            # Výpis statistik
            print(f"There are {word_count} words in the selected text.")
            print(f"There are {titlecase_count} titlecase words.")
            print(f"There are {uppercase_count} uppercase words.")
            print(f"There are {lowercase_count} lowercase words.")
            print(f"There are {numeric_count} numeric strings.")
            print(f"The sum of all the numbers {numeric_sum}")
            print(line)
            
            # Tabulka výskytů slov podle délky
            word_lengths = {}
            for word in words:
                length = len(word)
                word_lengths[length] = word_lengths.get(length, 0) + 1
            
            print("LEN|  OCCURENCES  |NR.")
            print(line)
            for length, count in sorted(word_lengths.items()):
                stars = "*" * count
                print(f"{length:>3}|{stars:<13}|{count}")
        else:
            print("Invalid number. Terminating the program.")
    else:
        print("Invalid input. You must enter a number. Terminating the program.")
else:
    print("Unregistered user, terminating the program..")

print(line)
