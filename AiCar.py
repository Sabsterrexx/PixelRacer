import pygame
import constants
from PlayerCar import PlayerCar
import random



class AiCar(PlayerCar):


    # Function to generate random car:

    def generate_random_car(self):
        car_choice = random.randint(0,11)
        self.image = pygame.image.load("Car_Images/" + constants.car_images[car_choice])
        self.car = pygame.transform.rotate(self.image,90)


    # ---------------------Code that does not work properly (Car moves erratically) (No syntax errors)-----------------#


    #------------------------------------------------ Function to drive itself: -------------------------------------- #

    def race(self,distance_travelled,direction):
 
        #if it travels 500 units:
        if distance_travelled == 0 or distance_travelled == 500:
            #reset the variables
            distance_travelled = 0
            self.dx = 0
            self.dy = 0

            #randomly decide which direction to move:
            direction = random.randint(1,2)

            #if it decided to move horizontally:
            if direction == 1:
                self.dx = random.randint(-5,5)
                distance_travelled += abs(self.dx)

            #if it decided to move vertically:
            elif direction ==  2:
                self.dy = random.randint(-5,5)
                distance_travelled += abs(self.dy)

        #making the car move:
        self.move()

        #updating the distance travelled:
        distance_travelled += abs(self.dx) + abs(self.dy)