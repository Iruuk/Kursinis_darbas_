import random
import pandas as pd

class ReadInputFile:
    def __init__(self, filename):
        self._info = pd.read_csv(filename, delimiter=';')

    def read_object(self, object_name):
        valid_object = self._info[object_name].dropna().astype(str).tolist()
        return valid_object
    
class Write_into_file:
    def __init__(self, filename):
        self.filename = filename

    def write(self, text):
        with open(self.filename, 'a') as file:
            file.write(text + '\n')

class GetInfo:
    def __init__(self, input_reader):
        self._read_input_file = input_reader
        self._VALID_RACES = self._read_input_file.read_object('Race')
        self._VALID_CLASSES = self._read_input_file.read_object('Class')
        self._VALID_STATS = self._read_input_file.read_object('Abilities')

    def player_name(self):
        while True:
            name = input("Write your name: ")
            if self._is_valid_name(name):
                return name
            else:
                print("Invalid name. Please enter a valid name.")

    def _is_valid_name(self, name):
        return name.isalpha() and len(name) > 0
  
    def character_name(self):
        character = input("Write your character name: ")
        return character

    def level(self):
        while True:
            level = int(input("What level do you want to play? (1-3): "))
            if level in [1, 2, 3]:
                return level
            print("Invalid level, please try again.")

    def race(self):
        while True:
            race = input(f"What race do you want to play? ({', '.join(self._VALID_RACES)}): ").lower()
            if race in self._VALID_RACES:
                return race
            print("Invalid race, please try again.")

    def class_choice(self):
        while True:
            clas = input(f"What class do you want to play? ({', '.join(self._VALID_CLASSES)}): ").lower()
            if clas in self._VALID_CLASSES:
                return clas
            print("Invalid class, please try again.")

class CharacterStats:
    def __init__(self):
        pass

    def calculate_stats(self):
        raise NotImplementedError("Subclass must implement abstract method")

class FourDiceMethod(CharacterStats):
    def __init__(self, valid_stats):
        super().__init__()
        self._abilities = []
        self._modifiers = []
        self._valid_stats = valid_stats

    def method(self):
        dice_rolls = []
        for _ in range(4):
            stat = random.randint(1, 6)
            dice_rolls.append(stat)
        dice_rolls.sort()
        dice_rolls.pop(0)
        return sum(dice_rolls)

    def add_stats(self, ability):
        self._abilities.append(ability)
        self._modifiers.append(round((ability - 10) / 2))

    def calculate_stats(self):
        for _ in range(6):
            ability = self.method()
            self.add_stats(ability)

    def display_stats(self):
        return "Abilities and Modifiers:\n" + '\n'.join([f"{stat}: {ability} (Modifier: {modifier})" for stat, ability, modifier in zip(self._valid_stats, self._abilities, self._modifiers)])

class DefaultStatsMethod(CharacterStats):
    def __init__(self, valid_stats):
        super().__init__()
        self._stats = [15, 14, 13, 12, 10, 8]
        self._abilities = {}
        self._modifiers = {}
        self._valid_stats = valid_stats

    def insert_stats(self):
        output = "Assign the stats to the abilities:\n"
        for stat_name in self._valid_stats:
            while True:
                value = input(f"Assign a value from {self._stats} to {stat_name}: ")
                try:
                    value = int(value)
                    if value in self._stats:
                        self._stats.remove(value)
                        self._abilities[stat_name] = value
                        self._modifiers[stat_name] = round((value - 10) / 2)
                        break
                    else:
                        print("Value not in available stats. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        output += "Stats assigned successfully.\n"
        return output

    def calculate_stats(self):
        self.insert_stats()

    def display_stats(self):
        return "Assigned stats and Modifiers:\n" + '\n'.join([f"{stat}: {value} (Modifier: {self._modifiers[stat]})" for stat, value in self._abilities.items()])

class Health:
    def hit_dices(self, character_class):
        if character_class in ["wizard", "sorcerer"]:
            return 6
        elif character_class in ["bard", "cleric", "monk", "druid", "rogue", "warlock", "artificier"]:
            return 8
        elif character_class in ["fighter", "paladin", "ranger", "bloodhunter"]:
            return 10
        else:
            return 12

    def hit_points(self,character_class, lvl):
        if lvl == 1:
            health = self.hit_dices(character_class)
        elif lvl == 2:
            health = self.hit_dices(character_class) + random.randint(1, self.hit_dices(character_class))
        else:
            health = self.hit_dices(character_class)
            for _ in range(2):
                health += random.randint(1, self.hit_dices(character_class))
        return health

class Inventory:
    def __init__(self, filename):
        self._read_input_file = ReadInputFile(filename)
        self._valid_armour = self._read_input_file.read_object('Armour')
        self._valid_weapon = self._read_input_file.read_object('Weapon')
        self._inventory_items = []

    def add_to_inventory(self, item):
        self._inventory_items.append(item)

    def armour(self):
        while True:
            choice = input("Insert your armour (from available in [Players Guide ] book): ")
            if choice in self._valid_armour:
                self.add_to_inventory(choice)
                print(f"{choice} added to inventory.")
                return 
            else:
                print("Invalid armour. Please enter a valid armour.")

    def weapon(self):
        while True:
            choice = input("Insert your weapon (from available in [Players Guide] book): ")
            if choice in self._valid_weapon:
                self.add_to_inventory(choice)
                print(f"{choice} added to inventory.")
                return 
            else:
                print("Invalid weapon. Please enter a valid weapon.")

    def inventory(self):
        while True:
            print("Inventory options:")
            print("1. Add to inventory")
            print("2. Exit inventory")

            choice = input("Enter your choice: ")
            if choice == '1':
                while True:
                    item = input("Enter item: ")
                    if item.isalpha():
                        self.add_to_inventory(item)
                        print(f"{item} added to inventory.")
                        break
                    else:
                        print("Invalid item. Please enter a word.")
            elif choice == '2':
                break
            else:
                print("Invalid choice. Please enter a valid option.")

class Runner:
    def run_program(self):
        my_choice = ""
        while my_choice != 'Exit':
            my_choice = input("If you want to make character enter [Make], if you want to finish enter [Exit]: ")
            if my_choice == 'Make':
                info = GetInfo(ReadInputFile('Input.csv'))
                player_name = info.player_name()
                character_name = info.character_name()
                level = info.level()
                race = info.race()
                character_class = info.class_choice()

                writer = Write_into_file('output.txt')
                writer.write(f"Player: {player_name}")
                writer.write(f"Character name: {character_name}")
                writer.write(f"Level: {level}")
                writer.write(f"Race: {race}")
                writer.write(f"Class: {character_class}")

                choice = input("Choose method (1: Four dice method, 2: Default stats method): ")
                if choice == '1':
                    method = FourDiceMethod(info._VALID_STATS)
                elif choice == '2':
                    method = DefaultStatsMethod(info._VALID_STATS)

                method.calculate_stats()
                stats_info = method.display_stats()

                health = Health()
                hit_points = health.hit_points(character_class, level)
                writer.write(f"Hit Points: {hit_points}")

                my_inventory = Inventory('Input.csv')
                my_inventory.armour()
                my_inventory.weapon()
                my_inventory.inventory()

                writer.write("Inventory Items:")
                for item in my_inventory._inventory_items:
                    writer.write(item)
                writer.write(stats_info)
                writer.write("\n\n\n")
            elif my_choice == 'Exit':
                break
            else:
                print("Your order has been inserted incorrectly. Try one more time: ")

program=Runner()
program.run_program()
