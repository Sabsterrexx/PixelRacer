import pygame
import constants

screen = constants.initalize()

class RoadLine:
    def __init__(self):
        self.height = constants.screenHeight/5
        self.width = 10
        self.x = constants.cx - self.width
        self.y = -self.height
    
    def animate(self,screen):
        self.y += 5
        if self.y >= constants.screenHeight:
            self.y = -self.height
        
        pygame.draw.rect(screen,constants.colors["YELLOW"],(self.x,self.y,self.width,self.height),0)