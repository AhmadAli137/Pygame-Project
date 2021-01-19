#Importing important libraries:
import pygame as pg
from os import path
from settings import *
from Game_Reset import *
from sprite_color_program import *
import sys


class StartScreen:
	def __init__(self): #initializing game class

		pg.init() #initialize pygame
		pg.font.init()
		#self.screen = pg.display.set_mode((int(screen_width-(7/30)*screen_width), int(screen_height-(13/45)*screen_height)),pg.FULLSCREEN)
		#self.screen = pg.display.set_mode((screen_width, screen_height),pg.FULLSCREEN)
		self.screen = pg.display.set_mode((WIDTH, HEIGHT),pg.FULLSCREEN) #creating a screen using parameters from settings.py
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock() #clock used to keep track of time
		pg.key.set_repeat(500, 500) #while a key is held down, there is 500 ms delay until the first repeat, and 500 ms delay between every other repeat
		self.load_data()
		self.spriteColor = sprite_color()
		self.SpriteReset = ResetSprite()

		
	def load_data(self):

		self.font = pg.font.Font(r'horrorfind\\Horrorfind.ttf', 100)
		self.font2 = pg.font.SysFont('Arial', 50, True, False)
		self.title = self.font.render(("Don't Come to My House"), True, (255,0,0))
		self.StartButtonText = self.font2.render("START", True, BLACK)

		self.animation_counter = 0
		self.animation_counter_2 = 0
		self.StartToggle = 1

		self.player_box = pg.Rect((WIDTH-200)/2, (HEIGHT-292)/2, 200, 292)
		self.StartButton = pg.Rect((WIDTH-250)/2, 600, 250,75)
		self.StartButtonOutline = pg.Rect((WIDTH-250)/2, 600, 250,75)
		self.color_box = pg.Rect((WIDTH-200)/2 +250, (HEIGHT-292)/2, 200, 292)
		self.color_box_fill = pg.Surface((200, 292), pg.SRCALPHA)
		self.shader = pg.Surface((40, 40), pg.SRCALPHA)
		self.MIDDLERED_box = pg.Rect(682, 258, 40, 40)
		self.MIDDLEBLUE_box = pg.Rect(737, 258, 40, 40)
		self.MIDDLEGREEN_box = pg.Rect(792, 258, 40, 40)
		self.MIDDLEPINK_box = pg.Rect(682, 313, 40, 40)
		self.MIDDLEORANGE_box = pg.Rect(737, 313, 40, 40)
		self.MIDDLEYELLOW_box = pg.Rect(792, 313, 40, 40)
		self.MIDDLEGREY_box = pg.Rect(682, 368, 40, 40)
		self.CLOUDYWHITE_box = pg.Rect(737, 368, 40, 40)
		self.MIDDLEPURPLE_box = pg.Rect(792, 368, 40, 40)
		self.BROWN_box = pg.Rect(682, 423, 40, 40)
		self.CYAN_box = pg.Rect(737, 423, 40, 40)
		self.LIGHTGREEN_box = pg.Rect(792, 423, 40, 40)
		
		
		
		
		
		
		
		
		
		
		
		  
	def RunStart(self):

		while self.StartToggle == 1:
			self.load_animation()
			self.events() 
			pg.draw.rect(self.screen, DARKGREY, self.player_box, 5)
			self.color_box_fill.fill((100, 100, 100,100))   
			self.shader.fill((40, 40, 40, 100))              
			self.screen.blit(self.color_box_fill, ((WIDTH-200)/2 +250, (HEIGHT-292)/2))
			pg.draw.rect(self.screen, DARKGREY, self.color_box, 5)

            
			self.animation_counter += 1
			if self.animation_counter >= 120:                    
				self.animation_counter = 0
				self.animation_counter_2 += 1
			if self.animation_counter_2 >= len(self.SpriteReset.WalkDown):
				self.animation_counter_2 = 0

			self.button_actions()

			self.screen.blit(self.title, (150,100))
			self.screen.blit(self.StartButtonText, ((WIDTH-140)/2, 610))
			self.screen.blit(self.SpriteReset.WalkDown[self.animation_counter_2], ((WIDTH-64)/2, (HEIGHT-146)/2))
			self.animation_counter += 1

			pg.display.flip()
			self.screen.fill((255,255,255)) #clears screen between frames


	def events(self): # this function handles all events (user input)
		self.mouse_x = pg.mouse.get_pos()[0]
		self.mouse_y = pg.mouse.get_pos()[1]
		self.click = pg.mouse.get_pressed()
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					self.quit()
				

	def button_actions(self):
		if (WIDTH-250)/2 <= self.mouse_x <= (WIDTH-250)/2+250 and 600 <= self.mouse_y <= 675:
				pg.draw.rect(self.screen, DARKRED, self.StartButton)
				pg.draw.rect(self.screen, BLACK, self.StartButtonOutline,5)
				if self.click[0] == 1:
					self.StartToggle=0
		else:
			pg.draw.rect(self.screen, RED, self.StartButton)
			pg.draw.rect(self.screen, BLACK, self.StartButtonOutline,5)

		#========================================================================================
		if (682) <= self.mouse_x <= (682+40)  and (258) <= self.mouse_y <= (258+40):  
			pg.draw.rect(self.screen, MIDDLERED, self.MIDDLERED_box)
			self.screen.blit(self.shader, (682, 258))##########
			if self.click[0] == 1:
				self.spriteColor.change_hair(MIDDLERED)

		else:
			pg.draw.rect(self.screen, MIDDLERED, self.MIDDLERED_box)
			
		pg.draw.rect(self.screen, DARKGREY, self.MIDDLERED_box, 3)
		#==========================================================================================
		if (737) <= self.mouse_x <= (737+40)  and (258) <= self.mouse_y <= (258+40): 
			pg.draw.rect(self.screen, MIDDLEBLUE, self.MIDDLEBLUE_box)
			self.screen.blit(self.shader, (737, 258))##########
			if self.click[0] == 1:
				self.spriteColor.change_hair(MIDDLEBLUE)

		else:
			pg.draw.rect(self.screen, MIDDLEBLUE, self.MIDDLEBLUE_box)
			
		pg.draw.rect(self.screen, DARKGREY, self.MIDDLEBLUE_box, 3)
		#==========================================================================================
		if (792) <= self.mouse_x <= (792+40)  and (258) <= self.mouse_y <= (258+40): 
			pg.draw.rect(self.screen, MIDDLEGREEN, self.MIDDLEGREEN_box)
			self.screen.blit(self.shader, (792, 258))##########
			if self.click[0] == 1:
				self.spriteColor.change_hair(MIDDLEGREEN)

		else:
			pg.draw.rect(self.screen, MIDDLEGREEN, self.MIDDLEGREEN_box)
			
		pg.draw.rect(self.screen, DARKGREY, self.MIDDLEGREEN_box, 3)
		#==========================================================================================
		if (682) <= self.mouse_x <= (682+40)  and (313) <= self.mouse_y <= (313+40): 
			pg.draw.rect(self.screen, MIDDLEPINK, self.MIDDLEPINK_box)              
			self.screen.blit(self.shader, (682, 313))##########
			if self.click[0] == 1:
				self.spriteColor.change_hair(MIDDLEPINK)

		else:
			pg.draw.rect(self.screen, MIDDLEPINK, self.MIDDLEPINK_box)
			
		pg.draw.rect(self.screen, DARKGREY, self.MIDDLEPINK_box, 3)
		#==========================================================================================
		if (737) <= self.mouse_x <= (737+40)  and (313) <= self.mouse_y <= (313+40): 
			pg.draw.rect(self.screen, MIDDLEORANGE, self.MIDDLEORANGE_box)              
			self.screen.blit(self.shader, (737, 313))##########
			if self.click[0] == 1:
				self.spriteColor.change_hair(MIDDLEORANGE)

		else:
			pg.draw.rect(self.screen, MIDDLEORANGE, self.MIDDLEORANGE_box)
			
		pg.draw.rect(self.screen, DARKGREY, self.MIDDLEORANGE_box, 3)
		#==========================================================================================
		if (792) <= self.mouse_x <= (792+40)  and (313) <= self.mouse_y <= (313+40): 
			pg.draw.rect(self.screen, MIDDLEYELLOW, self.MIDDLEYELLOW_box)              
			self.screen.blit(self.shader, (792, 313))##########
			if self.click[0] == 1:
				self.spriteColor.change_hair(MIDDLEYELLOW)

		else:
			pg.draw.rect(self.screen, MIDDLEYELLOW, self.MIDDLEYELLOW_box)
			
		pg.draw.rect(self.screen, DARKGREY, self.MIDDLEYELLOW_box, 3)
		#==========================================================================================
		if (682) <= self.mouse_x <= (682+40)  and (368) <= self.mouse_y <= (368+40): 
			pg.draw.rect(self.screen, MIDDLEGREY, self.MIDDLEGREY_box)              
			self.screen.blit(self.shader, (682, 368))##########
			if self.click[0] == 1:
				self.spriteColor.change_hair(MIDDLEGREY)

		else:
			pg.draw.rect(self.screen, MIDDLEGREY, self.MIDDLEGREY_box)
			
		pg.draw.rect(self.screen, DARKGREY, self.MIDDLEGREY_box, 3)
		#==========================================================================================
		if (737) <= self.mouse_x <= (737+40)  and (368) <= self.mouse_y <= (368+40): 
			pg.draw.rect(self.screen, CLOUDYWHITE, self.CLOUDYWHITE_box)              
			self.screen.blit(self.shader, (737, 368))##########
			if self.click[0] == 1:
				self.spriteColor.change_hair(CLOUDYWHITE)

		else:
			pg.draw.rect(self.screen, CLOUDYWHITE, self.CLOUDYWHITE_box)
			
		pg.draw.rect(self.screen, DARKGREY, self.CLOUDYWHITE_box, 3)
		#==========================================================================================
		if (792) <= self.mouse_x <= (792+40)  and (368) <= self.mouse_y <= (368+40): 
			pg.draw.rect(self.screen, MIDDLEPURPLE, self.MIDDLEPURPLE_box)              
			self.screen.blit(self.shader, (792, 368))##########
			if self.click[0] == 1:
				self.spriteColor.change_hair(MIDDLEPURPLE)

		else:
			pg.draw.rect(self.screen, MIDDLEPURPLE, self.MIDDLEPURPLE_box)
			
		pg.draw.rect(self.screen, DARKGREY, self.MIDDLEPURPLE_box, 3)
		#==========================================================================================
		if (682) <= self.mouse_x <= (682+40)  and (423) <= self.mouse_y <= (423+40): 
			pg.draw.rect(self.screen, BROWN, self.BROWN_box)              
			self.screen.blit(self.shader, (682, 423))##########
			if self.click[0] == 1:
				self.spriteColor.change_hair(BROWN)

		else:
			pg.draw.rect(self.screen, BROWN, self.BROWN_box)
			
		pg.draw.rect(self.screen, DARKGREY, self.BROWN_box, 3)
		#==========================================================================================
		if (737) <= self.mouse_x <= (737+40)  and (423) <= self.mouse_y <= (423+40): 
			pg.draw.rect(self.screen, CYAN, self.CYAN_box)              
			self.screen.blit(self.shader, (737, 423))##########
			if self.click[0] == 1:
				self.spriteColor.change_hair(CYAN)

		else:
			pg.draw.rect(self.screen, CYAN, self.CYAN_box)
			
		pg.draw.rect(self.screen, DARKGREY, self.CYAN_box, 3)
		#==========================================================================================
		if (792) <= self.mouse_x <= (792+40)  and (423) <= self.mouse_y <= (423+40): 
			pg.draw.rect(self.screen, LIGHTGREEN, self.LIGHTGREEN_box)              
			self.screen.blit(self.shader, (792, 423))##########
			if self.click[0] == 1:
				self.spriteColor.change_hair(LIGHTGREEN)

		else:
			pg.draw.rect(self.screen, LIGHTGREEN, self.LIGHTGREEN_box)
			
		pg.draw.rect(self.screen, DARKGREY, self.LIGHTGREEN_box, 3)

	def load_animation(self):
		self.SpriteReset.WalkDown =[]
		#self.WalkDown_raw =[]
		for filename in os.listdir(self.SpriteReset.WalkDownFolder):
		    #self.image = Image.open(path.join(self.WalkDownFolder, filename)) 
		    self.pg_image = pg.image.load(path.join(self.SpriteReset.WalkDownFolder, filename))
		    self.SpriteReset.WalkDown.append(self.pg_image)
		    #self.WalkDown_raw.append(self.image)

	def quit(self): #function used to quit pygame and the python program
		pg.quit()
		sys.exit()

