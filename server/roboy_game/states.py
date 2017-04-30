from typing import List, Tuple
from game import *
import roboy_interface
import random
import gpsquest
import speak

GS = enum("greet", "putball", "getball", "notask", "gpsresult")

done_missions = ""
ongoing_mission = " "

def set_mission_done():
	global done_missions, ongoing_mission
	done_missions += "+ *" + ongoing_mission + "*\n"
	ongoing_mission = " "

def get_missions_view():
	if ongoing_mission.strip() == "":
		return "*Quests:*\n" + done_missions
	return "*Quests:*\n" + done_missions + "+ " + ongoing_mission + "\n"

def is_focused(game:Game, player:int):
	return True
	if game.dm.get_data("focus") is None:
		return False
	if not game.dm.get_data("focus")["val"]:
		return False
	return True

def set_ongoing_mission(text:str):
	global ongoing_mission
	ongoing_mission = text

class GreetState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		set_ongoing_mission("Introduce yourself to the stranger")
		def cback():
			self.on_gps(game, player)
		#48.270156, 11.665524
		#coors = (48.268717, 11.665057)
		#gpsquest.set_quest(gpsquest.convertdec(coors[0]), gpsquest.convertdec(coors[1]), cback, 0.01)
		gpsquest.set_quest(4816.09948, 1139.90528, cback, 0.1)
	
	def on_leave(self, game:Game, player:int):
		set_mission_done()
	
	def get_view(self, game:Game, player:int):
		mv = get_missions_view()
		return View(mv, [[("speak", "*Speak*")], [("greetings", "Greetings!")],[("waddup", "Waddup!")]])
	
	def on_greetings(self, game:Game, player:int):
		if not is_focused(game, player):
			return "Face roboy when you speak!"
		
		roboy_interface.roboy_say("Greetings!")
		game.set_player_state(player, GS.putball)
		
	def on_waddup(self, game:Game, player:int):
		if not is_focused(game, player):
			return "Face roboy when you speak!"
		
		roboy_interface.roboy_say("Be respectful adventurer!")
		game.set_player_state(player, GS.putball)
	
	def on_gps(self, game:Game, player:int):
		game.set_player_state(player, GS.gpsresult)
	
	def on_speak(self, game:Game, player:int):
		if not is_focused(game, player):
			return "Face roboy when you speak!"
		return speak.on_speak_handler(self, game, player)

class PutBallState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		set_ongoing_mission("Take the ball to the mountains")
	
	def on_leave(self, game:Game, player:int):
		set_mission_done()
	
	def get_view(self, game:Game, player:int):
		mv = get_missions_view()
		return View(mv, [[("speak", "*Speak*")], [("done", "I did it!")],[("cancel", "I don't want to do it.")]])
	
	def on_done(self, game:Game, player:int):
		if not is_focused(game, player):
			return "Face roboy when you speak!"
		
		if game.dm.get_data("ball") != {"x":5,"y":5,"z":5}:
			roboy_interface.roboy_say("You can't fool me! You didn't put the ball!")
		else:
			roboy_interface.roboy_say("You are amazing!")
			game.set_player_state(player, GS.greet)
	
	def on_cancel(self, game:Game, player:int):
		roboy_interface.roboy_say("Casuals")
		game.set_player_state(player, GS.greet)
	
	def on_speak(self, game:Game, player:int):
		if not is_focused(game, player):
			return "Face roboy when you speak!"
		return speak.on_speak_handler(self, game, player)

class GetBallState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		set_ongoing_mission("Bring the ball back!")
	
	def on_leave(self, game:Game, player:int):
		set_mission_done()
	
	def get_view(self, game:Game, player:int):
		pass

class NoTasksState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		pass
	
	def get_view(self, game:Game, player:int):
		pass

class GpsResultState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		pass
	
	def get_view(self, game:Game, player:int):
		return View("You found the secret!!!", [[("done", "I did it!")]])
	
	def on_done(self, game:Game, player:int):
		game.set_player_state(player, GS.greet)

g_state_handlers = [GreetState(), PutBallState(), GetBallState(), NoTasksState(), GpsResultState()]