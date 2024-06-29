# Noah Figueroa


def present_instructions():
    print("----------------------------------------------------------------")
    print("Text Based Zombie Survival Game")
    print("Collect 7 items and save the world, or allow it to be zombified.")
    print("Movement commands include: go South, go North, go East, go West")
    print("Add to Inventory command: get 'item name'")


def present_status(room, inventory, item):
    print("----------------------------------------------------------------")
    print("You are in the", room)
    print("Inventory:", inventory)
    if (item not in inventory) and (room != 'Entrance') and (room != 'Hangar'):
        print("There is a", item, "in sight.")


def main():
    rooms = {
        'Entrance': {'East': 'Library', 'Item': 'None'},
        'Library': {'West': 'Entrance', 'East': 'Living Quarters', 'South': 'Meeting Hall', 'Item': 'map'},
        'Living Quarters': {'West': 'Library', 'Item': 'backpack'},
        'Meeting Hall': {'North': 'Library', 'West': 'Kitchen', 'South': 'Armory', 'Item': 'partner'},
        'Kitchen': {'East': 'Meeting Hall', 'Item': 'mre'},
        'Main Lab': {'East': 'Armory', 'Item': 'antidote'},
        'Armory': {'West': 'Main Lab', 'North': 'Meeting Hall', 'East': 'Shooting Range', 'Item': 'firearm'},
        'Shooting Range': {'West': 'Armory', 'South': 'Hangar', 'Item': 'manual'},
        'Hangar': {'North': 'Shooting Range', 'Item': 'None'}
            }
    present_instructions()
    room = 'Entrance'
    inventory = []
    present_status(room, inventory, rooms[room]['Item'])
    move = input("Enter your move:\n")
    while (room != 'exit') and (len(inventory) != 7):
        move = move.split()
        if (move[0] != 'go') and (move[0] != 'get') or (len(move) <= 1):
            print("----------------------------------------------------------------")
            print("INVALID MOVE!")
            present_status(room, inventory, rooms[room]['Item'])
        else:
            if (move[1] == rooms[room]['Item']) and (move[1] not in inventory):
                inventory.append(rooms[room]['Item'])
                print("----------------------------------------------------------------")
                print('You picked up the', rooms[room]['Item'])
                present_status(room, inventory, rooms[room]['Item'])
            elif (move[1] == rooms[room]['Item']) and (move[1] in inventory):
                print("----------------------------------------------------------------")
                print("You have already picked up the", rooms[room]['Item'], 'from this room.')
                present_status(room, inventory, rooms[room]['Item'])
            elif (move[1] != rooms[room]['Item']) and (move[0] == 'get'):
                print("----------------------------------------------------------------")
                print("There is no such item to acquire here.")
                present_status(room, inventory, rooms[room]['Item'])
            if move[1].capitalize() in rooms[room]:
                room = rooms[room][move[1].capitalize()]
                present_status(room, inventory, rooms[room]['Item'])
            elif (move[1].capitalize() not in rooms[room]) and (move[0] == 'go'):
                print("----------------------------------------------------------------")
                print("INVALID MOVE!")
                present_status(room, inventory, rooms[room]['Item'])
            if (room == 'Hangar') and (len(inventory) < 7):
                print("----------------------------------------------------------------")
                print('You have let the world rot...\nnow it is your turn.')
                print()
                print('GAME OVER, THANKS FOR PLAYING!')
                print("----------------------------------------------------------------")
                exit()
        move = input("Enter your move:\n")

    print("----------------------------------------------------------------")
    print('You have acquired the antidote and saved the world!')
    print('UNTIL NEXT TIME, HERO...')
    print("----------------------------------------------------------------")


main()