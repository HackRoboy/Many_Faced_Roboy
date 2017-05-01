from typing import List, Tuple
from game import *
import random
from roboy_game.states import *


class RGame(Game):
	def __init__(self, update_foo, leave_foo, creator, player_info):
		Game.__init__(self, update_foo, leave_foo, gtype="rgame", creator = creator, player_info=player_info, 
			state_handlers = g_state_handlers, player_limit = 300, init_state = 9)
		