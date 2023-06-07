#создай игру "Лабиринт"!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        pressed = key.get_pressed()
        if pressed[K_d] and self.rect.x < 630:
            self.rect.x += self.speed
        if pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if pressed[K_s] and self.rect.y < 430:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 450:
            self.direction = 'right'
        if self.rect.x >= 620:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


w = 700
h = 500

hero = GameSprite('hero.png', 35, h - 80, 4)
cyborg = GameSprite('cyborg.png', w - 80, 300, 3)
treasure = GameSprite('treasure.png', w - 120, h - 80, 0)

first = Wall(123, 123, 0, 10, 10, 680, 10)
second = Wall(123, 123, 0, 10, 10, 10, 500)
third = Wall(123, 123, 0, 110, 110, 10, 90)
fourth = Wall(123, 123, 0, 110, 110, 150, 10)
fifth = Wall(123, 123, 0, 110, 300, 10, 200)
sixth = Wall(123, 123, 0, 110, 300, 150, 10)
seventh = Wall(123, 123, 0, 110, 200, 150, 10)
eighth = Wall(123, 123, 0, 360, 10, 10, 150)
nineth = Wall(123, 123, 0, 440, 260, 10, 130)
one = Wall(123, 123, 0, 260, 300, 10, 190)
two = Wall(123, 123, 0, 260, 490, 250, 10)
three = Wall(123, 123, 0, 360, 390, 150, 10)
four = Wall(123, 123, 0, 510, 390, 10, 110)
five = Wall(123, 123, 0, 360, 260, 150, 10)
six = Wall(123, 123, 0, 260, 200, 10, 110)
seven = Wall(123, 123, 0, 510, 120, 10, 150)
eight = Wall(123, 123, 0, 680, 10, 10, 490)

font.init()
font = font.SysFont('Arial', 70)
win = font.render('ТЫ ПОБЕДИЛ!!!', True, (0, 215, 0))
lose = font.render('ТЫ ПРОИГРАЛ :(', True, (215, 0, 0))

window = display.set_mode((w, h))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'), (w, h))
mixer.init()
mixer.music.load('jungles.ogg')
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')
mixer.music.play()
game = True
finish = False

clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        first.draw_wall()
        second.draw_wall()
        third.draw_wall()
        fourth.draw_wall()
        fifth.draw_wall()
        sixth.draw_wall()
        seventh.draw_wall()
        eighth.draw_wall()
        nineth.draw_wall()
        one.draw_wall()
        two.draw_wall()
        three.draw_wall()
        four.draw_wall()
        five.draw_wall()
        six.draw_wall()
        seven.draw_wall()
        eight.draw_wall()
        hero.reset()
        cyborg.reset()
        treasure.reset()
        Player.update(hero)
        Enemy.update(cyborg)
    if sprite.collide_rect(hero, cyborg) or sprite.collide_rect(hero, first) or sprite.collide_rect(hero, second) or sprite.collide_rect(hero, third) or sprite.collide_rect(hero, fourth) or sprite.collide_rect(hero, fifth) or sprite.collide_rect(hero, sixth) or sprite.collide_rect(hero, seventh) or sprite.collide_rect(hero, eighth) or sprite.collide_rect(hero, nineth) or sprite.collide_rect(hero, one) or sprite.collide_rect(hero, two) or sprite.collide_rect(hero, three) or sprite.collide_rect(hero, four) or sprite.collide_rect(hero, five) or sprite.collide_rect(hero, six) or sprite.collide_rect(hero, seven) or sprite.collide_rect(hero, eight):
        finish = True
        window.blit(lose, (150, 220))
        kick.play()
    if sprite.collide_rect(hero, treasure):
        finish = True
        window.blit(win, (150, 220))
        money.play()
    display.update()
    clock.tick(FPS)
