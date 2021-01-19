import pygame as pg
import pytmx
from settings import *


def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f: # read in the text from specified text file
            for line in f:
                self.data.append(line.strip()) #appends each line from the text file to a list. strip() is used to get rid of "\n"

        self.tilewidth = len(self.data[0]) #number of characters in each row is the number of tiles wide
        self.tileheight = len(self.data) #number of rows in the list is the bumber of tiles tall
        self.width = self.tilewidth * TILESIZE 
        self.height = self.tileheight * TILESIZE  #size of width and height in pixels

class TiledMap:
    def __init__(self, filename):
        print(filename)
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        

    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))
    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

class Camera: #camera is the section of the map that can be seen on screen
    def __init__(self, width, height): #width and height will be that of the entire map
        self.camera = pg.Rect(0, 0, width, height) #initializing the camera at the top left of map as a rect
        self.width = width   #camera rect attributes
        self.height = height

    def apply(self, entity): 
        return entity.rect.move(self.camera.topleft) #moves any object/sprite any offset between the camera rect and the top left position on map

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)
        
    def update(self, target): #updates the coordinates of the camera to follow the player sprite
        
        x = -target.rect.x + int(WIDTH / 2) # if the player moves in one direction, camera is offsetted the same amount in opposite direction
        y = -target.rect.y + int(HEIGHT / 2) # We also add half the height and width of camera to coordinates to keep player centered in it
        #self.camera = pg.Rect(x, y, self.width, self.height) #apply the new coordinates to the camera rect
       
        # Map Scrolling Limits:
        # min function chooses the smallest number between 0 and x.
        x = min(0, x)  # Ensures camera is within left boundary of map 
        y = min(0, y)  # Ensures camera is within bottom boundary of map 
        x = max(-(self.width - WIDTH), x)  # Ensures camera is within right boundary of map 
        y = max(-(self.height - HEIGHT), y)  # Ensures camera is within left boundary of map 
        self.camera = pg.Rect(x, y, self.width, self.height) #apply the new coordinates to the camera rect 


