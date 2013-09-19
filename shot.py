#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *

BULLET_WIDTH = 4
BULLET_HEIGHT = 4
BULLET_COLOR = "#FF6262"
BULLET_SPEED = 20

 
class Shot(sprite.Sprite):
    def __init__(self, pos, direction):
        sprite.Sprite.__init__(self)
        self.direction = direction 
        self.image = Surface((BULLET_WIDTH, BULLET_HEIGHT))
        self.image.fill(Color(BULLET_COLOR))
        self.rect = self.image.get_rect(midbottom=pos) #Rect(pos, BULLET_WIDTH, BULLET_WIDTH)

    def update(self, platforms):
        self.rect.move_ip(BULLET_SPEED * self.direction, 0)
        for p in platforms:
            if sprite.collide_rect(self, p): # если есть пересечение с пулей
               Explosion(self)
               self.kill()



class Explosion(sprite.Sprite):
    defaultlife = 12
    animcycle = 3
    images = []
    def __init__(self, actor):
        sprite.Sprite.__init__(self)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = self.defaultlife

    def update(self):
        self.life = self.life - 1
        self.image = self.images[self.life//self.animcycle%2]
        if self.life <= 0: self.kill()
