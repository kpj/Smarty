Smarty
======

.. image:: https://pypip.in/v/smarty/badge.png
	:target: https://crate.io/packages/smarty/
	:alt: Latest version
	
.. image:: https://pypip.in/d/smarty/badge.png
	:target: https://crate.io/packages/smarty/
	:alt: Number of PyPI downloads

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

	usage: smarty [-h] [-i <ip>] [-p <port>] [--maxnum <num>] [--dist <num>]
			[--norepeat] [-v] [--exclude <genre> [<genre> ...]]


	Smart playlist generator written in python.

	optional arguments:
	  -h, --help            show this help message and exit
	  -i <ip>, --ip <ip>    IP address of mpd server
	  -p <port>, --port <port>
				Port mpd server is listening on
	  --maxnum <num>        Maximal number of songs in playlist
	  --dist <num>          Add new song if only <x> songs are left to play in current playlist
	  --norepeat            Don't add songs which are already in playlist.
	  -v, --verbose         Print information about running process
	  --exclude <genre> [<genre> ...]
				Never add these genres to playlist


Example
-------

Smarty could be used like this

::

    smarty --norepeat --maxnum 3000 --verbose --exclude Comedy

This would only add songs which are not already in the current playlist, allow a maximum number of 3000 songs (deletes from the beginning if that number is exceeded). It will furthermore display the genre of each added song and not add the genre 'Comedy'.


Bug Reports
-----------
Please submit any bugs you find to https://github.com/kpj/Smarty/issues.


Links
-----
- Github: https://github.com/kpj/Smarty
- PyPi Homepage: https://pypi.python.org/pypi/smarty
