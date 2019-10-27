import pygame
import sys
import time
import Player
from Level_Layout import Wall
from Zombie import Zombie

class Game:

    pygame.init()

    BLACK = 0,0,0
    WHITE = 255,255,255

    screen = pygame.display.set_mode((600,500))

    Player.Player.screen = screen
    Zombie.screen = screen

    z1_coors = [60,440,15,15]

    player = Player.Player(560, 460)
    zombie = Zombie(BLACK, z1_coors)
    zombie.dx = 5


    level = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W              W             W",
        "W              W             W",
        "W              W             W",
        "W   WWWWWWWWWWWWWWWWWWWWWW   W",
        "W                            W",
        "W                            W",
        "W              W   WWWWWWWWWWW",
        "W              W             W",
        "W              W             W",
        "W              WWWWWWWWWWW   W",
        "WWWWW   WWWWWWWW             W",
        "W              W             W",
        "W              W             W",
        "W    WWWWWWWWWWWWWWWWWWWWWWWWW",
        "W     W            W         W",
        "W                  W         W",
        "W                  W         W",
        "W                  W     W   W",
        "W     WWWWWWWWWWWWWW     W   W",
        "W                  W     W   W",
        "W                        W   W",
        "W                        W   W",
        "W                        W   W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]

    x = y = 0
    for row in level:
        for col in row:
            if col == "W":
                Wall((x,y))
            x += 20
        y += 20
        x = 0



    while True:

        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    player.delta_move_x = -1
                    player.direction = 'left'
                elif event.key == pygame.K_e:
                    player.delta_move_y = -1
                    player.direction = 'up'
                elif event.key ==  pygame.K_f:
                    player.delta_move_x = 1
                    player.direction = 'right'
                elif event.key == pygame.K_d:
                    player.delta_move_y = 1
                    player.direction = 'down'
                elif event.key == pygame.K_SPACE:
                    player.shootAction()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s or event.key == pygame.K_f:
                    player.delta_move_x = 0
                if event.key == pygame.K_e or event.key == pygame.K_d:
                    player.delta_move_y = 0



        player.x += player.delta_move_x
        player.y += player.delta_move_y

        zombie.move(Wall.walls, player.x, player.y)
        # zombie.moveRight(5, .5)

        player.draw(player.delta_move_x, player.delta_move_y, Wall.walls)
        player.update_projectile()

        for wall in Wall.walls:
            pygame.draw.rect(screen, BLACK, wall.rect)


        pygame.display.update()



if __name__ == '__main__':
    Game()
