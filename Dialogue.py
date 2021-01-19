from settings import *

class dialogue():
	def __init__(self,game):
	
		self.script1_dict = {}
		for npc in game.NPC_list:
			self.script1_dict[npc] = []

		with open("Dialogue\\Script1.txt") as script1:
			for line in script1:
				try:
				    string = line.split(":")
				    if string[0] in game.NPC_list:
				    	 self.script1_dict[string[0]].append(string[1].replace("\n", '').replace('[', '').replace(']', ''))
				except:
					pass
			    
		print(self.script1_dict)




		