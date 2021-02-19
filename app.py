import time
from telethon import TelegramClient, events, sync


import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-currently-playing"


spotify = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope, username="main"))




results = spotify.current_user_playing_track()
previous = {'item': {'uri': ''}}

def track_songs():
	not_playing = 0
	while True:
		if vk.status.get().get('text') != 'ъеъ':
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
						set_status(vk, "📻 Слушаю трек «{}» от {} в Спотифай | {}".format(results['item']['name'], results['item']['artists'][0]['name'], results['item']['external_urls']['spotify']))
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
		if vk.status.get().get('text') == '!' or 'Слушаю' in vk.status.get().get('text'):
			track_songs()
			break
		else:
			print(vk.status.get().get('text'))
		time.sleep(30)

check_for_on()