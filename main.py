import random
from fire_water_grass import fire_water_grass
import pygame


y = 0
a = 0
b = 0
c = 0
player_count = input("One or two players: ")

while y == 0:
    while a == 0:   
        if player_count  == ("one") or player_count == "1":
            choice_2 = random.randint(1,3)
            choice_1 =input("Choose Fire, Water, or Grass: ")
    
            if choice_1 == ("fire") or choice_1 == "Fire":
                choice_1 = 1
            if choice_1 == ("water") or choice_1 == "Water":
                choice_1 = 2
            if choice_1 == ("grass") or choice_1 == "Grass":
                choice_1 = 3
            
            win_player = fire_water_grass(choice_1, choice_2, player_count)
            pl_ag = input("Would you like to play again: ")
            if pl_ag == "yes" or pl_ag == "Yes":
                continue
            y = y + 1
            a = a + 1
        elif player_count  == ("two") or player_count== "2":
            choice_1 = input("Player 1, choose Fire, Water, or Grass: ")

            x = 0
            while x < 50:
                print("                                                  ")
                x = x + 1
            choice_2 = input("Player 2, choose Fire, Water, or Grass: ")

            if choice_1 == ("fire") or choice_1 == "Fire":
                choice_1 = 1
            if choice_2 == ("fire") or choice_2 == "Fire":
                choice_2 = 1
            if choice_1 == ("water") or choice_1 =="Water":
                choice_1 = 2
            if choice_2 == ("water") or choice_2 == "Water":
                choice_2 = 2
            if choice_1 == ("grass") or choice_1 == "Grass":
                choice_1 = 3
            if choice_2 == ("grass") or choice_2 == "Grass":
                choice_2 = 3

            win_player = fire_water_grass(choice_1, choice_2, player_count)
            pl_ag = input("Would you like to play again: ")
            if pl_ag == "yes" or pl_ag == "Yes":
                    continue
            y = 1
            a = 1

if win_player == 2 or win_player == 1 or win_player == 3:  
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("fire_type_symbol.png")
    image = pygame.image.load("fire_type_symbol.png").convert_alpha()
    image = pygame.transform.smoothscale(image, (200, 150))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        screen.blit(image, (300, 200))
        pygame.display.flip()
    pygame.quit
if win_player == 2.1 or win_player == 1.1 or win_player == 3.1:
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("water_type_symbol.png")
    image = pygame.image.load("water_type_symbol.png").convert_alpha()
    image = pygame.transform.smoothscale(image, (200, 150))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        screen.blit(image, (300, 200))
        pygame.display.flip()
    pygame.quit
if win_player == 2.2 or win_player == 1.2 or win_player == 3.2:
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("grass_type_symbol.jpeg")
    image = pygame.image.load("grass_type_symbol.jpeg").convert_alpha()
    image = pygame.transform.smoothscale(image, (200, 150))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        screen.blit(image, (300, 200))
        pygame.display.flip()
    pygame.quit

               
            
            
        
            

quit
quit
    
