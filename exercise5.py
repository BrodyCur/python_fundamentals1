distance = 0
energy = 100
hunger = 0
n_block = 0
s_block = 0
e_block = 0
w_block = 0

while True:
    print("Would you like to walk or run? Enter 'help' for more actions.")
    print("Distance: {} km".format(distance))
    print("Energy: {}".format(energy))
    print("Hunger: {}".format(hunger))
    activity = input().lower()

    if activity == "walk" or activity == "run" and energy > 0 and hunger < 100:
        print("Please choose a direction(north, south, east, west).")
        direction = input().lower()
        if direction == "north" or direction == "n":
            n_block += 1
            print("{} block(s) North".format(n_block))
        elif direction == "south" or direction == "s":
            s_block += 1
            print("{} block(s) South".format(s_block))
        elif direction == "east" or direction == "e":
            e_block += 1
            print("{} block(s) East".format(e_block))
        elif direction == "west" or direction == "w":
            w_block += 1
            print("{} block(s) West".format(w_block))
        else:
            print("Not a direction")
            continue

    if activity == "walk" or activity == "w":
        if energy > 0 and hunger < 100:
            distance += 1
            hunger += 5
        else:
            print("You need to rest or eat first!")
    elif activity == "run" or activity == "r":
        if energy > 10 and hunger < 95:
            distance += 5
            energy -= 20
            hunger += 10
        else:
            print("You need to rest or eat first!")
    elif activity == "rest":
        energy += 30
    elif activity == "eat":
        energy += 50
        hunger = 0
    elif activity == "help":
        print("Eat: Gain 50 energy\nRest: Gain 30 energy\n Go Home: Quit")
    elif activity == "go home"or activity == "home" or activity == "quit" or activity == "q":
        print("Good work out!")
        break
    else:
        print("Improper Input")
        continue
        
    if energy > 100:
        energy = 100
    elif energy < 0:
        energy = 0