import random
from fire_water_grass import fire_water_grass

y = 0
a = 0
b = 0
c = 0
player_count = input("One or two player: ")

while y == 0:
    while a == 0:   
        if player_count  == ("one") or ("1") or ("One"):
            choice_2 = random.randint(1,3)
            choice_1 =input("Choose Fire, Water, or Grass: ")
    
            if choice_1 == ("fire"):
                choice_1 = 1
            if choice_1 == ("water"):
                choice_1 == 2
            if choice_1 == ("grass"):
                choice_1 = 3
            
            win_player = fire_water_grass(choice_1, choice_2, player_count)
            pl_ag = input("Would You like to play again: ")
            if pl_ag == "yes":
                continue
            y = y + 1
            a = a + 1
            #break
            #print("stuck in a loop")
        elif player_count  == ("two") or ("2") or ("Two"):
            choice_1 = input("Player 1 choose Fire, Water, or Grass: ")

            x = 0
            while x < 50:
                print("                                                  ")
                x = x + 1
            choice_2 = input("Player 2 choose Fire, Water, or Grass: ")

            if choice_1 == ("fire"):
                choice_1 = 1
            if choice_2 == ("fire"):
                choice_2 = 1
            if choice_1 == ("water"):
                choice_1 = 2
            if choice_2 == ("water"):
                choice_2 = 2
            if choice_1 == ("grass"):
                choice_1 = 3
            if choice_2 == ("grass"):
                choice_2 = 3

               
            win_player = fire_water_grass(choice_1, choice_2, player_count)
            pl_ag = input("Would you like to play again: ")
            if pl_ag == "yes":
                    continue
            y = 1
            a = 1
            quit
            
            
            
        
            

    quit
quit
    
