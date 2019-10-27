import pygame


class Player(object):

    BLACK = 0,0,0

    screen = ''

    def __init__(self, x, y, color=(0,0,0)):
        self.x = x
        self.y = y

        self.delta_move_x = 0
        self.delta_move_y = 0
        self.direction = 'up'
        self.triangle = ((self.x + 5, self.y), (self.x, self.y - 15), (self.x - 5, self.y))

        self.rect_h = 30
        self.rect_w = 30

        self.rect = pygame.Rect(self.x -15, self.y - 15, self.rect_w, self.rect_h)

        self.shoot = False
        self.pewDict = {}

        self.color = color

        self.col_detect = False





    def draw(self, dx, dy, walls):



        if self.direction == 'left':
            self.triangle = ((self.x, self.y - 5), (self.x - 15, self.y), (self.x, self.y + 5))
        elif self.direction == 'up':
            self.triangle = ((self.x + 5, self.y), (self.x, self.y - 15), (self.x - 5, self.y))
        elif self.direction == 'right':
            self.triangle = ((self.x, self.y - 5), (self.x +15, self.y), (self.x, self.y + 5))
        elif self.direction == 'down':
            self.triangle = ((self.x + 5, self.y), (self.x, self.y + 15), (self.x - 5, self.y))
        else:
            # print('direction not set')
            pass

        if dx !=0:
            self.collision(dx, dy, walls)
        if dy !=0:
            self.collision(dx, dy, walls)

        self.player = pygame.draw.polygon(Player.screen, self.color, self.triangle)
        self.drawRect = pygame.draw.rect(Player.screen, self.color, self.rect, 1)



    def collision(self, dx, dy, walls):

        self.rect.x += dx
        self.rect.y += dy

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                # self.col_detect = True

                if self.delta_move_x > 0:
                    self.rect.right = wall.rect.left
                if self.delta_move_x < 0:
                    self.rect.left = wall.rect.right
                if self.delta_move_y > 0:
                    self.rect.bottom = wall.rect.top
                if self.delta_move_y < 0:
                    self.rect.top = wall.rect.bottom

                self.x = self.rect.x +15
                self.y = self.rect.y +15


    def shootAction(self):

        pew = 'pew' + str(len(self.pewDict))

        if self.direction == 'left':
            pew_1 = self.y
            pew_2 = self.x
            pew_3 = self.x - 10

        elif self.direction == 'up':

            pew_1 = self.x
            pew_2 = self.y
            pew_3 = self.y - 10

        elif self.direction == 'right':

            pew_1 = self.y
            pew_2 = self.x
            pew_3 = self.x + 10

        elif self.direction == 'down':

            pew_1 = self.x
            pew_2 = self.y
            pew_3 = self.y + 10

        else:
            print('issue with shootAction')


        # pew_1 = self.x
        # pew_2 = self.y
        # pew_3 = pew_y_1 - 10

        self.pewDict[pew] = [eval('pew_1'), eval('pew_2'), eval('pew_3'), eval('self.direction')]

        self.shoot = False


    def update_projectile(self):
        for key, value in self.pewDict.items():

            if value[3] == 'left':
                pygame.draw.line(Player.screen, Player.BLACK, (value[1], value[0]), (value[2], value[0]), 2)
                value[1] -= .5
                value[2] -= .5
            if value[3] == 'up':
                pygame.draw.line(Player.screen, Player.BLACK, (value[0], value[1]), (value[0], value[2]), 2)
                value[1] -= .5
                value[2] -= .5
            elif value[3] == 'right':
                pygame.draw.line(Player.screen, Player.BLACK, (value[1], value[0]), (value[2], value[0]), 2)
                value[1] += .5
                value[2] += .5
            elif value[3] == 'down':
                pygame.draw.line(Player.screen, Player.BLACK, (value[0], value[1]), (value[0], value[2]), 2)
                value[1] += .5
                value[2] += .5





