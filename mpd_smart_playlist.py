import random
import os
import time
import atexit
import argparse

import mpd


# handle cmdline-arguments
parser = argparse.ArgumentParser(description="Smart playlist generator written in python.")
parser.add_argument(
        "-i",
        "--ip",
        help="IP address of mpd server",
        type=str,
        metavar="<ip>",
        default=os.getenv("MPD_HOST", "localhost")
)
parser.add_argument(
        "-p",
        "--port",
        help="Port mpd server is listening on",
        type=int,
        metavar="<port>",
        default=6600
)
parser.add_argument(
        "--maxnum",
        help="Maximal number of songs in playlist",
        type=int,
        metavar="<num>",
        dest="max_num",
        default=50
)
parser.add_argument(
        "--dist",
        help="Choose new song if only <x> songs are left in current playlist",
        type=int,
        metavar="<num>",
        dest="songs_to_end",
        default=5
)
args = parser.parse_args()


# open connection
client = mpd.MPDClient()
client.connect(args.ip, args.port)

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

        print("Shutting down")

# init
if __name__ == "__main__":
        atexit.register(restore_previous_settings, save_current_settings())
        disable_random()

        wait = 1
        while True:
                pos, total = get_playlist_pos()
                if total > args.max_num:
                        for i in range(total - args.max_num):
                                rm_song(0)
                if pos != -1 and total - pos < args.songs_to_end:
                        playlist = parse_playlist()
                        next_genre = get_smart_genre(playlist)
                        print("Adding %s" % next_genre)
                        add_song(get_song(next_genre))
                        del playlist

                        wait = 0.5
                else:
                        wait = 10

                time.sleep(wait)
