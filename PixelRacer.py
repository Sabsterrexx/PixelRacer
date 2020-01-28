#--------------------------- Saabit Zubairi Final Game 2020/01/27-------------------------------#




#--------------------- Import Required Libraries -----------------------#

import pygame
import constants
import sys
import time
from PlayerCar import PlayerCar
from roadLine import RoadLine
from obstacle import Obstacle
from screenText import ScreenText
from AiCar import AiCar
import joyStickHandler

#-------- Create All Game Objects ----------------------#



#creating the start screen title
screenTitle = ScreenText()
screenTitle.text = "Press 'P' or 'Start' to play"
screenTitle.x -= 100

#creating a lives title
livesTitle = ScreenText()
livesTitle.text = "Lives: "
livesTitle.y = livesTitle.size
livesTitle.x = constants.screenWidth - (livesTitle.size + 200)
livesTitle.color = constants.colors["RED"]


#creating the timeer title
timerTitle = ScreenText()
timerTitle.color = constants.colors['GREEN']
timerTitle.x -= 50


#creating the game title
gameTitle = ScreenText()
gameTitle.text = "Pixel Racer"
gameTitle.y -= screenTitle.size + 20


#creating the end screen title
endTitle = ScreenText()
endTitle.color = constants.colors['GREEN']
endTitle.text = "Game Over"
endTitle.y -= endTitle.size + 20


#creating the player car
player_car = PlayerCar()


#creating the 3 ai cars
ai = AiCar()
ai.generate_random_car(0, constants.screenWidth/3)

ai2 = AiCar()
ai2.generate_random_car( constants.screenWidth/3, constants.screenWidth * 2/3)

ai3 = AiCar()
ai3.generate_random_car(constants.screenWidth * 2/3, constants.screenWidth)


# creatig and animating the 3 road lines
roadLine1 = RoadLine()

roadLine2 = RoadLine()
roadLine2.y = roadLine1.y + 2 * constants.screenHeight/5

roadLine3 = RoadLine()
roadLine3.y = roadLine2.y + 2 * constants.screenHeight/5

#creating the obstacle
obstacle = Obstacle()

#creating the 2nd obstacle
obstacle2 = Obstacle()
obstacle2.image = pygame.image.load("Obstacles/Gas-Barrel.png")
obstacle2.height += 5
obstacle2.width += 5


#creating the 3rd obstacle
obstacle3 = Obstacle()
obstacle3.image = pygame.image.load("Obstacles/Road-Block.png")
obstacle3.height += 15
obstacle3.width += 40

#initalise joysticks:
joyStickHandler.initJoysticks()

#generating the sounds
pygame.mixer.init()
pygame.mixer.music.load("Sounds/car acceleration sound effect.mp3")
pygame.mixer.music.play(-1)

#creating a screen variable with the screen constants
screen = constants.initalize()

#starting a timer
constants.startTime = time.perf_counter()

#setting the loop values
end = False
playing = False
start = True


#--------------------------Main Loop:----------------------------------------------#

while True:


 #-------------------------Start Screen Loop: -------------------------#

    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    end = False
                    start = False
                    playing = True
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == constants.joyStart:
                    start = False
                    playing = True

        #starting the timer from 0
        constants.startTime = time.perf_counter()

        #creating the start screen background
        screen.fill(constants.colors['GREEN'])


        #writing the titles onto the screen
        gameTitle.write()

        screenTitle.write()

        pygame.display.update()



 #-------------------------Game Screen Loop: -------------------------#


    while playing:
        for event in pygame.event.get():
            #cross-button event listener for quitting the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_car.dy = -player_car.speed
                elif event.key == pygame.K_DOWN:
                    player_car.dy = player_car.speed
                elif event.key == pygame.K_LEFT:
                    player_car.dx = -player_car.speed
                elif event.key == pygame.K_RIGHT:
                    player_car.dx = player_car.speed
            #if no keys are pressed set the vertical and horizontal speed to 0
            elif event.type == pygame.KEYUP:
                player_car.dy = 0
                player_car.dx = 0
            #coding the controllers:
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == constants.joyUp:
                    player_car.dy = -player_car.speed                   
                elif event.button == constants.joyDown:
                    player_car.dy = player_car.speed
                elif event.button == constants.joyLeft:
                    player_car.dx = -player_car.speed
                elif event.button == constants.joyRight:
                    player_car.dx = player_car.speed            
            elif event.type == pygame.JOYBUTTONUP:
                    player_car.dx = 0
                    player_car.dy = 0

        #setting the y-value of the timer to the top of the screen

        timerTitle.y = timerTitle.size 

        #setting its title color to white

        timerTitle.color = constants.colors["WHITE"]

        #calculating how long the car has been driving
        constants.clock.tick(constants.fps)
        constants.endTime = int(time.perf_counter() - constants.startTime)


        #updating the timer title    
        timerTitle.text = str(constants.endTime)

        livesTitle.text = "Lives: " + str(player_car.lives)


        #changing the background color to green by drawing a green rectangle in the background:
        screen.fill(constants.colors["GREEN"])
        pygame.draw.rect(screen,constants.colors["GREY"],(50,0,constants.screenWidth-100,constants.screenHeight),0)

        #animating the roadlines onto the screen:
        roadLine1.animate(screen)
        roadLine2.animate(screen)
        roadLine3.animate(screen)


        #drawing the player car onto the screen and making it move
        player_car.move()
        player_car.render()
        player_car.border_collision()

        #setting up the 3 ai cars and drawing then onto the screen and makking then move
        ai.render()
        ai.border_collision()
        ai.race()

        ai2.render()
        ai2.border_collision()
        ai2.race()

        ai3.render()
        ai3.border_collision()
        ai3.race()

        #drawing the obstacles onto the screen        

        obstacle.animate(screen)
        
        obstacle2.animate(screen)

        obstacle3.animate(screen)

        #writing the timer title onto the screen 

        timerTitle.write()

        #writign the numebr of lives onto the screen 

        livesTitle.write()

        #Detecting if the car collides with the obstacles and deciding what to do:

        if obstacle.collision(player_car) or obstacle2.collision(player_car) or obstacle3.collision(player_car):
            int(player_car.lives) 
            player_car.lives -= 1
            if player_car.lives == 0:
                playing = False
                end = True
                constants.endTime = int(time.perf_counter() - constants.startTime)

        pygame.display.update()



        #-------------------------End Screen Loop: -------------------------#


        while end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        start = True
                        end = False


            #Mkaing the timer title display the final score:

            timerTitle.color = constants.colors["GREEN"]

            timerTitle.y = constants.cy + timerTitle.size 

            timerTitle.text = "You lasted " + str(constants.endTime) + " seconds."

            #resetting everything
            obstacle.y = obstacle.height
            obstacle2.y = obstacle2.height
            obstacle3.y = obstacle3.height
            player_car.y = constants.screenHeight - player_car.height
            player_car.x = constants.cx
            player_car.lives = 3

            #writing text to end screen
            screen.fill(constants.colors["YELLOW"])
            timerTitle.write()
            endTitle.write()
            pygame.display.update()


#-----------------------End of code -------------------------------#
