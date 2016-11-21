# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:12:46 2016

@author: PET3RtheGreat
"""
import pygame as pg
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.pos = vec(WIDTH // 2, HEIGHT // 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.mass = PLAYERMASS

    def jump(self):
        # jump only if standing on a platform
        self.rect.x += 1
#        false means the sprite is not deleted upon collision
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_d]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH - 15:
            self.pos.x = WIDTH - 15
        if self.pos.x < 15:
            self.pos.x = 15

        self.rect.midbottom = self.pos


class bullet(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.mass = BULLMASS

    def getTarget(self):
        cur = pg.mouse.get_pos()
        xdiff = cur[0] - self.rect.x
        ydiff = cur[1] - self.rect.y
        self.xmove = xdiff
        self.ymove = ydiff
        self.rect.x = self.xmove
        self.rect.y = self.ymove


#    def __init__(self, game, pos, dir):
#        self.groups = game.all_sprites
#        pg.sprite.Sprite.__init__(self, self.groups)
#        self.image = pg.Surface((10,10))
#        self.rect = self.image.get_rect()
#
#
#    def update(self):
'''        need to figure out a way to shoot the bullet towards where the cursor is
    meaning that the x and y velocity values cannot be numbers, but must instead
    be functions?
    Not sure if i can use vector?
    Then mass needs to be added so that it can interfere with a gravitational field'''


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
