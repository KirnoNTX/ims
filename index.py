#MIT License
# Copyright (c) 2023 Kirno

# -*- coding: utf-8 -*-

# - - - - - - - - - - - - - - - - - - - # IMPORT # - - - - - - - - - - - - - - - - - - - #

import os
import time

# - - - - - - - - - - - - - - - - - - # CLEAR MODULE # - - - - - - - - - - - - - - - - - - #

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# - - - - - - - - - - - - - - - - # HOME CHOICE MODULE # - - - - - - - - - - - - - - - - #

def home_choice():
    while True:
        clear()
        inventory.display_inventory()
        inventory.display_menu()

        choice = input(f"{inventory.user_name}> ").lower()

        if choice == "g":
            inventory.give()
            print(f"\n")

        elif choice == "w":
            inventory.withdraw()
            print(f"\n")

        elif choice == "e":
            inventory.export_save()
            print(f"\n")

        elif choice == "i":
            inventory.import_save()
            print(f"\n")

        elif choice == "s":
            inventory.set_name()
            print(f"\n")

        elif choice == "d":
            inventory.debug()
            print(f"\n")

        elif choice == "r":
            inventory.reset()
            print(f"\n")

        else:
            clear()
            print(f"[ERROR] Invalid action wait 2 secondes and retry please...")
            time.sleep(2)

# - - - - - - - - - - - - - - - - - - # INVENTORY CLASS # - - - - - - - - - - - - - - - - - - #

class Inventory:
    def __init__(self):
        self.inventory_file = "./logs/inv.txt"
        self.save_file = "./data/save.txt"
        self.max_items = 7
        self.items = []

# - - - - - - - - - - - - - - - - - - # DEBUG INV MODULE # - - - - - - - - - - - - - - - - - - #

    def debug(self):
        with open(self.save_file, "r", encoding="utf-8") as file:
            temp_save = [line.strip() for line in file.readlines()]

        clear()
        print(f"=== Inventory Debug Information ===")
        print(f"Inventory File: {self.inventory_file}")
        print(f"Save File: {self.save_file}")
        print(f"Items Save : {temp_save}")
        print(f"Items: {self.items}")
        print(f"===================================\n")
        print(f"Press a key to exit\n\n")
        input(f"{self.user_name}> ")

# - - - - - - - - - - - - - - - - - - # DISPLAY INV MODULE # - - - - - - - - - - - - - - - - - - #

    def display_inventory(self):
        print(f"|◇───◇────────◇───────────◇  ◇───◇────────◇───────────◇|")
        for item in self.items:
            print(f"◇◇ {item} ◇◇", end="")
        print(f"\n|◇───────────◇────────◇───◇  ◇───────────◇────────◇───◇|")

# - - - - - - - - - - - - - - - - - # DISPLAY MENU INV MODULE # - - - - - - - - - - - - - - - - - #

    def display_menu(self):
        print(f"◇────◇────────◇────────────◇◇────◇────────◇────────────◇")
        print(f"|                Welcome to your Inventory             |")
        print(f"◇────────────◇────────◇────◇◇────────────◇────────◇────◇\n")
        print(f"◇─◇─◇───────────◇   ◇─◇─◇───────────◇   ◇─◇─◇───────────◇")
        print(f"| G : Give      |   | E : Export    |   | S : Set name  |")
        print(f"◇───────────◇─◇─◇   ◇───────────◇─◇─◇   ◇───────────◇─◇─◇")
        print(f"| W : Withdraw  |   | I : Import    |")
        print(f"◇─◇─◇───────────◇   ◇─◇─◇───────────◇")
        print(f"◇───────────◇─◇─◇   ◇───────────◇─◇─◇")
        print(f"| D : Debug     |   | R : Reset     |")
        print(f"◇─◇─◇───────────◇   ◇─◇─◇───────────◇\n")

