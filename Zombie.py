import pygame
import sys
import time


class Zombie(object):

    screen = ""

    def __init__(self, color, coordinates):
        self.screen = Zombie.screen
        self.color = color
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.w = coordinates[2]
        self.h = coordinates[3]

        self.delta_move_x = 0
        self.delta_move_y = 0

        self.coordinates = [self.x, self.y, self.w, self.h]

        self.timeDifference = 0
        self.timeDiff = .5

        self.oldTime = time.time()
        self.switch = True
        self.switch2 = True

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        self.dx = 0

        self.blocked = True

    def draw(self):
        self.bg = pygame.draw.rect(Zombie.screen, self.color, self.rect)



    def move(self, walls, player_x, player_y):
        self.draw()
        wallCount = 0
        if self.timeDifference > self.timeDiff:
            self.rect.x += self.dx
            self.oldTime = time.time()
            self.timeDifference = 0
            for wall in walls:
                if wall.rect.x < player_x and wall.rect.y >  player_y-10 and wall.rect.y < player_y + 10:
                    wallCount +=1

                if wall.rect.x > player_x and wall.rect.y > player_y-10 and wall.rect.y < player_y + 10:
                    wallCount += 1

                if self.rect.colliderect(wall.rect):
                    self.dx = -self.dx

            if wallCount > 1:
                self.blocked = True
            else:
                self.blocked = False

            self.charge(player_x, self.blocked)


        else:
            currentTime = time.time()
            self.timeDifference = currentTime - self.oldTime



    def charge(self, player, blocked):

        if self.dx < 0 and blocked == True and player < self.rect.x:
            self.timeDiff = .1
        elif self.dx > 0 and blocked == True and player > self.rect.x:
            self.timeDiff = .1
        else:
            self.timeDiff = 1


    # def zigZag(self):
    #     if self.coordinates[0] > 325:
    #         self.switch = False
    #     elif self.coordinates[0] < 225:
    #         self.switch = True
    #
    #     if self.switch == True:
    #         self.moveRight(10, .5)
    #     else:
    #         self.moveLeft(10, .5)
    #
    #     if self.switch != self.switch2:
    #         self.coordinates[1] += 10
    #         self.switch2 = self.switch


