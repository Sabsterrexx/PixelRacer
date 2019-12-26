import pygame
import constants

screen = constants.initalize()

class ScreenText:
    def __init__(self):
        self.size = 50
        self.text = ''
        self.color = constants.colors["YELLOW"]
        self.font = 'bahnschrift'
        self.x = constants.cx - (3*self.size)
        self.y = constants.cy - self.size


        #attributes needed for the 'write' method:
        self.fonttitle = pygame.font.SysFont(self.font,self.size)
        self.rendertitle = self.fonttitle.render(self.text,True,self.color)
        self.screen = screen

        

    #writing the font onto the screen:
    def write(self):
        self.rendertitle = self.fonttitle.render(self.text,True,self.color)
        return self.screen.blit(self.rendertitle,(self.x,self.y))