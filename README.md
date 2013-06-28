MusicSync
=========

Keeps my music synced between multiple computers, acting much like a revision control system.

Arguments
---------

 -host hosname or -h hostname : The host to connect to and compare music against. It will also upload music.
 
 -port # or -p #: Port on which to contact the host. Defaults to 7355.
 
 -hashtree path or -t path : location on disk of pickle file of music library to be used
 
 -folder path or -f path: Location on disk where files will loaded and downloaded.
 
 -download false or -d false: option to download the files. Defaults to true.
 
 -delete false or -x false: If files should be removed if they don't exist anymore. Defaults to true.
 
 -add path or -a path: Location of added files. This can be used to continue downloading if it gets interupted.
 
 -keep or -k: Instructs the program to generate a local hashtree of your music folder

 -server or -s: Instructs the program to host music for download.

Example usage
-------------

To compare your music folder against the server's music folder, and then download the music you are missing:
python musicSync.py -f /home/username/music -h music.hostname.com

To set your computer to host music for other machines:
python musicSync.py -s -f /home/username/music

To host on port 9000:
python musicSync.py -s -f /home/username/music -p 9000

To compare your music folder against the server's music folder but to not download the new music or delete music that has been removed:
python musicSync.py -f /home/username/music -h music.hostname.com -d false -x false

To download music from a previous compare:
python musicSync.py -f /home/username/music -h music.hostname.com -a /home/username/time.added

To compare previously generated local hashtree against your music folder:
python musicSync.py -f /home/username/music -t /home/username/time.p

To generate a local copy of your music folder:
python musicSync.py -k -f /home/username/music



