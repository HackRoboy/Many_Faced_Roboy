from typing import List, Tuple
from game import *
import roboy_interface
import random
import gpsquest
import speak
import roboy_game as states

class GreetState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		self.set_priv_data(game, player, "not_count", 0)
		self.set_priv_data(game, player, "said_not", False)
		
		states.set_ongoing_mission("Greet the fairy")
	
	def on_leave(self, game:Game, player:int):
		states.set_mission_done()
	
	def get_view(self, game:Game, player:int):
		mv = states.get_missions_view()
		yes_option = "Yes Navi?" if not self.get_priv_data(game, player, "said_not") else "Ugh ok."
		not_option = "Not now" + "!" * self.get_priv_data(game, player, "not_count")
		
		return View(mv, [[("speak", "*Speak*")], [("opt_yes", yes_option)], [("opt_not", not_option)]])
	
	def on_speak(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		return speak.on_speak_handler(self, game, player)
	
	def on_opt_not(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		
		self.set_priv_data(game, player, "said_not", True)
		self.set_priv_data(game, player, "not_count", self.get_priv_data(game, player, "not_count") + 1)
		
		pname = game.player_info[player].first_name
		diag = "{pname}! Listen! Hey! Hey you! Listen!".format(pname = pname)
		game.update_single(player)
		roboy_interface.roboy_say(diag)
	
	def on_opt_yes(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		
		game.set_player_state(player, states.GS.navi_quest)
		pname = game.player_info[player].first_name
		diag = "Hey listen! Hold the controller in the air and jump!"
		roboy_interface.roboy_say(diag)

class QuestState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		states.set_ongoing_mission("Hold the controller in the air and jump!")
	
	def on_leave(self, game:Game, player:int):
		states.set_mission_done()
	
	def get_view(self, game:Game, player:int):
		mv = states.get_missions_view()
		return View(mv, [[("speak", "*Speak*")], [("opt_leaveme","Leave me alone!")], [("opt_imdone","I'm done.")]])
	
	def on_opt_leaveme(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		game.set_player_state(player, states.GS.navi_greet)
		pname = game.player_info[player].first_name
		diag = "Hey! Listen! Hey {pname}! Listen!".format(pname = pname)
		roboy_interface.roboy_say(diag)
	
	def on_opt_imdone(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		
		if game.dm.get_data("ball") != {"x":5,"y":5,"z":5}:
			roboy_interface.roboy_say("Hey you! You aren't done! Listen!")
		else:
			roboy_interface.roboy_say("Hey you! Hey! Thank you!")
			game.set_player_state(player, states.GS.navi_end)
	
	def on_speak(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		return speak.on_speak_handler(self, game, player)

class EndState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		#set_ongoing_mission("Take the ball to the mountains")
		pass
	
	def on_leave(self, game:Game, player:int):
		pass
	
	def get_view(self, game:Game, player:int):
		mv = states.get_missions_view() + "\n\nTHE END"
		return View(mv, [[("opt_ok", "*Ok*")]])
	
	def on_opt_ok(self, game:Game, player:int):
		return "Thanks for playing!"
	
	def on_speak(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		return speak.on_speak_handler(self, game, player)

