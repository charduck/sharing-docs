import random

# ==========================================
# THE DARKEST DUNGEON - BROKEN BUILD v0.1
# AUTHOR: SpaghettiCoder99
# FIXED BY: Lucas and Owen
# ==========================================

def show_instructions():
    print("Escape the Dungeon!")
    print("Commands: go [north, south, east, west], get [item], scan [items/rooms], quit")
    print("Goal: Find the Key and reach the Exit.")

def show_status(current_room, inventory, hp):
    # TODO: Make the HUD look better
    print("---------------------------")
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")
    print(f"Health: {hp}")
    print("---------------------------")

def main():
    # Map configuration
    rooms = {
        'Hall': {
            'south': 'Kitchen',
            'east': 'Dining Room',
            'item': 'Shield'
        },
        'Kitchen': {
            'north': 'Hall',
            'item': 'Monster'
        },
        'Dining Room': {
            'west': 'Hall',
            'south': 'Garden',
            'item': 'Potion' 
        },
        'Garden': {
            'north': 'Dining Room',
            'east': 'Exit',
            'item': 'Key' 
        },
        'Exit': {
            'west': 'Garden'
        }
    }

    current_room = 'Hall'
    inventory = []
    

    hp = 100 

    show_instructions()

    # GAME LOOP
    while True:
        show_status(current_room, inventory, hp)

        if hp <= 0:
            print("You died! Game Over.")
            break

        # Get user input
        move = input("> ").lower().split()

        # Handle empty input
        if len(move) == 0:
            continue

        action = move[0]

        # MOVEMENT HANDLER
        if action == "go":
            if len(move) > 1:
                direction = move[1]
                
                # NAVIGATION LOGIC        
                if direction in rooms[current_room]:
                    current_room = rooms[current_room][direction]
                else:
                    print("You can't go that way!")
            else:
                print("Go where?")

        # ITEM HANDLER
        elif action == "get":
            if len(move) > 1:
                item_wanted = move[1]
                
                # Check if item is in room
                if 'item' in rooms[current_room] and rooms[current_room]['item'].lower() == item_wanted:
                    if len(inventory) >= 2:
                            print("You have too many items!")
                    else:
                        print(f"You picked up the {item_wanted}!")
                        
                        if item_wanted == "monster":
                            chance = random.randint(1, 2)
                            if chance == 1:
                                print("The monster bites you!")
                                hp = hp - 50
                                del rooms[current_room]['item']
                                print("It scurried away...")

                            else:
                                print("You escaped the monster... it's gone.")
                                del rooms[current_room]['item']

                        if item_wanted == "potion":
                            print("You consumed the potion...")
                            hp = hp + 20
                            del rooms[current_room]['item']

                        else:
                            if item_wanted != "potion":
                                inventory.append(item_wanted)
                                del rooms[current_room]['item']
                else:
                    print(f"There is no {item_wanted} here.")
            else:
                print("Get what?")

        elif action == "scan":
            mode = move[1] if len(move) > 1 else "all"

            print("SCANNED")

            if mode in ("all", "items"):
                if "item" in rooms[current_room]:
                    print(f"Detected item: {rooms[current_room]['item']}.")
                else:
                    print("No item detected.")

            if mode in ("all", "rooms"):
                exits = {d: r for d, r in rooms[current_room].items() if d in ['north', 'south', 'east', 'west']}
                if exits:
                    print("Nearby rooms:")
                    for direction, room in exits.items():
                        print(f"{direction.title()} -> {room}")
                else:
                    print("No visible exits.")
            continue

        elif action == "xyzzy":
            current_room = "Dining Room"
            print("Suddenly, you find yourself in the Dining Room!")
        
        # QUIT HANDLER
        elif action == "quit": 
            break
            
        if current_room == "Exit":
            if "key" in inventory:
                print("You use the key and escape!")
                break


if __name__ == "__main__":
    main()
