import pygame
from pygame.locals import *
import sys
from game_display import *

class map_1() :
    def __init__(self) :
        self.map_1 = pygame.image.load('C:/Users/User/Desktop/shrimp cocktail/map1.png')

        self.ground_1 = pygame.image.load('C:/Users/User/Desktop/shrimp cocktail/dirt-1.png')
        self.ground_2 = pygame.image.load('C:/Users/User/Desktop/shrimp cocktail/dirt-2.png')
        self.ground_3 = pygame.image.load('C:/Users/User/Desktop/shrimp cocktail/dirt-3.png')

        self.Shrimp_front_atk = pygame.image.load("C:/Users/User/Desktop/shrimp cocktail/Shrimp-front-atk.png")
        self.Shrimp_front = pygame.image.load("C:/Users/User/Desktop/shrimp cocktail/Shrimp-front.png")
        self.Shrimp_back_atk = pygame.image.load("C:/Users/User/Desktop/shrimp cocktail/Shrimp-back-atk.png")
        self.Shrimp_back = pygame.image.load("C:/Users/User/Desktop/shrimp cocktail/Shrimp-back.png")

    def type_1(self) :
        charactor = [[self.Shrimp_front_atk,0,7,self.Shrimp_front,self.Shrimp_back_atk,self.Shrimp_back]]
        ground = [[ self.ground_1,0,7],[ self.ground_1,1,7],[self.ground_2,2,7],[self.ground_1,3,7],[self.ground_2,4,7],[self.ground_2,5,7],[self.ground_2,6,7],[self.ground_1,7,7]]
        gui = built(self.map_1,ground,charactor)
        gui

t = map_1()
go = t.type_1()
go