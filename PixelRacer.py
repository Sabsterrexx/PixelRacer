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

screenTitle = ScreenText()
screenTitle.text = "Press 'P' or 'Start' to play"
screenTitle.x -= 100

timerTitle = ScreenText()
timerTitle.color = constants.colors['GREEN']
timerTitle.x -= 50

gameTitle = ScreenText()
gameTitle.text = "Pixel Racer"
gameTitle.y -= screenTitle.size + 20

endTitle = ScreenText()
endTitle.color = constants.colors['GREEN']
endTitle.text = "Game Over"
endTitle.y -= endTitle.size + 20

player_car = PlayerCar()

ai = AiCar()
ai.generate_random_car(0, constants.screenWidth/3)

ai2 = AiCar()
ai2.generate_random_car( constants.screenWidth/3, constants.screenWidth * 2/3)

ai3 = AiCar()
ai3.generate_random_car(constants.screenWidth * 2/3, constants.screenWidth)

roadLine1 = RoadLine()

roadLine2 = RoadLine()
roadLine2.y = roadLine1.y + 2 * constants.screenHeight/5

roadLine3 = RoadLine()
roadLine3.y = roadLine2.y + 2 * constants.screenHeight/5


obstacle = Obstacle()

obstacle2 = Obstacle()
obstacle2.image = pygame.image.load("Obstacles/Gas-Barrel.png")
obstacle2.height += 5
obstacle2.width += 5

obstacle3 = Obstacle()
obstacle3.image = pygame.image.load("Obstacles/Road-Block.png")
obstacle3.height += 15
obstacle3.width += 40

#initalise joysticks:
joyStickHandler.initJoysticks()

pygame.mixer.init()
pygame.mixer.music.load("Sounds/car acceleration sound effect.mp3")
pygame.mixer.music.play(-1)


screen = constants.initalize()

constants.startTime = time.perf_counter()

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


        constants.startTime = time.perf_counter()

        screen.fill(constants.colors['GREEN'])

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

        timerTitle.y = timerTitle.size 

        timerTitle.color = constants.colors["WHITE"]

        constants.clock.tick(constants.fps)

        constants.endTime = int(time.perf_counter() - constants.startTime)

        timerTitle.text = str(constants.endTime)

        screen.fill(constants.colors["GREEN"])
        pygame.draw.rect(screen,constants.colors["GREY"],(50,0,constants.screenWidth-100,constants.screenHeight),0)

        roadLine1.animate(screen)
        roadLine2.animate(screen)
        roadLine3.animate(screen)

        player_car.move()
        player_car.render()
        player_car.border_collision()

        ai.render()
        ai.border_collision()
        ai.race()

        ai2.render()
        ai2.border_collision()
        ai2.race()

        ai3.render()
        ai3.border_collision()
        ai3.race()

        obstacle.animate(screen)
        
        obstacle2.animate(screen)

        obstacle3.animate(screen)

        timerTitle.write()

        #Detecting if the car collides with the obstacles:

        if obstacle.collision(player_car) or obstacle2.collision(player_car) or obstacle3.collision(player_car):
            playing = False
            end = True
            
            constants.endTime = int(time.perf_counter() - constants.startTime)

        pygame.display.update()



        # #-------------------------End Screen Loop: -------------------------#


        while end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        start = True
                        end = False


            timerTitle.color = constants.colors["GREEN"]

            timerTitle.y = constants.cy + timerTitle.size 

            timerTitle.text = "You lasted " + str(constants.endTime) + " seconds."

            #resetting everything
            obstacle.y = obstacle.height
            obstacle2.y = obstacle2.height
            obstacle3.y = obstacle3.height
            player_car.y = constants.screenHeight - player_car.height
            player_car.x = constants.cx

            #writing text to end screen
            screen.fill(constants.colors["YELLOW"])
            timerTitle.write()
            endTitle.write()
            pygame.display.update()


#-----------------------End of code -------------------------------#
