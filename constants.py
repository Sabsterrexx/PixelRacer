#This file is responsible for declaring all the global variables that wil be used across files

#importing the pygame module
import pygame
import random

#Making the global variables

screenWidth = 0
screenHeight = 0
clock = pygame.time.Clock()
fps  = 60
cx = 0
cy = 0
distance_travelled = 0
direction = random.randint(1,2)

#the colors used in the game are set to a bunch of key (color name as a string) and value (color's rgb code as a tuple) pairs in a dictionary
colors = {"WHITE": (255,255,255) , "GREEN": (0,102,0) , "RED": (255,0,0), "BLUE": (0,0,255), "BLACK": (0,0,0),"GREY": (55,55,55),"YELLOW": (255,255,0)}

car_images = ["Aston Martin DB9.png","Audi R8Gt.png","Chevrolet Corvette.png","Dodge Viper GTS.png","Ferrari 458 Italia.png","Lamborghini Murcielago.png","Lotus Elise.png","McLaren F1.png","Mercedes Benz SLS AMG.png","Pagani Zonda F.png","Porsche 911 Carrera.png","Toyota Supra.png"]

#function that initalize's the constants for the screen:

def initalize():
    #the word global is used to acess variables outside of the function and not create new ones with the same name
    global screenWidth
    global screenHeight
    global cx
    global cy
    pygame.init()
    screenSize = (800,600)
    screen = pygame.display.set_mode((screenSize),0)
    pygame.display.set_caption("Pixel Racer")

    pygame.display.update()
    screenWidth = screen.get_width()
    screenHeight = screen.get_height()
    cx = screenWidth//2
    cy = screenHeight//2

    #returning screen at the end
    return screen