from typing import List, Tuple
from game import *
import roboy_interface
import random
import gpsquest
import speak
import roboy_game.navi as navi
import roboy_game.glados as glados
import roboy_game.khajit as khajit

GS = enum("navi_greet", "navi_quest", "navi_end", 
		"glados_greet", "glados_challenge", "glados_quest", "glados_refusal", "glados_results", "glados_end",
		"khajit_greet", "khajit_whatwho", "khajit_what", "khajit_who", "khajit_end", "khajit_whathap", "khajit_whatsword")

done_missions = ""
ongoing_mission = " "

def set_mission_done():
	global done_missions, ongoing_mission
	done_missions += "+ _" + ongoing_mission + "_\n"
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



g_state_handlers = [navi.GreetState(), navi.QuestState(), navi.EndState(),
 glados.GreetState(), glados.ChallengeState(), glados.QuestState(), glados.RefusalState(), glados.ResultsState(), glados.EndState(),
 khajit.GreetState(), khajit.WhatWhoState(), khajit.WhatState(), khajit.WhoState(), khajit.EndState(), khajit.WhathapState(), khajit.WhatswordState()]