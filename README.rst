Smarty
======

A smart playlist generator for MPD written in python.


Installation
------------
Using pip
+++++++++
::

	$ pip install smarty

Using easy_install
++++++++++++++++++
::

	$ easy_install smarty


Usage
-----

In default configuration, smarty will try to use ``$MPD_HOST`` (environment variable) and port ``6600``. If ``$MPD_HOST`` is not set, it will use localhost.

::

	usage: smarty [-h] [-i <ip>] [-p <port>] [--maxnum <num>] [--dist <num>] [--norepeat]

	Smart playlist generator written in python.

	optional arguments:
	   -h, --help            show this help message and exit
	   -i <ip>, --ip <ip>    IP address of mpd server
	   -p <port>, --port <port>
				 Port mpd server is listening on
	   --maxnum <num>        Maximal number of songs in playlist
	   --dist <num>          Choose new song if only <x> songs are left to play in current playlist
	   --norepeat            Don't add songs which are already in playlist.


Bug Reports
-----------
Please submit any bugs you find to https://github.com/kpj/Smarty/issues.


Links
-----
- Github: https://github.com/kpj/Smarty
- PyPi Homepage: https://pypi.python.org/pypi/smarty
- Travis CI: https://travis-ci.org/kpj/Smarty