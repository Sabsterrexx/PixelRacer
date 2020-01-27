import pygame
import constants
from PlayerCar import PlayerCar
import random



class AiCar(PlayerCar):


    # Function to generate random car:
    def generate_random_car(self, min_x, max_x):
        car_choice = random.randint(0,11)
        self.image = pygame.image.load("Car_Images/" + constants.car_images[car_choice])
        self.car = pygame.transform.rotate(self.image,90)
        self.direction = random.randint(1,2)
        self.frames = 0
        self.min_x = min_x
        self.max_x = max_x
        self.x = min_x




    #------------------------------------------------ Function to drive itself: -------------------------------------- #

    def race(self):
 
        self.frames = (self.frames +1 ) % 100

        #if self.x >= constants.screenWidth-55 or self.y >= constants.screenHeight-105 or self.x == 0 or self.y==0:
        if self.x >= self.max_x-55 or self.x <= 2*self.min_x or self.y >= constants.screenHeight-105  or self.y==0:
            #reset the variables
            self.dx = 0
            self.dy = 0
            if self.direction == 1:
                self.direction = 2
            else:
                self.direction = 1


    

        if self.frames < 50:
            #randomly decide which direction to move:
            self.dx = random.randint(0,5)
            self.dy = 0
        else:
            self.dy = random.randint(0,5)
            self.dx = 0


        #if it decided to move vertically:
        if self.direction ==  2:
            self.dx *= -1
            self.dy *= -1

        
        #making the car move:
        self.move()

        #updating the distance travelled:
