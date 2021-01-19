#Importing important libraries:
import pygame as pg
import sys  
from os import path
from settings import *
from sprites import *
from Game_Reset import *
from tilemap1 import *   
from StartScreen import *     
from Dialogue import *  
     

class Game:
    def __init__(self): #initializing game class
        print(WIDTH, HEIGHT)

        self.SpriteReset = ResetSprite()
        self.SpriteReset.delete_cache()
        self.SpriteReset.reset_sprite()

        pg.init() #initialize pygame
        pg.font.init()
        self.NPC_list = ["NPC_red","NPC_green","NPC_blue"]
     
        self.screen = pg.display.set_mode((WIDTH, HEIGHT),pg.FULLSCREEN) #creating a screen using parameters from settings.py
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock() #clock used to keep track of time
        pg.key.set_repeat(500, 500) #while a key is held down, there is 500 ms delay until the first repeat, 
                                    #                          and 500 ms delay between every other repeat
        self.load_data() #call load_data function
        

    def load_data(self):
        self.game_folder =""
        #self.game_folder = path.dirname(__file__) #game folder is the folder this program is currently located in
        map_folder = path.join(self.game_folder, 'maps') #locating map folder
        
        self.map = TiledMap(path.join(map_folder, 'WindsorBig.tmx')) #locates Tiled map and turns it into an object of the class
        
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(r'sprites\\Premade Sprite\\WalkDown\\sprite_2.png').convert_alpha()

        self.font = pg.font.Font(r'thin-pixel-7-font\\ThinPixel7.ttf', 55)
        self.title = self.font.render(("Don't Come to My House"), True, BLACK)
        self.scripts = dialogue(self)
        #self.dialogue_rect = pg.Rect(10,HEIGHT-130,WIDTH-20,120)
        self.dialogue_rect = pg.Surface((WIDTH-20,120), pg.SRCALPHA)
        self.dialogue_rect.fill((100, 100, 100, 220))    
        



        


    def new(self): # setting up a new game:
        
        self.all_sprites = pg.sprite.Group() #creating a container class to store character Sprites.
        self.walls = pg.sprite.Group() #creating a container class to store wall Sprites.
        self.NPCs = pg.sprite.Group() #creating a container class to store NPC Sprites.

        for tile_object in self.map.tmxdata.objects: #searching through objects belong to the tmx file
            if tile_object.name == 'Player':
                self.player = Player(self, tile_object.x, tile_object.y) #creating a new player object
           
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y,tile_object.width, tile_object.height) #creating a new wall object

            
            if tile_object.name in self.NPC_list:
                NPC(self, tile_object.name, tile_object.x, tile_object.y,tile_object.width, tile_object.height) #creating an NPC
        
        self.camera = Camera(self.map.width, self.map.height) #spawning the game camera using the map dimensions

        self.draw_debug = False
        self.bubble_toggle = False
        self.space_toggle = False
        self.bubble_counter = 0
        self.current_dialogue =""
        self.dialogue_toggle =False
        self.dialogue_initializer =0
        self.dialogue_counter = 0
        self.letter_counter=0
  
        
             

    def run(self): #function to run the game
        self.playing = True #the game loop runs forever until self.playing is made False
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000 #each loop should last this amount of time (called "time step")
            self.events() #checks for user input and processes them
            self.update() #updates all the data after changes made by events
            #==================================================================================================================
            self.bubble_counter = 0
            self.current_dialogue =""
            for npc in self.NPCs:
                
                if npc.x - 40 <=self.player.pos.x<=npc.x+npc.w+40 and npc.y - 40 <=self.player.pos.y<=npc.y+npc.h+40:
                    self.current_dialogue = self.scripts.script1_dict[npc.name]
                    npc.NPC_bubble=True
                    self.bubble_counter+=1
                else:
                    npc.NPC_bubble=False

            if self.bubble_counter >0:
                self.bubble_toggle = True
            else:
                self.bubble_toggle = False
                

            if self.space_toggle == True and self.bubble_toggle == False:
                self.space_toggle = False

            if self.bubble_toggle == True:
                if self.space_toggle == True:
                    self.dialogue_toggle = True
                else:
                    self.dialogue_toggle = False
            else:
                self.dialogue_toggle = False



            if self.dialogue_toggle == True:

                self.dialogue_initializer += 1
                if self.dialogue_initializer >=40:
                    self.dialogue_initializer =0
                    if self.dialogue_counter +1 < len(self.current_dialogue):
                        self.dialogue_counter +=1 
                

                if self.letter_counter +1 <= len(self.current_dialogue[self.dialogue_counter]):
                    self.letter_counter +=1
               
  
            else:
                self.letter_counter =0
                self.dialogue_initializer =0
                self.dialogue_counter =0

            #==================================================================================================================

            print(self.dialogue_counter)

            

            
                   


            
        
            self.draw() #draws all updated graphics on screen 
       


 
    def quit(self): #function used to quit pygame and the python program
        pg.quit()
        sys.exit()


    def update(self):
        # update portion of the game loop
        self.all_sprites.update() #updates the position of all sprites
        #if self.space_toggle == False and self.current_dialogue != "":
        self.camera.update(self.player) #updates the camera in response to changes in player movement


    def draw(self): #function draws all graphics

       
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect)) # render map image using updated dimensions (map_rect)
        
        for sprite in self.all_sprites: #iterating throught sprite container class
            self.screen.blit(sprite.image, self.camera.apply(sprite)) #draws all sprites according to camera position
            if self.draw_debug:
                pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.hit_rect), 1) #if debugging mode activated, draw sprite borders

        for npc in self.NPCs:
            self.screen.blit(npc.image, self.camera.apply(npc))

        if self.draw_debug:
            for wall in self.walls:
                pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(wall.rect), 1) #if debugging mode activated, draw wall borders
            for npc in self.NPCs:
                pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(npc.rect), 1) #if debugging mode activated, draw wall borders
                if npc.NPC_bubble:
                    pg.draw.rect(self.screen, MIDDLERED, self.camera.apply_rect(npc.rect), 1)

        '''if self.current_dialogue != "":
            pg.draw.rect(self.screen,LIGHTGREY, self.dialogue_rect)'''
        if self.dialogue_toggle == True:
            #pg.draw.rect(self.screen,LIGHTGREY, self.dialogue_rect)
            self.screen.blit(self.dialogue_rect, (10,HEIGHT-130))
            self.dialogue_text =self.font.render((self.current_dialogue[self.dialogue_counter])[0:self.letter_counter], True, BLACK)
            self.screen.blit(self.dialogue_text, (10,HEIGHT-130))
           
        pg.display.flip() #flips the screen to show user what has been drawn


    def events(self): # this function handles all events (user input)
        self.mouse_x = pg.mouse.get_pos()[0]
        self.mouse_y = pg.mouse.get_pos()[1]
        self.click = pg.mouse.get_pressed()
        for event in pg.event.get(): 

            #Quit game is user presses the "x" window button or the escape key
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_h:
                    self.draw_debug = not self.draw_debug #flips the debugging toggle (If on, then off. If off, then on)
                if event.key == pg.K_SPACE:
                    self.space_toggle = not self.space_toggle
                
                
                

    def show_start_screen(self): 

        self.start = StartScreen()
        self.start.RunStart()


    def show_go_screen(self):
        pass  #shows the go screen, which currently doesn't exist

#=================================Main Program===================================
# create the game object
g = Game() #start the game application and loads data
g.show_start_screen() #show start screen
#while True:   
g.new() #start new game
g.run() #run the game
g.show_go_screen() #show the go screen