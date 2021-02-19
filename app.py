import time
import vk_api

# python3 app.py <start_phrase> <stop_phrase>
from sys import argv
from os import environ
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-currently-playing"


spotify = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope, username="main"))

start_phrase = argv[1]
stop_phrase = argv[2]

# Получить токен можно здесь: https://vkhost.github.io
vk_session = vk_api.VkApi(token=environ.get('VK_TOKEN'), app_id=2685278)
vk = vk_session.get_api()

def clear_status(vk):
	vk.status.set(text="")


def set_status(vk, status):
	vk.status.set(text=status)


results = spotify.current_user_playing_track()
previous = {'item': {'uri': ''}}

def track_songs():
	not_playing = 0
	while True:
		if vk.status.get().get('text') != stop_phrase:
			global previous
			results = spotify.current_user_playing_track()
			if results['is_playing']:
				not_playing = 0
				if results.get('item').get('uri') != previous.get('item').get('uri'):
					print(results['item']['uri'])
					try:
						print(previous.get('item').get('uri'))
					except:
						pass
					try:
						set_status(vk, "📻 Слушаю трек «{}» от {} в Спотифай | {}".format(results['item']['name'],
						 results['item']['artists'][0]['name'], results['item']['external_urls']['spotify']))
						previous = spotify.current_user_playing_track()
					except Exception as e:
						print(e)
						time.sleep(11)
						continue
			else:
				not_playing+=1
				if not_playing >= 2:
					clear_status(vk)
					check_for_on()
		else:
			check_for_on()
		time.sleep(10)

def check_for_on():
	while True:
		if vk.status.get().get('text') == '!' or start_phrase in vk.status.get().get('text'):
			track_songs()
			break
		else:
			print(vk.status.get().get('text'))
		time.sleep(30)

check_for_on()