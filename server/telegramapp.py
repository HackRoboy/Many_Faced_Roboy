import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
import game
import my_games
import uuid, threading, sys
from random import getrandbits

from botsettings import TOKEN

update_id = None


games = {}
player_gameids = {}
player_info = {}
message_state = {}
button_state = {}


def main():
	global update_id
	global bot
	global the_game
	
	
	#global game
	# Telegram Bot Authorization Token
	bot = telegram.Bot(TOKEN)
	
	#game = resistance.ResistanceGame(update_view)
	#games[game.id] = game

	# get the first pending update_id, this is so we can skip over it in case
	# we get an "Unauthorized" exception.
	if len(bot.getUpdates()) > 0:
		update_id = bot.getUpdates()[-1].update_id + 1
	else:
		update_id = None

	logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	
	def mt():
		while True:
			try:
				handle(bot)
			except NetworkError:
				pass
				#sleep(1)
			except Unauthorized:
				# The user has removed or blocked the bot.
				update_id += 1
			except:
				print("There was exception")

	threading.Thread(target=mt).start()
	

def join_game(chat_id: int, gameid:str):
	if not chat_id in player_gameids:
		game = games[gameid]
		player_gameids[chat_id] = game.id
		joined = game.add_player(chat_id)
		if joined:
			bot.send_message(chat_id = chat_id, text = "Joined game " + str(gameid))
			msg = bot.send_message(chat_id = chat_id, text = "_Loading..._", parse_mode="Markdown")
			print(msg)
			game.player_data[chat_id] = {"message" : msg.message_id}
			game.update_single(chat_id)
		else:
			bot.send_message(chat_id = chat_id, text = "Couldn't join game, it's probably full.")
	else:
		bot.send_message(chat_id = chat_id, text = "You are already in a game!")


def handle(bot):
	global update_id
	# Request updates after the last update_id
	for update in bot.getUpdates(offset=update_id, timeout=10):
		# chat_id is required to reply to any message
		update_id = update.update_id + 1
		#print(update.message)
		print(update)
		if update.message:  # your bot can receive updates without messages
			chat_id = update.message.chat_id
			player_info[chat_id] = update.message.from_user
			# Reply to the message
			if update.message.text.startswith("/start"):
				bot.send_message(chat_id = chat_id, text = "/join {gameid}".format(gameid = the_game.id), reply_markup=[])
				join_game(chat_id, the_game.id)
		elif update.callback_query:
			#from_id = update.callback_query.from_user.id
			from_id = update.callback_query.message.chat.id
			data = update.callback_query.data
			notif = None
			if from_id in player_gameids:
				notif = games[player_gameids[from_id]].handle_action(from_id, data)
			bot.answer_callback_query(callback_query_id=update.callback_query.id, text = notif)

