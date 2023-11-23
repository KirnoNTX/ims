## Inventory Management System

### Overview

This is a simple command-line inventory management system written in Python. The program allows users to perform various actions on an inventory, such as giving items, withdrawing items, exporting and importing the inventory, debugging, and resetting the inventory.

### Features

- **Give Items:** Users can give items like swords, bows, and guns to the inventory.
- **Withdraw Items:** Users can withdraw the last item added to the inventory.
- **Export/Import:** The inventory can be exported to a save file and later imported to resume the inventory state.
- **Username:** Users can have their username personalized to their image
- **Debugging:** Provides debug information about the current state of the inventory.
- **Reset:** Resets the inventory, clearing all items.

### How to Use

1. **Give Items (`G`):** Choose from the available items (Sword, Bow, Gun) to give to the inventory.

2. **Withdraw Items (`W`):** Withdraw the last item added to the inventory.

3. **Export Inventory (`E`):** Save the current state of the inventory to a file.

4. **Import Inventory (`I`):** Load a previously saved inventory state from a file.

5. **Set Name (`N`):** Create or update your name in the program.

6. **Debug (`D`):** View debug information about the inventory, including the file paths and current items.

7. **Reset (`R`):** Clear all items in the inventory and reset it.

### Inventory Display

The inventory display shows a graphical representation of the items in the inventory using symbols like ⚔️ (sword), 🏹 (bow), and 🔫 (gun).

### Error Handling

If an invalid action is entered, the program will display an error message and wait for 2 seconds before returning to the main menu.

### File Paths

- **Inventory File:** "./logs/inv.txt"
- **Save File:** "./data/save.txt"

### How to Run

1. Make sure you have Python installed on your system.

2. Run the script using the command:

   ```
   python index.py
   ```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.