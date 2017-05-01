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
		roboy_interface.roboy_emotion(True)
		states.set_ongoing_mission("Greet the Khajiit")
	
	def on_leave(self, game:Game, player:int):
		#states.set_mission_done()
		pass
	
	def get_view(self, game:Game, player:int):
		mv = states.get_missions_view()
		return View(mv, [[("speak", "*Speak*")], [("opt_hello", "Hello!")], [("opt_greetings", "Greetings Master Khajiit.")]])
	
	def on_opt_hello(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		
		self.set_priv_data(game, player, "who_disabled", True)
		game.set_player_state(player, states.GS.khajit_whatwho)
		pname = game.player_info[player].first_name
		diag = "I welcome you friend, how can I serve you?"
		roboy_interface.roboy_say(diag)
	
	def on_opt_greetings(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		
		
		self.set_priv_data(game, player, "who_disabled", False)
		game.set_player_state(player, states.GS.khajit_whatwho)
		pname = game.player_info[player].first_name
		diag = "You approach as if you know Khajiit. Who are you and what do you want?"
		roboy_interface.roboy_say(diag)
	
	def on_speak(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		return speak.on_speak_handler(self, game, player)

class WhatWhoState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		if self.get_priv_data(game, player, "what_done") and self.get_priv_data(game, player, "who_done"):
			game.set_player_state(player, states.GS.khajit_whathap)
			pname = game.player_info[player].first_name
			diag = "May the sun keep you warm even in this land of bitter cold."
			roboy_interface.roboy_say(diag)
	
	def on_leave(self, game:Game, player:int):
		#states.set_mission_done()
		pass
	
	def get_view(self, game:Game, player:int):
		mv = states.get_missions_view()
		
		whatbut = []
		whobut = []
		pname = game.player_info[player].first_name
		if not self.get_priv_data(game, player, "who_done"):
			whobut = [[("opt_who", "I am {pname} the Adventurer!".format(pname = pname))]]
		if not self.get_priv_data(game, player, "what_done"):
			whatbut = [[("opt_what", "I am looking for an invisible sword.")]]
			if self.get_priv_data(game, player, "who_disabled"):
				whobut = []
		
		return View(mv, [[("speak", "*Speak*")]] + whatbut + whobut)
	
	def on_opt_who(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		
		game.set_player_state(player, states.GS.khajit_who)
		pname = game.player_info[player].first_name
		diag = "Ah, I see my friend. I used to be an adventurer like you."
		roboy_interface.roboy_say(diag)
	
	def on_opt_what(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		
		game.set_player_state(player, states.GS.khajit_what)
		pname = game.player_info[player].first_name
		diag = "Khajiit has wares if you have coin."
		roboy_interface.roboy_say(diag)
	
	def on_speak(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		return speak.on_speak_handler(self, game, player)
		


class WhoState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		pass
	
	def on_leave(self, game:Game, player:int):
		self.set_priv_data(game, player, "who_done", True)
		pass
	
	def get_view(self, game:Game, player:int):
		mv = states.get_missions_view()
		diag1 = "It is your turn to tell me about you."
		diag2 = "What kind of an adventurer were you?"
		return View(mv, [[("speak", "*Speak*")],[("opt_diag1", diag1)],[("opt_diag2", diag2)]])
	
	def on_opt_diag1(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
			
		game.set_player_state(player, states.GS.khajit_whatwho)
		pname = game.player_info[player].first_name
		diag = "I travel all across Garshing to serve you, but I seem to have an unfortunate talent for getting myself involved with misunderstandings with the law."
		roboy_interface.roboy_say(diag)
		pass
	
	def on_opt_diag2(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
			
		game.set_player_state(player, states.GS.khajit_whatwho)
		pname = game.player_info[player].first_name
		diag = "I travel all across Garshing to serve you, but I seem to have an unfortunate talent for getting myself involved with misunderstandings with the law."
		roboy_interface.roboy_say(diag)
		pass
	
	def on_speak(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		return speak.on_speak_handler(self, game, player)

class WhatState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		pass
	
	def on_leave(self, game:Game, player:int):
		self.set_priv_data(game, player, "what_done", True)
		pass
	
	def get_view(self, game:Game, player:int):
		mv = states.get_missions_view()
		diag1 = "Not interested."
		diag2 = "Yes, I have. But I have to bring it later."
		return View(mv, [[("speak", "*Speak*")],[("opt_diag1", diag1)],[("opt_diag2", diag2)]])
	
	def on_opt_diag1(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
			
		game.set_player_state(player, states.GS.khajit_whatwho)
		pname = game.player_info[player].first_name
		diag = "Oh, I see. These lands are cruel."
		roboy_interface.roboy_say(diag)
		pass
	
	def on_opt_diag2(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
			
		game.set_player_state(player, states.GS.khajit_whatwho)
		pname = game.player_info[player].first_name
		diag = "These sands are cold, but Khajiit feels warm from your presence."
		roboy_interface.roboy_say(diag)
		pass
	
	def on_speak(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		return speak.on_speak_handler(self, game, player)

class WhathapState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		roboy_interface.roboy_emotion(False)
		states.set_mission_done()
		states.set_ongoing_mission("Go back to the Khajiit")
		pass
	
	def on_leave(self, game:Game, player:int):
		roboy_interface.roboy_emotion(True)
		pass
	
	def get_view(self, game:Game, player:int):
		mv = states.get_missions_view()
		return View(mv, [[("speak", "*Speak*")],[("opt_diag1", "Why do you seem so upset?")]])
	
	def on_opt_diag1(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
			
		game.set_player_state(player, states.GS.khajit_whatsword)
		pname = game.player_info[player].first_name
		diag = "Have you seen a sword around here? They blame Khajiit for stealing it."
		roboy_interface.roboy_say(diag)
		pass
	
	def on_speak(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		return speak.on_speak_handler(self, game, player)
	
class WhatswordState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		pass
	
	def on_leave(self, game:Game, player:int):
		pass
	
	def get_view(self, game:Game, player:int):
		mv = states.get_missions_view()
		return View(mv, [[("speak", "*Speak*")],[("opt_diag1", "No, I haven't seen anything.")],[("opt_diag2", "Yes I actually...")]])
	
	def on_opt_diag1(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
			
		game.set_player_state(player, states.GS.khajit_end)
		#pname = game.player_info[player].first_name
		#roboy_interface.roboy_say(diag)
		pass
	
	def on_opt_diag2(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
			
		game.set_player_state(player, states.GS.khajit_end)
		#pname = game.player_info[player].first_name
		#roboy_interface.roboy_say(diag)
		pass
	
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