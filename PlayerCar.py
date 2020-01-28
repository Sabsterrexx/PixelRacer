import pygame
import constants

screen = constants.initalize()

class PlayerCar:
    def __init__(self):
        self.x = constants.cx
        self.speed = 5
        self.dy = 0
        self.dx = 0
        self.image = pygame.image.load("Car_Images/Toyota Supra.png")
        self.width = 50
        self.height = 100
        self.car = pygame.transform.rotate(self.image,90)
        self.rect = self.car.get_rect()
        self.y = constants.screenHeight - self.height
        self.lives  = 3

    
    def render(self):
        self.car = pygame.transform.scale(self.car,(self.width,self.height))
        self.rect = self.car.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.car,self.rect)

    def border_collision(self):

        if self.x >= constants.screenWidth - (self.width + 5):
            self.x = constants.screenWidth - (self.width + 5)
        elif self.x <= 0:
            self.x = 0

        if self.y >= constants.screenHeight - (self.height + 5):
            self.y = constants.screenHeight - (self.height + 5)
        elif self.y <= 0:
            self.y = 0

    def move(self):
        self.y += self.dy
        self.x += self.dx
