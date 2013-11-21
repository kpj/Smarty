smartPlaylist
=============

Smart playlist generator for mpd

Usage
-----
    usage: mpd_smart_playlist.py [-h] [-i <ip>] [-p <port>] [--maxnum <num>] [--dist <num>] [--norepeat]

    Smart playlist generator written in python.

    optional arguments:
       -h, --help            show this help message and exit
       -i <ip>, --ip <ip>    IP address of mpd server
       -p <port>, --port <port>
                             Port mpd server is listening on
       --maxnum <num>        Maximal number of songs in playlist
       --dist <num>          Choose new song if only <x> songs are left in current
                             playlist
       --norepeat            Don't add songs which are already in playlist.
