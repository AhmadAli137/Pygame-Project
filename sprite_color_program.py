from PIL import Image

#import sys  
from os import path
from sprites import *
import shutil
from Game_Reset import *

class sprite_color():
    def __init__(self): 


        self.SpriteReset = ResetSprite()
                     #[[dark brown], [peach],      [light brown] 
        self.skin_colors = [(90, 60, 0), (255,191,130), (156, 110, 0)]

        #  [horizontal start, h.end, vertical start, v. end] 
        self.hair_pixels = [[4,20,0,4],[0,24,4,8],[0,12,8,12],[20,24,8,12],[0,4,12,16]]

        self.skin_pixels = [[12,20,8,12],[8,16,12,16],[20,24,12,16],[0,24,16,24], [8,16,24,28],[0,4,32,40],[20,24,32,40]]


    def change_hair(self,colorTuple): 
        self.load_player_data()
        self.colorCounter=-1
        for sprite in self.WalkDown_raw:
            self.pixels = sprite.load()
            self.colorCounter += 1
            for i in self.hair_pixels:
                for j in range(i[0],i[1]):
                    for k in range(i[2],i[3]):
                        self.pixels[j,k] = colorTuple
                        sprite.save(r'sprites\\Temp Sprite\\WalkDown\\sprite_'+str(self.colorCounter)+".png")
        
    

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
