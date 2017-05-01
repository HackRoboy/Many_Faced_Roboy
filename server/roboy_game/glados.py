from typing import List, Tuple
from game import *
import roboy_interface
import random
import gpsquest
import speak
import roboy_game as states
from cacher import mcache

class GreetState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		states.set_ongoing_mission("Greet the robot!")
	
	def on_leave(self, game:Game, player:int):
		#states.set_mission_done()
		pass
	
	def get_view(self, game:Game, player:int):
		mv = states.get_missions_view()
		pname = game.player_info[player].first_name
		diag = "Hello I am {pname}.".format(pname = pname)
		return View(mv, [[("speak", "*Speak*")],[("opt_hi", diag)]])
	
	def on_opt_hi(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		
		game.set_player_state(player, states.GS.glados_challenge)
		pname = game.player_info[player].first_name
		diag = "Are you ready for a challenge!"
		roboy_interface.roboy_say(diag)
	
	def on_speak(self, game:Game, player:int):
		if not is_focused(game, player):
			return "Face roboy when you speak!"
		return speak.on_speak_handler(self, game, player)

class ChallengeState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		pass
	
	def on_leave(self, game:Game, player:int):
		#states.set_mission_done()
		pass
	
	def get_view(self, game:Game, player:int):
		mv = states.get_missions_view()
		return View(mv, [[("speak", "*Speak*")],[("opt_yes","Yes")],[("opt_no","What kind of a challenge?")]])
	
	def on_opt_no(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		
		game.set_player_state(player, states.GS.glados_refusal)
		pname = game.player_info[player].first_name
		diag = "Are you ready for a challenge!"
		roboy_interface.roboy_say(diag)
	
	def on_opt_yes(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		
		states.set_mission_done()
		game.set_player_state(player, states.GS.glados_quest)
		game.update_single(player)
		pname = game.player_info[player].first_name
		diag = "Are you ready for a challenge!"
		roboy_interface.roboy_say(diag)
	
	def on_speak(self, game:Game, player:int):
		if not is_focused(game, player):
			return "Face roboy when you speak!"

class RefusalState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		#states.set_ongoing_mission("Take the ball to the mountains")
		pass
	
	def on_leave(self, game:Game, player:int):
		#states.set_mission_done()
		pass
	
	def get_view(self, game:Game, player:int):
		mv = states.get_missions_view()
		return View(mv, [[("speak", "*Speak*")],[("opt_fun1", "Funny 1")],[("opt_fun2", "Funny 2")]])
	
	def on_opt_fun1(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		
		game.set_player_state(player, states.GS.glados_challenge)
		pname = game.player_info[player].first_name
		diag = "Are you ready for a challenge!"
		roboy_interface.roboy_say(diag)
	
	def on_opt_fun2(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		
		game.set_player_state(player, states.GS.glados_challenge)
		pname = game.player_info[player].first_name
		diag = "Are you ready for a challenge!"
		roboy_interface.roboy_say(diag)
	
	def on_speak(self, game:Game, player:int):
		if not is_focused(game, player):
			return "Face roboy when you speak!"
		return speak.on_speak_handler(self, game, player)

class QuestState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		states.set_ongoing_mission("Take the Companion Pi to the Food Processing Unit")
		
		def cback():
			self.on_gps(game, player)
		
		coors = (48.268707, 11.665083)
		gpsquest.set_quest(gpsquest.convertdec(coors[0]), gpsquest.convertdec(coors[1]), cback, 0.02)
		#gpsquest.set_quest(4816.09948, 1139.90528, cback, 0.1)
	
	def on_leave(self, game:Game, player:int):
		states.set_mission_done()
	
	def get_view(self, game:Game, player:int):
		mv = states.get_missions_view()
		gpsdone = self.get_priv_data(game, player, "ball_done")
		if not gpsdone:
			return View(mv, [[("speak", "*Speak*")],[("opt_isdone", "I'm done.")],[("opt_refusedo", "I don't wanna do it.*")]])
		else:
			return View(mv, [[("speak", "*Speak*")],[("opt_isdone", "I'm done.")]])
	
	def on_opt_isdone(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		gpsdone = self.get_priv_data(game, player, "ball_done")
		if not gpsdone:
			pname = game.player_info[player].first_name
			diag = "Are you ready for a challenge!"
			roboy_interface.roboy_say(diag)
		else:
			game.set_player_state(player, states.GS.glados_results)
			pname = game.player_info[player].first_name
			diag = "Are you ready for a challenge!"
			roboy_interface.roboy_say(diag)
	
	def on_opt_refusedo(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		
		game.set_player_state(player, states.GS.glados_refusal)
		pname = game.player_info[player].first_name
		diag = "Are you ready for a challenge!"
		roboy_interface.roboy_say(diag)
	
	def on_gps(self, game:Game, player:int):
		pname = game.player_info[player].first_name
		diag = "Are you ready for a challenge!"
		roboy_interface.roboy_say(diag)
		self.set_priv_data(game, player, "ball_done", True)
		states.set_mission_done()
		states.set_ongoing_mission("Go back to GlaDOS")
		game.update_single(player)
		
	
	def on_speak(self, game:Game, player:int):
		if not is_focused(game, player):
			return "Face roboy when you speak!"
		return speak.on_speak_handler(self, game, player)

class ResultsState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		states.set_ongoing_mission("Get your test results.")
	
	def on_leave(self, game:Game, player:int):
		states.set_mission_done()
	
	def get_view(self, game:Game, player:int):
		mv = states.get_missions_view()
		return View(mv, [[("speak", "*Speak*")],[("opt_fun1", "Fun 1")],[("opt_fun2", "Fun 2")]])
	
	def on_opt_fun1(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		
		game.set_player_state(player, states.GS.glados_end)
		pname = game.player_info[player].first_name
		diag = "Are you ready for a challenge!"
		roboy_interface.roboy_say(diag)
	
	def on_opt_fun2(self, game:Game, player:int):
		if not states.is_focused(game, player):
			return "Face roboy when you speak!"
		
		game.set_player_state(player, states.GS.glados_end)
		pname = game.player_info[player].first_name
		diag = "Are you ready for a challenge!"
		roboy_interface.roboy_say(diag)
	
	def on_speak(self, game:Game, player:int):
		if not is_focused(game, player):
			return "Face roboy when you speak!"
		return speak.on_speak_handler(self, game, player)

class EndState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		#states.set_ongoing_mission("Take the ball to the mountains")
		mcache.buzzergo = True
	
	def on_leave(self, game:Game, player:int):
		#states.set_mission_done()
		pass
	
	def get_view(self, game:Game, player:int):
		mv = states.states.get_missions_view() + "\n\nTHE END"
		return View(mv, [[("opt_ok", "*Ok*")]])
	
	def on_opt_ok(self, game:Game, player:int):
		return "Thanks for playing!"
	
	def on_speak(self, game:Game, player:int):
		if not is_focused(game, player):
			return "Face roboy when you speak!"
		return speak.on_speak_handler(self, game, player)