def handle_old(bot):
	global update_id
	# Request updates after the last update_id
	for update in bot.getUpdates(offset=update_id, timeout=10):
		# chat_id is required to reply to any message
		update_id = update.update_id + 1
		#print(update.message)
		print(update)
		if update.message:  # your bot can receive updates without messages
			chat_id = update.message.chat_id
			player_info[chat_id] = update.message.from_user
			# Reply to the message
			if update.message.text.startswith("/start") and len(update.message.text.split()) == 1:
				bot.send_message(chat_id = chat_id,parse_mode="Markdown", text = "Welcome!\n`/create [GAMETYPE]`\t\t-create a game\n`/join [GAMEID]`\t-join a game\n`/leave`\t\t-leave game\n\n*Available game types:*\nresistance\nticktacktoe\nrockpaperscissors")
			elif update.message.text.startswith("/join") or update.message.text.startswith("/start join"):
				if update.message.text.startswith("/start join"):
					ss = ["/join", update.message.text[len("/start join_"):]]
				else:
					ss = update.message.text.split()
				if len(ss) < 2:
					bot.send_message(chat_id = chat_id, text = "Use\n/join [GAMEID]\n to join a game")
				else:
					if chat_id in player_gameids:
						bot.send_message(chat_id = chat_id, text = "You are already in a game!")
						continue
					try:
						gameid = ss[1]
						if gameid not in games:
							bot.send_message(chat_id = chat_id, text = "That game doesn't exist")
						else:
							join_game(chat_id, gameid)
					except ValueError:
						bot.send_message(chat_id = chat_id, text = "Id not valid")
			elif update.message.text.startswith("/create"):
				if chat_id in player_gameids:
					bot.send_message(chat_id = chat_id, text = "You are already in a game!")
					continue
				ss = update.message.text.split()
				if len(ss) < 2:
					gt = my_games.game_types[my_games.DEFAULT_GAME]
				else:
					if ss[1].lower() not in my_games.game_types:
						bot.send_message(chat_id = chat_id, text = "Game type doesn't exist.")
					else:
						gt = my_games.game_types[ss[1].lower()]
				gg = gt(update_view, leave_foo, creator=chat_id, player_info=player_info)
				games[gg.id] = gg
				bot.send_message(chat_id = chat_id, text = "Created game {gameid}".format(gameid = gg.id))
				buttons = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton(text = "Share", switch_inline_query = "")]])
				bot.send_message(chat_id = chat_id, text = "/join {gameid}".format(gameid = gg.id), reply_markup=buttons)
				join_game(chat_id, gg.id)
			elif update.message.text.startswith("/leave"):
				if chat_id not in player_gameids:
					bot.send_message(chat_id = chat_id, text = "You are not in a game!")
				else:
					gid = player_gameids[chat_id]
					games[gid].cancel()
					del games[gid]
				pass
		elif update.callback_query:
			#from_id = update.callback_query.from_user.id
			from_id = update.callback_query.message.chat.id
			data = update.callback_query.data
			notif = None
			if from_id in player_gameids:
				notif = games[player_gameids[from_id]].handle_action(from_id, data)
			bot.answer_callback_query(callback_query_id=update.callback_query.id, text = notif)
		elif update.inline_query:
			q = update.inline_query.query
			qid = update.inline_query.id
			fid = update.inline_query.from_user.id
			
			if q.startswith("join"):
				qs = "_".join(q.split())
				bot.answer_inline_query(inline_query_id = qid, results=[], switch_pm_text="Join game", switch_pm_parameter=qs, cache_time = 0, is_personal = True)
			elif fid not in player_info:
				bot.answer_inline_query(inline_query_id = qid, results=[], switch_pm_text="Start bot", switch_pm_parameter="start", cache_time = 0, is_personal = True)
			elif fid in player_gameids:
				gameid = player_gameids[fid]
				gt = games[gameid].type
				butts = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton(text = "Join", switch_inline_query_current_chat = "join " + gameid)]])
				results = [telegram.InlineQueryResultArticle(id=hex(getrandbits(64))[2:],
					title= "*" + str(gt) + "* " + str(gameid),
					reply_markup=butts,
					input_message_content = telegram.InputTextMessageContent(message_text="Play a game of *" + gt + "* with me!",
						parse_mode="Markdown"))]
				bot.answer_inline_query(inline_query_id = qid, results=results, cache_time = 0, is_personal = True)
			else:
				def makeres(gt):
					gameid = str(uuid.uuid4().hex)[:8]
					butts = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton(text = "Join", switch_inline_query_current_chat = "join " + gameid)]])
					return telegram.InlineQueryResultArticle(id= str(gt) + "_" + str(gameid),
						title= "Create new *" + str(gt) + "*",
						reply_markup = butts,
						input_message_content = telegram.InputTextMessageContent(message_text="Play a game of *" + gt + "* with me!",
							parse_mode="Markdown"))
				results = [makeres(gt) for gt in my_games.game_types.keys()]
				bot.answer_inline_query(inline_query_id = qid, results=results, cache_time = 0, is_personal = True)
		elif update.chosen_inline_result:
			rid = update.chosen_inline_result.result_id
			if "_" not in rid:
				continue
			chat_id = update.chosen_inline_result.from_user.id
			gt, gameid = rid.split("_")
			
			gg = my_games.game_types[gt](update_view, leave_foo, creator=chat_id, player_info=player_info)
			gg.id = gameid
			games[gg.id] = gg
			bot.send_message(chat_id = chat_id, text = "Created game {gameid}".format(gameid = gg.id))
			buttons = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton(text = "Share", switch_inline_query = "")]])
			bot.send_message(chat_id = chat_id, text = "/join {gameid}".format(gameid = gg.id), reply_markup=buttons)
			join_game(chat_id, gg.id)
		
def update_view(player:int, message_id:int, view:game.View):
	if view.buttons is None:
		buttons = None
	else:
		def process_button(but):
			return telegram.InlineKeyboardButton(text = but[1], callback_data = but[0])
		buttons = telegram.InlineKeyboardMarkup([[process_button(b) for b in l] for l in view.buttons])
	
	if message_id not in message_state or message_state[message_id] != view.text:
		res = bot.edit_message_text(chat_id = player, message_id = message_id, text = view.text, reply_markup = buttons, parse_mode="Markdown")
		message_state[message_id] = view.text
		button_state[message_id] = view.buttons
	elif message_id not in button_state or button_state[message_id] != view.buttons:
		res = bot.edit_message_reply_markup(chat_id = player, message_id = message_id, reply_markup = buttons)
		button_state[message_id] = view.buttons
	#print(res)
	
def leave_foo(player:int):
	gameid = player_gameids[player]
	del player_gameids[player]
	bot.send_message(chat_id = player, text = "You left the game!")


#if __name__ == '__main__':
#	main()

the_game_type = my_games.game_types[my_games.DEFAULT_GAME]
the_game = the_game_type(update_view, leave_foo, creator=0, player_info=player_info)
games[the_game.id] = the_game