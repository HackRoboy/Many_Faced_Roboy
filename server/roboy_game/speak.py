from typing import List, Tuple
from game import *
from roboy_interface import roboy_detect_speech
import random

def on_speak_handler(state:State, game:Game, player:int):
	view = state.get_view(game, player)
    ops = [but[0] for but in view.buttons]
    