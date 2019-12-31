import pygame
import constants
import random
import sys
import time

screen = constants.initalize()

class Obstacle:

    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = random.randint(self.width,constants.screenWidth - self.width)
        self.y = self.height   
        self.image = pygame.image.load("Obstacles/Traffic-Cone.png")    
        self.rect = self.image.get_rect() 
    

    def animate(self,screen):
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.rect = self.image.get_rect() 

        if self.y >= constants.screenHeight:
            self.y = -self.height
            self.x = random.randint(self.width + 50,constants.screenWidth - self.width - 50)
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.image,self.rect)
        self.y += 5

    #Function to handle collision between car and obstacle

    def collision(self,car):
        if self.rect.colliderect(car.rect):
            print(time.time())
            print(car.rect)
            print(self.rect)
        else:
            print("No collision")