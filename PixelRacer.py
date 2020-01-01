#--------------------- Import Required Libraries -----------------------#

import pygame
import constants
import sys
from PlayerCar import PlayerCar
from roadLine import RoadLine
from obstacle import Obstacle
from screenText import ScreenText
from AiCar import AiCar


#-------- Create All Game Objects ----------------------#

screenTitle = ScreenText()
screenTitle.text = "Press 'P' to play"


gameTitle = ScreenText()
gameTitle.text = "Pixel Racer"
gameTitle.y -= screenTitle.size + 20

endTitle = ScreenText()
endTitle.color = constants.colors['GREEN']
endTitle.text = "Game Over"
endTitle.y -= endTitle.size + 20

player_car = PlayerCar()

ai = AiCar()
ai.generate_random_car()

ai2 = AiCar()
ai2.generate_random_car()

ai3 = AiCar()
ai3.generate_random_car()

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


pygame.mixer.init()
pygame.mixer.music.load("Sounds/car acceleration sound effect.mp3")
pygame.mixer.music.play(-1)


screen = constants.initalize()

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
                    start = False
                    playing = True
    
    
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

        constants.clock.tick(constants.fps)

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
        ai.race(constants.distance_travelled,constants.direction)

        ai2.render()
        ai2.border_collision()
        ai2.race(constants.distance_travelled,constants.direction)

        ai3.render()
        ai3.border_collision()
        ai3.race(constants.distance_travelled,constants.direction)


        obstacle.animate(screen)
        
        obstacle2.animate(screen)

        obstacle3.animate(screen)

        if obstacle.collision(player_car) or obstacle2.collision(player_car) or obstacle3.collision(player_car):
            playing = False
            end = True

        pygame.display.update()



        #-------------------------End Screen Loop: -------------------------#


        while end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



            screen.fill(constants.colors["YELLOW"])
            endTitle.write()
            pygame.display.update()


#-----------------------End of code -------------------------------#