#!/Library/Frameworks/Python.framework/Versions/3.6/bin

import sys
import json

assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

with open('gulag.json') as json_data:
	world = json.load(json_data)

def get_response(response):
	try :
		return int(response)-1
	except ValueError:
		return -1

def print_response(count,responses):
	return str(count + 1)

def check_quit(response):
	response = str(response)
	if response.lower() == 'q' or response.lower == 'quit':
		return True
	return False

location = 'gulag_intro'

game_is_running = True
while game_is_running:
	current = world[location]
	print(current['description'])
	if len(current['options']) == 0:
		continue
	for count,option in enumerate(current['options']):
		print('[' + print_response(count,current['options']) + '] ' + option['option'])
	print('[q] to quit')
	response = input('What do you do?')
	if check_quit(response):
		game_is_running = False
		continue
	response = get_response(response)
	for count,option in enumerate(current['options']):
		if (response == count):
			location = option['goto']