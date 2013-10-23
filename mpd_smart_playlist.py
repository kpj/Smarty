import random
import os
import time
import atexit

import mpd


# settings
mpd_ip = os.getenv("MPD_HOST")
mpd_port = 6600

songs_to_end = 5 # choose new song when only x are left in playlist
max_num = 3000 # maximal number of songs in playlist


# open connection
client = mpd.MPDClient()
client.connect(mpd_ip, mpd_port)

# helper functions
def parse_playlist():
	"""Order playlist dependent on genre
	"""
	genres = {}
	for song in client.playlistinfo():
		if "genre" in song.keys():
			g = song["genre"]
			if type(g) == type([]):
				g = g[0]
			genres.setdefault(g, []).append(song["file"])
	return genres

def get_smart_genre(genres):
	"""Returns some genre from playlist. The more often one genre appears the more likely it is to be added
	"""
	totals = []
	running_total = 0
	for k in genres.keys():
		running_total += len(genres[k])
		totals.append(running_total)

	rnd = random.random() * running_total
	for i, total in enumerate(totals):
		if rnd < total:
			return list(genres.keys())[i]

def get_song(genre):
	"""Returns path to random song of given genre
	"""
	songs = client.find("genre", genre)
	if len(songs) > 0:
		return random.choice(songs)["file"]
	else:
		return None

def add_song(path):
	"""Adds song specified by file path to current playlist
	"""
	client.add(path)

def rm_song(pos):
	"""Removes song at given position from playlist.
	First song in playlist has position 0
	"""
	client.delete(pos)

def disable_random():
	"""Disables random playing of songs from playlist
	"""
	client.random(0)

def get_playlist_pos():
	"""Returns current position in and length of playlist
	"""
	cs = client.status()
	return (int(cs["song"]) + 1, int(cs["playlistlength"]))

def save_current_settings():
	"""Saves current mpd settings to allow later restoration
	"""
	return client.status()

def restore_previous_settings(settings):
	"""Set important parameters to previous values
	"""
	client.random(settings["random"])

	client.close()
	client.disconnect()

	print("Shutting down")

# init
if __name__ == "__main__":
	atexit.register(restore_previous_settings, save_current_settings())
	disable_random()

	wait = 1
	while True:
		pos, total = get_playlist_pos()
		if total > max_num:
			for i in range(total - max_num):
				rm_song(0)
		if total - pos < songs_to_end:
			playlist = parse_playlist()
			next_genre = get_smart_genre(playlist)
			print("Adding %s" % next_genre)
			add_song(get_song(next_genre))

			wait = 0.5
		else:
			wait = 10

		time.sleep(wait)
