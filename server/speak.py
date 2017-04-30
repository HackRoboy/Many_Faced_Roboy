from typing import List, Tuple
from game import *
import roboy_interface
import sys

def strdist(s1, s2):
	arr1 = [0 for i in range(len(s2) + 1)]
	arr2 = [0 for i in range(len(s2) + 1)]
	for a in range(len(s1)):
		for b in range(len(s2)):
			arr2[b] = min(arr1[b] + 1, arr2[b-1] + 1, arr1[b-1] + (0 if s1[a] == s2[b] else 1))
		arr1 = arr2
		arr2 = [0 for i in range(len(s2) + 1)]
	return arr1[-2]

def on_speak_handler(state:State, game:Game, player:int):
	view = state.get_view(game, player)
	ops = [but[0] for but in view.buttons]
	speech = roboy_interface.roboy_detect_speech()#"test"#roboy_detect_speech()
	if speech is None: 
		speech = ""
	print(speech, file=sys.stderr)
	minop = min(ops, key = lambda x:strdist(x[1],speech))
	return state.handle_action(game, player, minop[0])
	