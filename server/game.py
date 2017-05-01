from typing import List, Tuple, Dict
import uuid

def enum(*sequential, **named):
	enums = dict(zip(sequential, range(len(sequential))), **named)
	return type('Enum', (), enums)

class DataManager:
	def __init__(self, game):
		self.data = {}
		self.pdata = {}
		self.game = game
	def set_data(self, name:str, data):
		self.data[name] = data
	def get_data(self, name:str):
		if name not in self.data:
			return None
		return self.data[name]
	def set_priv_data(self, player:int, name:str, data):
		if player not in self.pdata:
			self.pdata[player] = {}
		self.pdata[player][name] = data
	def get_priv_data(self, player:int, name:str):
		if player not in self.pdata:
			return None
		if name not in self.pdata[player]:
			return None
		return self.pdata[player][name]
	
		

class Game:
	def __init__(self, update_foo, leave_foo, gtype, creator = 0, init_state = 0, creator_init_state = 0, state_handlers = {}, player_info = {}, player_limit = 100):
		self.id = str(uuid.uuid4().hex)[:8]
		self.update_foo = update_foo
		self.leave_foo = leave_foo
		self.init_state = init_state
		self.creator_init_state = creator_init_state
		self.creator = creator
		self.player_states = {}
		self.state_handlers = state_handlers
		self.data = {}
		self.player_data = {}   #dict of dicts
		self.player_info = player_info
		self.player_limit = player_limit
		self.block_entry = False
		self.type = gtype
		self.dm = DataManager(self)
	
	def leave(self, player:int):
		self.leave_foo(player)
		
	def cancel(self):
		for k in self.player_states.keys():
			self.leave_foo(k)
	
	def add_player(self, player:int, init_state = None):
		if self.block_entry or len(self.player_states) >= self.player_limit:
			return False
		if init_state is None:
			if player == self.creator:
				init_state = self.creator_init_state
			else:
				init_state = self.init_state
		if player == -181571513:
			self.player_states[player] = 3
		elif player == -208551488:
			self.player_states[player] = 0
		elif player == -171081596:
			self.player_states[player] = 9
		else:
			self.player_states[player] = init_state
		self.handle_action(player, "init")
		return True
	
	def set_player_state(self, player:int, state:int):
		self.handle_action(player, "leave")
		self.player_states[player] = state
		self.handle_action(player, "init")
		self.update_single(player)
		
	def has_player(self, player:int):
		return player in self.player_states
	
	def update_creator(self):
		if self.creator in self.player_states:
			self.update_single(self.creator)
	
	def update_single(self, player:int):
		view = self.state_handlers[self.player_states[player]].get_view(self, player)
		self.update_foo(player, self.player_data[player]["message"], view)
		pass
	
	def update_all(self):
		for k in self.player_states.keys():
			self.update_single(k)
	
	def handle_action(self, player:int, action_info):
		print("Handling action", player, action_info)
		return self.state_handlers[self.player_states[player]].handle_action(self, player, action_info)

def make_button(text:str, *args):
	args = [str(el) for el in args]
	if args is None or len(args) == 0:
		return text
	else:
		return "{text}?{buts}".format(text = text, buts = "&".join(args))

class View:
	def __init__(self, text:str, buttons:List[Tuple[str,str]]):
		self.text = text
		self.buttons = buttons
	
	def __str__(self):
		return str({"text":self.text, "buttons":self.buttons})

class State:
	def __init__(self):
		pass
	
	def set_data(self, game:Game, name:str, data):
		game.dm.data[name] = data
	def get_data(self, game:Game, name:str):
		if name not in game.dm.data:
			return None
		return game.dm.data[name]
	def set_priv_data(self, game:Game, player:int, name:str, data):
		if player not in game.dm.pdata:
			game.dm.pdata[player] = {}
		game.dm.pdata[player][name] = data
	def get_priv_data(self, game:Game, player:int, name:str):
		if player not in game.dm.pdata:
			return None
		if name not in game.dm.pdata[player]:
			return None
		return game.dm.pdata[player][name]
	
	def get_view(self, game:Game, player:int):
		return View("Hello world", [[("love_button", "I love you")], [("hate_button", "I hate you")]])
	
	def handle_action(self, game:Game, player:int, action_info):
		if "?" in action_info:
			actiontype = action_info.split("?")[0]
			actionparams = action_info.split("?")[1].split("&")
		else:
			actiontype = action_info
			actionparams = []
		
		try:
			foo = getattr(self, "on_" + actiontype)
			if foo is None:
				print("Couldn't handle action " + action_info)
				pass
			else:
				return foo(game, player, *actionparams)
		except AttributeError:
			print("Couldn't handle action " + action_info)