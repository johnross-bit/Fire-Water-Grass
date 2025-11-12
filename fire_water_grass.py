

def fire_water_grass(choice_1, choice_2, player_count):
    if player_count == ("one"):    
        if choice_2 == 1 and choice_1 == 3:
            print("You lose, Fire beats Grass.")
            return 2
        if choice_2 == 2 and choice_1 == 1:
            print("You lose, Water beats Fire.")
            return 2.1
        if choice_2 == 3 and choice_1 == 2:
            print("You lose, Grass beats Water.")
            return 2.2
        if choice_1 == 1 and choice_2 == 3:
            print("You win, Fire beats Grass!")
            return 1
        if choice_1 == 2 and choice_2 == 1:
            print("second")
            print("You win, Water beats Fire!")
            return 1.1
        if choice_1 == 3 and choice_2 == 2:
            print("You win, Grass beats Water!")
            return 1.2
        if choice_1 == 1 and choice_2 == 1:
            print("It was a tie, you both chose Fire!")
            return 3
        if choice_1 == 2 and choice_2 == 2:
            print("It was a tie, you both chose Water!")
            return 3.1
        if choice_1 == 3 and choice_2 == 3:
            print("It was a tie, you both chose Grass!")
            return 3.2
    elif player_count == "two":
        if choice_2 == 1 and choice_1 == 3:
            print("Player 2 wins, Fire beats Grass.")
            return 2
        if choice_2 == 2 and choice_1 == 1:
            print("Player 2 wins, Water beats Fire.")
            return 2.1
        if choice_2 == 3 and choice_1 == 2:
            print("Player 2 wins, Grass beats Water.")
            return 2.2
        if choice_1 == 1 and choice_2 == 3:
            print("Player 1 wins, Fire beats Grass!")
            return 1
        elif choice_1 == 2 and choice_2 == 1:
            print("Player 1 wins, Water beats Fire!")
            return 1.1
        elif choice_1 == 3 and choice_2 == 2:
            print("Player 1 wins, Grass beats Water!")
            return 1.2
        if choice_1 == 1 and choice_2 == 1:
            print("It was a tie, you both chose Fire!")
            return 3
        if choice_1 == 2 and choice_2 == 2:
            print("It was a tie, you both chose Water!")
            return 3.1
        if choice_1 == 3 and choice_2 == 3:
            print("It was a tie, you both chose Grass!")
            return 3.2


