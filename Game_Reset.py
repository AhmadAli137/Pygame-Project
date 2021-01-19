import shutil  
import os
from os import path


class ResetSprite:
	def __init__(self):
		
		self.game_folder = ""
		#self.game_folder = path.dirname(__file__) #game folder is the folder this program is currently located in
		self.sprite_folder = path.join(self.game_folder, 'sprites')
		self.temp_folder = path.join(self.sprite_folder, 'Temp Sprite')
		self.Pre_folder = path.join(self.sprite_folder, 'Premade Sprite')

		self.WalkUpFolder = path.join(self.temp_folder, 'WalkUp')
		self.WalkUpFolder_2 = path.join(self.Pre_folder, 'WalkUp')

		self.WalkDownFolder = path.join(self.temp_folder, 'WalkDown') 
		self.WalkDownFolder_2 = path.join(self.Pre_folder, 'WalkDown') 
		
		self.WalkRightFolder = path.join(self.temp_folder, 'WalkRight')
		self.WalkRightFolder_2 = path.join(self.Pre_folder, 'WalkRight')
		
		self.WalkLeftFolder = path.join(self.temp_folder, 'WalkLeft')
		self.WalkLeftFolder_2 = path.join(self.Pre_folder, 'WalkLeft')
			
		self.WalkRightUpFolder = path.join(self.temp_folder, 'WalkRightUp')
		self.WalkRightUpFolder_2 = path.join(self.Pre_folder, 'WalkRightUp')
			
		self.WalkLeftUpFolder = path.join(self.temp_folder, 'WalkLeftUp')
		self.WalkLeftUpFolder_2 = path.join(self.Pre_folder, 'WalkLeftUp')
		
		self.WalkRightDownFolder = path.join(self.temp_folder, 'WalkRightDown')
		self.WalkRightDownFolder_2 = path.join(self.Pre_folder, 'WalkRightDown')
		
		self.WalkLeftDownFolder = path.join(self.temp_folder, 'WalkLeftDown')
		self.WalkLeftDownFolder_2 = path.join(self.Pre_folder, 'WalkLeftDown')
		
		self.SarkerWalkDownFolder = path.join(self.temp_folder, 'SarkerWalkDown')
		self.SarkerWalkDownFolder_2 = path.join(self.Pre_folder, 'SarkerWalkDown')
		
		self.RunUpFolder = path.join(self.temp_folder, 'RunUp')
		self.RunUpFolder_2 = path.join(self.Pre_folder, 'RunUp')
		
		self.RunDownFolder = path.join(self.temp_folder, 'RunDown')
		self.RunDownFolder_2 = path.join(self.Pre_folder, 'RunDown')
			
		self.RunRightFolder = path.join(self.temp_folder, 'RunRight')
		self.RunRightFolder_2 = path.join(self.Pre_folder, 'RunRight')
		
		self.RunLeftFolder = path.join(self.temp_folder, 'RunLeft')
		self.RunLeftFolder_2 = path.join(self.Pre_folder, 'RunLeft')
		
		self.RunRightUpFolder = path.join(self.temp_folder, 'RunRightUp')
		self.RunRightUpFolder_2 = path.join(self.Pre_folder, 'RunRightUp')
		
		self.RunLeftUpFolder = path.join(self.temp_folder, 'RunLeftUp')
		self.RunLeftUpFolder_2 = path.join(self.Pre_folder, 'RunLeftUp')
		
		self.RunRightDownFolder = path.join(self.temp_folder, 'RunRightDown')
		self.RunRightDownFolder_2 = path.join(self.Pre_folder, 'RunRightDown')
		
		self.RunLeftDownFolder = path.join(self.temp_folder, 'RunLeftDown')
		self.RunLeftDownFolder_2 = path.join(self.Pre_folder, 'RunLeftDown')
		
		
	def delete_cache(self):
		shutil.rmtree(self.WalkUpFolder)
		shutil.rmtree(self.WalkDownFolder)
		shutil.rmtree(self.WalkRightFolder)
		shutil.rmtree(self.WalkLeftFolder)
		shutil.rmtree(self.WalkRightUpFolder)
		shutil.rmtree(self.WalkLeftUpFolder)
		shutil.rmtree(self.WalkRightDownFolder)
		shutil.rmtree(self.WalkLeftDownFolder)
		shutil.rmtree(self.SarkerWalkDownFolder)
		shutil.rmtree(self.RunUpFolder)
		shutil.rmtree(self.RunDownFolder)
		shutil.rmtree(self.RunRightFolder)
		shutil.rmtree(self.RunLeftFolder)
		shutil.rmtree(self.RunRightUpFolder)
		shutil.rmtree(self.RunLeftUpFolder)
		shutil.rmtree(self.RunRightDownFolder)
		shutil.rmtree(self.RunLeftDownFolder)


	def reset_sprite(self):
		shutil.copytree(self.WalkUpFolder_2, self.WalkUpFolder)
		shutil.copytree(self.WalkDownFolder_2, self.WalkDownFolder)
		shutil.copytree(self.WalkRightFolder_2, self.WalkRightFolder)
		shutil.copytree(self.WalkLeftFolder_2, self.WalkLeftFolder)
		shutil.copytree(self.WalkRightUpFolder_2, self.WalkRightUpFolder)
		shutil.copytree(self.WalkLeftUpFolder_2, self.WalkLeftUpFolder)
		shutil.copytree(self.WalkRightDownFolder_2, self.WalkRightDownFolder)
		shutil.copytree(self.WalkLeftDownFolder_2, self.WalkLeftDownFolder)
		shutil.copytree(self.SarkerWalkDownFolder_2, self.SarkerWalkDownFolder)
		shutil.copytree(self.RunUpFolder_2, self.RunUpFolder)
		shutil.copytree(self.RunDownFolder_2, self.RunDownFolder)
		shutil.copytree(self.RunRightFolder_2, self.RunRightFolder)
		shutil.copytree(self.RunLeftFolder_2, self.RunLeftFolder)
		shutil.copytree(self.RunRightUpFolder_2, self.RunRightUpFolder)
		shutil.copytree(self.RunLeftUpFolder_2, self.RunLeftUpFolder)
		shutil.copytree(self.RunRightDownFolder_2, self.RunRightDownFolder)
		shutil.copytree(self.RunLeftDownFolder_2, self.RunLeftDownFolder)