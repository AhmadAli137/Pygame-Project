#importing important libraries:
from PIL import Image
from os import path
import os
import pygame as pg
from settings import *
from tilemap1 import collide_hit_rect
vec = pg.math.Vector2 #used to make vectors
from Game_Reset import *


'''def NPC_Bubble(sprite, group, dir):
    hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
    print(hits)'''


def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y

class Player(pg.sprite.Sprite): #creating a class for making players
    def __init__(self, game, x, y):  #Initializing method uses 3 parameters:
        #                             game--> gives access to the self data from "new" function in the "Game" class in main.py 
        #                             x --> x-coordinate in game grid
        #                             y --> y-coordinate in game grid

        self.SpriteReset = ResetSprite()
        self.groups = game.all_sprites #grabbing the chracter sprite container class from "Game" class in main.py
        pg.sprite.Sprite.__init__(self, self.groups) #initializing a player sprite
        self.game = game
        self.image = game.player_img

        #self.image = pg.Surface((TILESIZE, TILESIZE)) #creating the player sprite image using dimensions from settings.py
        #self.image.fill(YELLOW) #making the player sprite yellow
        self.rect = self.image.get_rect() #creating a rect object for the player sprite
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0) # initial x & y velocity of player sprite
        self.pos = vec(x, y) #storing the x & y grid coordinates where player sprite spawns

        self.PrevMove = "WalkDown"
        self.MoveCounter = 2
        self.Move_initializer = 0

                     #[[dark brown], [peach],      [light brown] 
        '''self.skin_colors = [(90, 60, 0), (255,191,130), (156, 110, 0)]

        #  [horizontal start, h.end, vertical start, v. end] 
        self.hair_pixels = [[4,20,0,4],[0,24,4,8],[0,12,8,12],[20,24,8,12],[0,4,12,16]]

        self.skin_pixels = [[12,20,8,12],[8,16,12,16],[20,24,12,16],[0,24,16,24], [8,16,24,28],[0,4,32,40],[20,24,32,40]]'''
        self.load_player_data()
        
    
        
    '''def change_hair(self,colorTuple): 
        self.colorCounter=-1
        for sprite in WalkDown_raw:
            self.pixels = sprite.load()
            self.colorCounter += 1
            for i in self.hair_pixels:
                for j in range(i[0],i[1]):
                    for k in range(i[2],i[3]):
                        self.pixels[j,k] = colorTuple
                        sprite.save(r'sprites\\Temp Sprite\\WalkDown\\sprite_'+str(self.colorCounter)+".png")'''
        
    def move(self, dx=0, dy=0): #creating a class for moving sprite objects
    #                            dx and dy are automatically 0 if not defined when this function is called upon

        if not self.collide_with_walls(dx, dy): #check to see if new position overlaps with a wall object
            self.x += dx 
            self.y += dy  # dx and dy are the amounts by which the sprite will move along x/y grid coordinates
            #print(self.x +", "+self.y)

    def get_keys(self): #function to handle player movement when arrow keys are pressed
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        #if self.game.space_toggle == False and self.game.current_dialogue == "":#=================================
        #if self.game.current_dialogue == "":#=================================
        if self.game.dialogue_toggle == False:
            self.Move_initializer += 1
            if self.Move_initializer <3:
                self.MoveCounter += 1
                if self.MoveCounter >5:
                    self.MoveCounter = 0
            else:
                self.Move_initializer=0

        

            if keys[pg.K_LEFT] or keys[pg.K_a]:
                
                if keys[pg.K_SPACE]:
                    self.vel.x = -PLAYER_RUN_SPEED
                    self.image = self.RunLeft[self.MoveCounter]
                else:
                    self.vel.x = -PLAYER_SPEED
                    self.image = self.WalkLeft[self.MoveCounter]
                self.PrevMove = "WalkLeft"
            #====================================================

            if keys[pg.K_RIGHT] or keys[pg.K_d]:
                if keys[pg.K_SPACE]:
                    self.vel.x = PLAYER_RUN_SPEED
                    self.image = self.RunRight[self.MoveCounter]
                else:
                    self.vel.x = PLAYER_SPEED
                    self.image = self.WalkRight[self.MoveCounter]
                self.PrevMove = "WalkRight"

            #====================================================
            if keys[pg.K_UP] or keys[pg.K_w]:
                if keys[pg.K_SPACE]:
                    self.vel.y = -PLAYER_RUN_SPEED
                    self.image = self.RunUp[self.MoveCounter]
                else:
                    self.vel.y = -PLAYER_SPEED
                    self.image = self.WalkUp[self.MoveCounter]
                self.PrevMove = "WalkUp"

            #====================================================
            if keys[pg.K_DOWN] or keys[pg.K_s]:
                if keys[pg.K_SPACE]:
                    self.vel.y = PLAYER_RUN_SPEED
                    self.image = self.RunDown[self.MoveCounter]
                else:
                    self.vel.y = PLAYER_SPEED
                    self.image = self.WalkDown[self.MoveCounter]
                    #self.image = SarkerWalkDown[self.MoveCounter]
                self.PrevMove = "WalkDown"

            #====================================================
            #if both the x and y velocity is non-zero, object is moving diagonally
            # We want to make sure that the diagonal velocity = 1
            # Pythagorean theorem: a^2 +b^2 = c^2 ; we want c = 1 and b=a
            # 1 = sqrt(2a^2) --> 1 = 2a^2 --> a = sqrt(1/2) = 0.7071
            #====================================================

            if keys[pg.K_LEFT] and keys[pg.K_UP]:
                if keys[pg.K_SPACE]:
                    self.vel.x = -PLAYER_RUN_SPEED*0.7071
                    self.vel.y = -PLAYER_RUN_SPEED*0.7071
                    self.image = self.RunLeftUp[self.MoveCounter]
                else:
                    self.vel.x = -PLAYER_SPEED*0.7071
                    self.vel.y = -PLAYER_SPEED*0.7071
                    self.image = self.WalkLeftUp[self.MoveCounter]  
                self.PrevMove = "WalkLeft"

            #====================================================
            if keys[pg.K_RIGHT] and keys[pg.K_UP]:
                if keys[pg.K_SPACE]:
                    self.vel.x = PLAYER_RUN_SPEED*0.7071
                    self.vel.y = -PLAYER_RUN_SPEED*0.7071
                    self.image = self.RunRightUp[self.MoveCounter]
                else:
                    self.vel.x = PLAYER_SPEED*0.7071
                    self.vel.y = -PLAYER_SPEED*0.7071
                    self.image = self.WalkRightUp[self.MoveCounter]
                self.PrevMove = "WalkRight"

            #====================================================
            if keys[pg.K_LEFT] and keys[pg.K_DOWN]:
                if keys[pg.K_SPACE]:
                    self.vel.x = -PLAYER_RUN_SPEED*0.7071
                    self.vel.y = PLAYER_RUN_SPEED*0.7071
                    self.image =self.RunLeftDown[self.MoveCounter]
                else:
                    self.vel.x = -PLAYER_SPEED*0.7071
                    self.vel.y = PLAYER_SPEED*0.7071
                    self.image = self.WalkLeftDown[self.MoveCounter]
                self.PrevMove = "WalkLeft"

            #====================================================
            if keys[pg.K_RIGHT] and keys[pg.K_DOWN]:
                if keys[pg.K_SPACE]:
                    self.vel.x = PLAYER_RUN_SPEED*0.7071
                    self.vel.y = PLAYER_RUN_SPEED*0.7071
                    self.image = self.RunRightDown[self.MoveCounter]
                else:
                    self.vel.x = PLAYER_SPEED*0.7071
                    self.vel.y = PLAYER_SPEED*0.7071
                    self.image = self.WalkRightDown[self.MoveCounter]
                self.PrevMove = "WalkRight"
                #====================================================
            if not keys[pg.K_LEFT] and not keys[pg.K_RIGHT] and not keys[pg.K_UP] and not keys[pg.K_DOWN]:
                if self.PrevMove == "WalkDown":
                    self.image = self.WalkDown[2]

                if self.PrevMove == "WalkUp":
                    self.image = self.WalkUp[2]

                if self.PrevMove == "WalkRight":
                    self.image = self.WalkRight[2]

                if self.PrevMove == "WalkLeft":
                    self.image = self.WalkLeft[2]
        else:
            self.PrevMove =self.PrevMove
            if self.PrevMove == "WalkDown":
                self.image = self.WalkDown[2]

            if self.PrevMove == "WalkUp":
                self.image = self.WalkUp[2]

            if self.PrevMove == "WalkRight":
                self.image = self.WalkRight[2]

            if self.PrevMove == "WalkLeft":
                self.image = self.WalkLeft[2]



           
            
        


            
    def collide_with_walls(self, dir): #function for when player sprite collides with wall sprite
        if dir == 'x': 
            hits = pg.sprite.spritecollide(self, self.game.walls, False) #determines if their are any collisions with wall sprites
            NPC_hits = pg.sprite.spritecollide(self, self.game.NPCs, False) #determines if their are any collisions with NPC's
            if hits or NPC_hits:
                if self.vel.x > 0: #if sprite moving right
                    self.pos.x = hits[0].rect.left - self.rect.width #sets the sprite position so that it 
                    #                                                 presses directly on the left side of the wall it has collided with
                if self.vel.x < 0: #if sprite moving left
                    self.pos.x = hits[0].rect.right#sets the sprite position so that it 
                    #                                         presses directly on the right side of the wall it has collided with

                self.vel.x = 0 #stops the sprite from moving in x-direction
                self.rect.x = self.pos.x #updates player rect x-position




        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            NPC_hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits or NPC_hits:
                if self.vel.y > 0: #if sprite moving down
                    self.pos.y = hits[0].rect.top - self.rect.height #sets the sprite position so that it
                    #                                           presses directly against the top of the wall it has collided with

                if self.vel.y < 0: #if sprite moving up
                    self.pos.y = hits[0].rect.bottom #sets the sprite position so that it
                    #                                  presses directly against the bottom of the wall it has collided with

                self.vel.y = 0 #stops the sprite from moving in y-direction
                self.rect.y = self.pos.y #updates player rect y-position




            

    def update(self):
        self.get_keys()
        if self.game.dialogue_toggle == True:
            self.pos = self.pos
        else:
            self.pos += self.vel * self.game.dt#updates the x & y pixel position of the player
                                           #uses physics concept to determine how much the player moved with each time step [v=d/t --> d=v*t]
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x') #checks to see if there are any collisions in x-direction
        collide_with_walls(self, self.game.NPCs, 'x')


        
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        collide_with_walls(self, self.game.NPCs, 'y')
  

        self.rect.center = self.hit_rect.center

    def load_player_data(self):
        self.WalkUp =[]
        self.WalkUp_raw =[]
        for filename in os.listdir(self.SpriteReset.WalkUpFolder):
            self.image = Image.open(path.join(self.SpriteReset.WalkUpFolder, filename))
            self.pg_image = pg.image.load(path.join(self.SpriteReset.WalkUpFolder, filename))
            self.WalkUp.append(self.pg_image)
            self.WalkUp_raw.append(self.image)
            

        self.WalkDown =[]
        self.WalkDown_raw =[]
        for filename in os.listdir(self.SpriteReset.WalkDownFolder):
            self.image = Image.open(path.join(self.SpriteReset.WalkDownFolder, filename))
            self.pg_image = pg.image.load(path.join(self.SpriteReset.WalkDownFolder, filename))
            self.WalkDown.append(self.pg_image)
            self.WalkDown_raw.append(self.image)


        self.WalkRight =[]
        for filename in os.listdir(self.SpriteReset.WalkRightFolder):
            self.pg_image = pg.image.load(path.join(self.SpriteReset.WalkRightFolder, filename))
            self.WalkRight.append(self.pg_image)

        self.WalkLeft =[]
        for filename in os.listdir(self.SpriteReset.WalkLeftFolder):
            self.pg_image = pg.image.load(path.join(self.SpriteReset.WalkLeftFolder, filename))
            self.WalkLeft.append(self.pg_image)

        self.WalkRightUp =[]
        for filename in os.listdir(self.SpriteReset.WalkRightUpFolder):
            self.pg_image = pg.image.load(path.join(self.SpriteReset.WalkRightUpFolder, filename))
            self.WalkRightUp.append(self.pg_image)

        self.WalkLeftUp =[]
        for filename in os.listdir(self.SpriteReset.WalkLeftUpFolder):
            self.pg_image = pg.image.load(path.join(self.SpriteReset.WalkLeftUpFolder, filename))
            self.WalkLeftUp.append(self.pg_image)

        self.WalkRightDown =[]
        for filename in os.listdir(self.SpriteReset.WalkRightDownFolder):
            self.pg_image = pg.image.load(path.join(self.SpriteReset.WalkRightDownFolder, filename))
            self.WalkRightDown.append(self.pg_image)

        self.WalkLeftDown =[]
        for filename in os.listdir(self.SpriteReset.WalkLeftDownFolder):
            self.pg_image = pg.image.load(path.join(self.SpriteReset.WalkLeftDownFolder, filename))
            self.WalkLeftDown.append(self.pg_image)

        self.SarkerWalkDown =[]
        for filename in os.listdir(self.SpriteReset.SarkerWalkDownFolder):
            self.pg_image = pg.image.load(path.join(self.SpriteReset.SarkerWalkDownFolder, filename))
            self.SarkerWalkDown.append(self.pg_image)

        #==========================================================================================
        self.RunUp =[]
        for filename in os.listdir(self.SpriteReset.RunUpFolder):
            self.pg_image = pg.image.load(path.join(self.SpriteReset.RunUpFolder, filename))
            self.RunUp.append(self.pg_image)

        self.RunDown =[]
        for filename in os.listdir(self.SpriteReset.RunDownFolder):
            self.pg_image = pg.image.load(path.join(self.SpriteReset.RunDownFolder, filename))
            self.RunDown.append(self.pg_image)

        self.RunRight =[]
        for filename in os.listdir(self.SpriteReset.RunRightFolder):
            self.pg_image = pg.image.load(path.join(self.SpriteReset.RunRightFolder, filename))
            self.RunRight.append(self.pg_image)

        self.RunLeft =[]
        for filename in os.listdir(self.SpriteReset.RunLeftFolder):
            self.pg_image = pg.image.load(path.join(self.SpriteReset.RunLeftFolder, filename))
            self.RunLeft.append(self.pg_image)

        self.RunRightUp =[]
        for filename in os.listdir(self.SpriteReset.RunRightUpFolder):
            self.pg_image = pg.image.load(path.join(self.SpriteReset.RunRightUpFolder, filename))
            self.RunRightUp.append(self.pg_image)

        self.RunLeftUp =[]
        for filename in os.listdir(self.SpriteReset.RunLeftUpFolder):
            self.pg_image = pg.image.load(path.join(self.SpriteReset.RunLeftUpFolder, filename))
            self.RunLeftUp.append(self.pg_image)

        self.RunRightDown =[]
        for filename in os.listdir(self.SpriteReset.RunRightDownFolder):
            self.pg_image = pg.image.load(path.join(self.SpriteReset.RunRightDownFolder, filename))
            self.RunRightDown.append(self.pg_image)

        self.RunLeftDown =[]
        for filename in os.listdir(self.SpriteReset.RunLeftDownFolder):
            self.pg_image = pg.image.load(path.join(self.SpriteReset.RunLeftDownFolder, filename))
            self.RunLeftDown.append(self.pg_image)

   


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class NPC(pg.sprite.Sprite):
    def __init__(self, game, name, x, y, w, h):
        
        self.name = name
        self.image_string = "Sprites\\NPCs\\"+self.name+".png"
        self.image = pg.image.load(self.image_string)
        self.groups = game.NPCs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.w = w
        self.h =h
        self.rect.x = x
        self.rect.y = y
        self.Bubble_toggle = False