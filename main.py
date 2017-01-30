# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 20:49:25 2016

@author: Peter Kyriakopoulos
"""
import numpy as np
import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def shoot(self):
        self.bullet = bullet(self)
        self.all_sprites.add(self.bullet)
        cur = pg.mouse.get_pos()
        xdiff = self.player.rect.x - cur[0] 
        ydiff = self.player.rect.y - cur[1]
        self.bullet.xmove = xdiff
        self.bullet.ymove = ydiff
        self.bullet.rect.x = self.bullet.xmove
        self.bullet.rect.y = self.bullet.ymove

#    def gravity(BULLMASS,mass, xdif, ydif):
##        mass is the mass of the bullet
##       xdif and ydif are the distance of the bullet from the gravitational field
#        g = 10
        
#        force = (g * BULLMASS * mass*BulletPositionVector)//(np.linalg.norm(BulletPositionVector))**3
#        Bullet position Vector would be the position of the bullet at any given time (assuming we get it as a matrix that would 
#        be the way to create the field, in a way that only interacts with the bullets)
        '''gravitational constant, not actual value, but the one that will give the best performance gameplay wise
        f = g*(gravity.mass*bullet.mass)//(xdif,ydif)
        The graviational field will have to have a mass of its own, if this formula is to be used
        unless the formula F = ma is used, in which case an acceleration will have to be given to the bullet'''


    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
        mouse = pg.mouse.get_pressed()
        if mouse[0]:
            print("Bang!")
            self.shoot()
#        if self.player.vel.y < 0:
#            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
#            if hits:
#                self.player.pos.y = hits[0].rect.bottom
#                self.player.vel.y = 0
        '''Still trying to figure out how to detect collision on all sides of the blocks'''

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.player.jump()
#            if event.type == pg.MOUSEBUTTONDOWN:
#                bullet.rect.x = Player.rect.x
#                bullet.rect.y = Player.rect.y
#                all_sprites.add(bullet)
#                all_sprite.update()
#'''needs reworking, once i get the movement to work'''
    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)

        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
