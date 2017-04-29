from typing import List, Tuple
from game import *
import random


GS = enum("init", "give", "result")

class InitState(State):
	def __init__(self):
		pass
		
	def on_init(self, game:Game, player:int):
		self.set_priv_data(game, player, "smiled", False)
	
	def get_view(self, game:Game, player:int):
		if game.dm.get_priv_data(player, "smiled"):
			return View("Get that stupid smile off your face soldier!", [[("say", "Have you heard of any rumors lately?")]])
		else:
			return View("Hi Stranger!", [[("smile", "*smile*")], [("say", "Have you heard of any rumors lately?")]])
	
	def on_smile(self, game:Game, player:int):
		self.set_priv_data(game, player, "smiled", True)
		game.update_single(player)
	
	def on_say(self, game:Game, player:int):
		game.set_player_state(player, GS.give)

class GiveState(State):
	def __init__(self):
		pass
	def get_view(self, game:Game, player:int):
		return View("You need to help Johnny!", [[("ok","Ok man calm down, I'll help Johnny.")]])
	def on_ok(self, game:Game, player:int):
		game.set_player_state(player, GS.result)
		
class ResultState(State):
	def __init__(self):
		pass
	def get_view(self, game:Game, player:int):
		return View("You helped Johnny you are amazing!", [[("ok","Ok.")]])
	def on_ok(self, game:Game, player:int):
		game.set_player_state(player, GS.init)

class RGame(Game):
	g_state_handlers = [InitState(), GiveState(), ResultState()]
	
	def __init__(self, update_foo, leave_foo, creator, player_info):
		Game.__init__(self, update_foo, leave_foo, gtype="rgame", creator = creator, player_info=player_info, 
			state_handlers = RGame.g_state_handlers, player_limit = 300)
		