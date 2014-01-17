import os, random


def set_client(c):
	"""Set client for use in rest of file
	"""
	global client
	client = c

def set_args(a):
	"""Set cmd-line args for use in rest of file
	"""
	global args
	args = a

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
	# filter out excluded genres
	genres = {genre: files for genre, files in genres.items() if not genre in args.exclude}

	# select genre
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
	while len(songs) > 0:
		song = random.choice(songs)
		if not args.norepeat or not in_playlist(song):
			return song["file"]
		else:
			songs.remove(song)
	return None

def in_playlist(new_song):
	"""Checks if given song is already in playlist
	"""
	if len(client.playlistsearch("file", new_song["file"])) == 0:
		return False
	return True

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
	if "song" in cs.keys():
		return (int(cs["song"]) + 1, int(cs["playlistlength"]))
	else:
		return (-1, int(cs["playlistlength"]))

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

	if args.verbose: print("Shutting down")