# - - - - - - - - - - - - - - - - - - # GIVE INV MODULE # - - - - - - - - - - - - - - - - - - #

    def give(self):
        clear()
        inventory.display_inventory()
        print(f"◇────◇────────◇────────────◇◇────◇────────◇────────────◇")
        print(f"|             Select an item with its name             |")
        print(f"◇────────────◇────────◇────◇◇────────────◇────────◇────◇\n")
        print(f"◇────◇────────◇────────────◇◇────◇────────◇────────────◇")
        print(f"|        ⚔️ ⌂ Sword      🏹 ⌂ Bow      🔫 ⌂ Gun        |")
        print(f"◇────────────◇────────◇────◇◇────────────◇────────◇────◇\n")
        item_give = input(f"{self.user_name}> ")
        if len(self.items) < self.max_items:
            if item_give in ["sword", "bow", "gun"]:
                with open(self.inventory_file, "a", encoding="utf-8") as file:
                    file.write(f"[{item_give.upper()}] has been given\n")
                self.items.append(self.item_skin(item_give))
            else:
                print(f"[ERROR] Invalid item name back to home in 2 seconds...")
                time.sleep(2)
        else:
            print(f"[ERROR] Maximum number of items reached back to home in 2 seconds...")
            time.sleep(2)

# - - - - - - - - - - - - - - - - - - # WITHDRAW INV MODULE # - - - - - - - - - - - - - - - - - - #

    def withdraw(self):
        if self.items:
            withdrawn_item = self.items.pop()
            with open(self.inventory_file, "a", encoding="utf-8") as file:
                file.write(f"[{withdrawn_item.upper()}] has been withdrawn\n")
        else:
            print(f"[ERROR] Inventory is empty. Nothing to withdraw wait 2 seconds...")
            time.sleep(2)

# - - - - - - - - - - - - - - - - - - # EXPORT INV MODULE # - - - - - - - - - - - - - - - - - - #

    def export_save(self):
        with open(self.save_file, "w", encoding="utf-8") as file:
            file.write(f"{self.user_name};")
            file.write(";".join(self.items))
            
        with open(self.inventory_file, "a", encoding="utf-8") as file:
            file.write(f"[EXPORT] Inventory saved successfully\n")
        
        clear()
        inventory.display_inventory()
        print(f"◇────◇────────◇────────────◇◇────◇────────◇────────────◇")
        print(f"|            You can now import your backup            |")
        print(f"|              directly from the home menu             |")
        print(f"◇────────────◇────────◇────◇◇────────────◇────────◇────◇\n")
        print(f"Press a key to exit\n\n")
        input(f"{self.user_name}> ")

# - - - - - - - - - - - - - - - - - - # IMPORT INV MODULE # - - - - - - - - - - - - - - - - - - #

    def import_save(self):
        with open(self.save_file, "r", encoding="utf-8") as file:
            content = file.read().split(";")
            self.user_name = content[0].strip()
            self.items = content[1:]
        
        with open(self.inventory_file, "a", encoding="utf-8") as file:
            file.write(f"[IMPORT] Inventory loaded successfully\n")


# - - - - - - - - - - - - - - - - - - # SET NAME INV MODULE # - - - - - - - - - - - - - - - - - - #

    def set_name(self):
        clear()
        inventory.display_inventory()
        print(f"◇────◇────────◇────────────◇◇────◇────────◇────────────◇")
        print(f"|                  Enter your new name                 |")
        print(f"◇────────────◇────────◇────◇◇────────────◇────────◇────◇\n")

        past_name = self.user_name
        self.user_name = input(f"{self.user_name}> ")
        with open(self.inventory_file, "a", encoding="utf-8") as file:
            file.write(f"[USERNAME] Successfully edit username from {past_name} to {self.user_name}\n")

# - - - - - - - - - - - - - - - - - - # RESET INV MODULE # - - - - - - - - - - - - - - - - - - #

    def reset(self):
        self.items = []
        self.user_name = ""
        open(self.save_file, "w").close()
        open(self.inventory_file, "w").close()

# - - - - - - - - - - - - - - - - - - # SKIN INV MODULE # - - - - - - - - - - - - - - - - - - #

    @staticmethod
    def item_skin(item_id):
        return "⚔️" if item_id == "sword" else ("🏹" if item_id == "bow" else "🔫")

# - - - - - - - - - - - - - - - - - - # CODE LAUNCHER # - - - - - - - - - - - - - - - - - - #

if __name__ == "__main__":
    try:
        inventory = Inventory()
        inventory.user_name = ""
        while True:
            clear()
            home_choice()

    except Exception as error:
        print(f"[ERROR] {error}")
