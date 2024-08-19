import time
import os
import random

# Karakter özellikleri
attack = 0
health = 0
money = 0
character_selected = False

def select_the_character():
    global attack, health, money, character_selected

    if not character_selected:
        print("""
        - Phoenix (High Attack, Normal Health, Normal Defense)
        - Notr (Normal Attack, High Health, Normal Defense)
        - Viking (Normal Attack, Normal Health, High Defense)
        """)
        select_char = input("Select The Character (Please Enter Char Name): ").lower()
        main_char = select_char

        if select_char == "phoenix":
            print("Okey Phoenix, Welcome To the World!!")
            attack = 200
            health = 100
            money = 500

        elif select_char == "notr":
            print("Okey Notr, Welcome To the World!!")
            attack = 100
            health = 200
            money = 500

        elif select_char == "viking":
            print("Okey Viking, Welcome To the World!!")
            attack = 100
            health = 100
            money = 500

        else:
            print("Invalid character selected. Please restart the game and select a valid character.")
            return None

        character_selected = True
        save_game()
        return main_char
    else:
        print("Character already selected. Loading previous game state.")
        return load_character()

def select_the_history(main_char):
    time.sleep(2)
    os.system("cls")
    print("All Rights Captain, Select Your History")

    print("""
    1- Forest Guardian
    2- Farmer King
    3- Shadow Warrior
    """)

    select_history = input("Select The History (Please Enter Number): ")

    if select_history == "1":
        print(f"{main_char}, this is your history: Forest Guardian")

    elif select_history == "2":
        print(f"{main_char}, this is your history: Farmer King")

    elif select_history == "3":
        print(f"{main_char}, this is your history: Shadow Warrior")

    else:
        print("Invalid selection. Please restart the game and select a valid history.")
        return None

    village_screen(main_char)

def enemy1(main_char):
    global health, money

    print("Enemy is Barbarians")
    enemy1_attack = 70
    enemy1_health = 100

    print("You don't have an escape!")
    time.sleep(2)
    print("1- Give Money \n2- Fight")

    enemy_choose = input("Please enter your choice (1 or 2): ")

    if enemy_choose == "1":
        random_money = random.randint(1, 70)
        print(f"Your Money: {money}")
        money -= random_money
        print(f"OMG! You gave {random_money} money to the Barbarians.")
        print(f"Your New Money: {money}")
        print("Oh Noo Escape Captainn")
        village_screen(main_char)

    elif enemy_choose == "2":
        print("You chose to fight the Barbarians! Fight starts now.")
        time.sleep(1)

        while health > 0 and enemy1_health > 0:
            player_damage = random.randint(10, attack)
            enemy_damage = random.randint(10, enemy1_attack)

            enemy1_health -= player_damage
            health -= enemy_damage

            print(f"\n{main_char} attacks! Deals {player_damage} damage.")
            print(f"Barbarian attacks! Deals {enemy_damage} damage.")
            print(f"Your Health: {health} | Barbarian's Health: {enemy1_health}\n")

            time.sleep(1)

        if enemy1_health <= 0:
            print("You have defeated the Barbarian!")
            reward_money = random.randint(50, 150)
            money += reward_money
            print(f"You earned {reward_money} money! Total Money: {money}")
        else:
            print("You were defeated by the Barbarian.")
            penalty_money = random.randint(50, 100)
            money -= penalty_money
            print(f"You lost {penalty_money} money. Remaining Money: {money}")

    else:
        print("Invalid choice. You missed your opportunity!")

    health, money = check_game_over(health, money)
    return health, money

def enemy2(main_char):
    global health, money

    print("Enemy is Zombies")
    enemy2_attack = 50
    enemy2_health = 50

    print("OMG! This is a zombie")
    time.sleep(2)

    print("1- Escape \n2- Fight (easy enemy)")

    enemy_choose = input("Please enter your choice 1 or 2: ")

    if enemy_choose == "1":
        print("YOU RAN!")
        time.sleep(2)
        village_screen(main_char)
        print("You escaped the zombies! All right captain")

    elif enemy_choose == "2":
        print("You chose to fight the Zombies! Fight starts now.")
        time.sleep(1)

        while health > 0 and enemy2_health > 0:
            player_damage = random.randint(10, attack)
            enemy_damage = random.randint(10, enemy2_attack)

            enemy2_health -= player_damage
            health -= enemy_damage

            print(f"\n{main_char} attacks! Deals {player_damage} damage.")
            print(f"Zombie attacks! Deals {enemy_damage} damage.")
            print(f"Your Health: {health} | Zombie's Health: {enemy2_health}\n")

            time.sleep(1)

        if enemy2_health <= 0:
            print("You have defeated the Zombie!")
            reward_money = random.randint(50, 150)
            money += reward_money
            print(f"You earned {reward_money} money! Total Money: {money}")
        else:
            print("You were defeated by the Zombie.")
            penalty_money = random.randint(50, 100)
            money -= penalty_money
            print(f"You lost {penalty_money} money. Remaining Money: {money}")

    else:
        print("Invalid choice. You missed your opportunity!")

    health, money = check_game_over(health, money)
    return health, money

