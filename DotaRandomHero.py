import random
import os
import keyboard
import time

ALL_HEROES_POOL = "HERO.txt"
CARRY_POOL = "CARRY.txt"
MID_POOL = "MID.txt"
OFFLANE_POOL = "OFFLANE.txt"
SOFT_SUPPORT_POOL = "SOFT_SUPPORT.txt"
SUPPORT_POOL = "SUPPORT.txt"

# Main program loop
# This is really ugly rn
def parse_pool(pool_name):
    os.system('cls')
    content = []
    with open(pool_name) as f:
        content = f.read().splitlines()
    print(f"Your random {pool_name.split('.txt')[0]}:\n\n\t{random.choice(content)}\n")
    print("New Hero: Enter\nCarry: 1\nMid: 2\nOfflane: 3\nSoft Support: 4\tHard Support: 5\nAll Heroes: 6\nCustom Pool: 7")
    while True:
        user_input = keyboard.read_key()
        time.sleep(0.2)
        match user_input:
            case '1':
                parse_pool(CARRY_POOL)
            case '2':
                parse_pool(MID_POOL)
            case '3':
                parse_pool(OFFLANE_POOL)
            case '4':
                parse_pool(SOFT_SUPPORT_POOL)
            case '5':
                parse_pool(SUPPORT_POOL)
            case '6':
                parse_pool(ALL_HEROES_POOL)
            case 'enter':
                parse_pool(pool_name)
            case '7':
                time.sleep(0.2)
                os.system('cls')
                while True:
                    custom_pool = input("Enter name of custom pool file (without .txt):\n")
                    try:
                        parse_pool(custom_pool + '.txt')
                        break
                    except:
                        print(f"Failed to open {custom_pool}")
                        continue
            case _:
                continue


# Main Menu
print("Welcome to the excellent Dota 2 Random Hero Tool")
print("All Heroes: Enter\nCarry: 1\nMid: 2\nOfflane: 3\nSoft Support: 4\nHard Support: 5\nCustom Pool: 7")
user_input = keyboard.read_key()
time.sleep(0.2)
match user_input:
        case '1':
            parse_pool(CARRY_POOL)
        case '2':
            parse_pool(MID_POOL)
        case '3':
            parse_pool(OFFLANE_POOL)
        case '4':
            parse_pool(SOFT_SUPPORT_POOL)
        case '5':
            parse_pool(SUPPORT_POOL)
        case 'enter':
            parse_pool(ALL_HEROES_POOL)
        case '7':
            time.sleep(0.2)
            os.system('cls')
            while True:
                custom_pool = input("Enter name of custom pool file (without .txt):\n")
                try:
                    parse_pool(custom_pool + '.txt')
                    break
                except:
                    print(f"Failed to open {custom_pool}")
                    continue