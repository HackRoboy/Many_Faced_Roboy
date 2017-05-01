from typing import List, Tuple
from game import *
import roboy_interface
import sys

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def strdist(s1, s2):
	res = levenshtein(s1, s2)
	print(s1, s2, res, file=sys.stderr)
	return res
	
	arr1 = [0 for i in range(len(s2) + 1)]
	arr2 = [0 for i in range(len(s2) + 1)]
	for a in range(len(s1)):
		for b in range(len(s2)):
			arr2[b] = min(arr1[b] + 1, arr2[b-1] + 1, arr1[b-1] + (0 if s1[a] == s2[b] else 1))
		arr1 = arr2
		arr2 = [0 for i in range(len(s2) + 1)]
	print(s1, s2, arr1[-2], file=sys.stderr)
	return arr1[-2]

def on_speak_handler(state:State, game:Game, player:int):
	view = state.get_view(game, player)
	ops = [but[0] for but in view.buttons if but[0][0] != "speak"]
	speech = roboy_interface.roboy_detect_speech()#"test"#roboy_detect_speech()
	if speech is None: 
		speech = ""
	print(speech, file=sys.stderr)
	minop = min(ops, key = lambda x:strdist(x[1],speech))
	return state.handle_action(game, player, minop[0])
	