def mission(main_char):
    print(f"{main_char}, Yeahh captain are you ready, new mission is coming!!")

    missions = ["find_loss_item", "save_the_village", "defense_lookout_castle", "find_antidote", "theft_secret_file"]

    random_mission = random.choice(missions)

    print(f"{main_char}, You have a mission, this is new mission {random_mission}")

    if random_mission == "find_loss_item":
        print("Mission Description: An old woman living in the city lost her valuable necklace inherited from her grandmother. The necklace is lost somewhere deep in the forest. Your mission is to go into the forest and find the necklace and bring it back to the woman.")
        time.sleep(2)
        print("You venture into the forest, searching for the necklace...")
        time.sleep(2)
        print("While searching, you encounter enemies!")
        enemy1(main_char)
        print("You found the necklace in a hidden chest. Returning it to the old woman.")
        reward_money = random.randint(50, 150)
        money += reward_money
        print(f"You earned {reward_money} money! Total Money: {money}")

    elif random_mission == "save_the_village":
        print("Mission Description: An evil gang of bandits have kidnapped several innocent villagers from the village. The villagers are being held in a nearby cave. Your mission is to save these villagers and bring them back to the village safely.")
        time.sleep(2)
        print("You head to the cave where the villagers are held...")
        time.sleep(2)
        print("Inside the cave, you encounter enemies!")
        enemy2(main_char)
        print("You have rescued the villagers and brought them back to the village.")
        reward_money = random.randint(50, 150)
        money += reward_money
        print(f"You earned {reward_money} money! Total Money: {money}")

    elif random_mission == "defense_lookout_castle":
        print("Mission Description: Enemy armies are about to attack the watchtower. Your mission is to defend the tower and prevent the enemies from taking it over. If the tower falls, the entire village may be in danger.")
        time.sleep(2)
        print("You prepare for the defense of the watchtower...")
        time.sleep(2)
        print("The enemy armies arrive!")
        enemy1(main_char)
        print("The tower has been defended successfully.")
        reward_money = random.randint(50, 150)
        money += reward_money
        print(f"You earned {reward_money} money! Total Money: {money}")

    elif random_mission == "find_antidote":
        print("Quest Description: The water supply in the town has been poisoned and the townspeople are slowly falling ill. According to legend, the only antidote to this poison is obtained from a rare plant that grows in a dangerous swamp. Your mission is to find this plant and prepare the antidote.")
        time.sleep(2)
        print("You venture into the dangerous swamp...")
        time.sleep(2)
        print("While searching, you encounter enemies!")
        enemy1(main_char)
        print("You find the rare plant and return to prepare the antidote.")
        reward_money = random.randint(50, 150)
        money += reward_money
        print(f"You earned {reward_money} money! Total Money: {money}")

    elif random_mission == "theft_secret_file":
        print("Mission Description: An important secret file has been stolen from the king's archives. The file contains sensitive information that must not fall into enemy hands. Your mission is to retrieve the file from the thieves and return it to the king.")
        time.sleep(2)
        print("You track the thieves to their hideout...")
        time.sleep(2)
        print("Inside the hideout, you encounter enemies!")
        enemy2(main_char)
        print("You recover the secret file and return it to the king.")
        reward_money = random.randint(50, 150)
        money += reward_money
        print(f"You earned {reward_money} money! Total Money: {money}")

    else:
        print("Unknown mission. Please restart the game.")

def village_screen(main_char):
    global health, money

    print(f"\nWelcome to the village, {main_char}! Your current status:")
    print(f"Health: {health}")
    print(f"Money: {money}")
    print("\nWhat would you like to do?")
    print("1- Visit the shop")
    print("2- Start a new mission")
    print("3- Exit")

    choice = input("Please enter your choice (1, 2, or 3): ")

    if choice == "1":
        print("You visit the shop and purchase some items.")
        time.sleep(2)
        village_screen(main_char)

    elif choice == "2":
        mission(main_char)

    elif choice == "3":
        print("Thanks for playing! See you next time.")
        exit()

    else:
        print("Invalid choice. Please try again.")
        village_screen(main_char)

def save_game():
    global attack, health, money
    with open("save_game.txt", "w") as file:
        file.write(f"{attack},{health},{money}\n")
        file.write("Character selected.")

def load_character():
    global attack, health, money, character_selected
    if os.path.exists("save_game.txt"):
        with open("save_game.txt", "r") as file:
            data = file.readline().strip().split(',')
            attack, health, money = map(int, data)
            character_selected = True
            return "Loaded character"
    else:
        return "No saved game found."

def check_game_over(health, money):
    if health <= 0:
        print("Game Over! You have been defeated.")
        exit()
    if money < 0:
        print("You have run out of money. Game Over!")
        exit()
    return health, money

if __name__ == "__main__":
    main_char = select_the_character()
    if main_char:
        select_the_history(main_char)
