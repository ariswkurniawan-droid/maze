from pygame import *
from random import randint

win_width =  1000
win_height = 700
#Game scene:
window = display.set_mode((win_width, win_height))
display.set_caption('WLECOMA BAKC GESAH!')
background = transform.scale(image.load('background.jpg'), (win_width, win_height))

#music

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.1)
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')


class Game(sprite.Sprite):
    #class constructor
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        #every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed

        #every sprite must have the rect property - the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#heir class for the player sprite (controlled by arrows)
class Player(Game):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 70:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 70:
            self.rect.y += self.speed
#        if keys[K_q] 
#

class Enemy(Game):
    side = 'left'
    def hor_update(self):
        if self.rect.x <= 10:
            self.side = 'right'
        if self.rect.x >= win_width - 20:
            self.side = 'left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

    side = 'down'
    def ver_update(self):
        if self.rect.y <= 10:
            self.side = 'down'
        if self.rect.y >= win_width - 20:
            self.side = 'up'
        if self.side == 'down':
            self.rect.y = self.speed
        else:
            self.rect.y -= self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color = (color_1, color_2, color_3)
        self.width = wall_width
        self.height = wall_height

        self.image = Surface([self.width, self.height])
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    
    def draw_wall(self):
        draw.rect(window, self.color, (self.rect.x,self.rect.y,self.width,self.height))
        #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmoooooooooooooooooooooooooooooooooooooogggggggggggggggggggguuuuuuuuuuuusssssss

#Game characters:
packman = Player('hero.png', 5, win_height - 80, 8)
monster1 = Enemy('cyborg.png', win_width - 80, 280, 15)
monster2 = Enemy('cyborg.png', win_width - 80, 100, 10)
monster3 = Enemy('cyborg.png', win_width - 80, 400, 20)

random_number1 = randint(0,255)
random_number2 = randint(0,255)
random_number3 = randint(0,255)

w1 = Wall(random_number1,random_number2,random_number3, 100,20,450,10)
w2 = Wall(random_number1,random_number2,random_number3, 100,480,350,10)
w3 = Wall(random_number1,random_number2,random_number3, 100,20,10,380)
w4 = Wall(random_number1,random_number2,random_number3, 350,100,10,390)


final = Game('treasure.png', win_width - 120, win_height - 80, 0)

font.init()
font = font.Font(None, 200)
# custom font
# font 2 = font.SysFont('Arial', 36)
win = font.render('YOU WIN!!', True, (255,215,0))
lose = font.render('YOU LOSE!', True, (180,0,0))


#game loop
run = True
clock = time.Clock()
FPS = 60
finish = False

while run:
    # .blit itu fungsinya untuk menempel gambar ke layar
    #uwaw
    
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.blit(background,(0,0))
        packman.update()
        monster1.hor_update()
        monster2.hor_update()
        monster3.hor_update()

        packman.draw()
        monster1.draw()
        monster2.draw()
        monster3.draw()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()

        final.draw()
        c1 = sprite.collide_rect(packman,monster1)
        c2 = sprite.collide_rect(packman,monster2)
        c3 = sprite.collide_rect(packman,monster3)
        c4 = sprite.collide_rect(packman, w1)
        c5 = sprite.collide_rect(packman, w2)
        c6 = sprite.collide_rect(packman, w3)
        c7 = sprite.collide_rect(packman, w4)

        conditions = [c1,c2,c3,c4,c5,c6,c7]

        #lose con
        for condition in conditions:
            if condition:
                finish = True
                window.blit(lose,(250,win_height/2))
                kick.play()
    
        #win con
        if sprite.collide_rect(packman,final):
            finish = True
            window.blit(win,(250,win_height/2))
            money.play()

    display.update()
    clock.tick(FPS)


#       YEEEEEEEEEEEEEEEEEE
# 
# 
#                                                                      |         |
#                                                                      |         |
#                                                                      |         |
#                                                                      |         |
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 





























































