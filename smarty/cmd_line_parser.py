import argparse, os

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
	help="Add new song if only <x> songs are left to play in current playlist",
	type=int,
	metavar="<num>",
	dest="songs_to_end",
	default=5
)
parser.add_argument(
	"--norepeat",
	help="Don't add songs which are already in playlist.",
	action="store_true"
)

def get_args():
	return parser.parse_args()