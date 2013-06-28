MusicSync
=========

Keeps my music synced between multiple computers, acting much like a revision control system.

The program works by creating a hashmap of the locations of the MP3, MP4, and WAV files in a directory. It then compares
two hashmaps together to determine which files need to be moved, deleted, or downloaded. If the user specifies a server,
the program can even go download the songs that are missing.

Arguments
---------

 -h, -host hosname
    The host to connect to and compare music against. It will also upload music.
 
 -p, -port #
    Port on which to contact the host. Defaults to 7355.
 
 -t, -hashtree path
    Location on disk of pickle file of music library to be used.
 
 -f, -folder path
    Location on disk where files will loaded and downloaded.
 
 -d, -download false
    Option to download the files. Defaults to true.
 
 -x, -delete false
    If files should be removed if they don't exist anymore. Defaults to true.
 
 -a, -add path
    Location of added files. This can be used to continue downloading if it gets interupted.
 
 -k, -keep
    Instructs the program to generate a local hashtree of your music folder

 -s, server
    Instructs the program to host music for download.

Example usage
-------------

**To compare your music folder against the server's music folder, and then download the music you are missing:**
```
python musicSync.py -f /home/username/music -h music.hostname.com
```

**To set your computer to host music for other machines:**
```
python musicSync.py -s -f /home/username/music
```

**To host on port 9000:**
```
python musicSync.py -s -f /home/username/music -p 9000
```

**To compare your music folder against the server's music folder but to not download the new music or delete music that has been removed:**
```
python musicSync.py -f /home/username/music -h music.hostname.com -d false -x false
```

**To download music from a previous compare:**
```
python musicSync.py -f /home/username/music -h music.hostname.com -a /home/username/time.added
```

**To compare previously generated local hashtree against your music folder:**
```
python musicSync.py -f /home/username/music -t /home/username/time.p
```

**To generate a local copy of your music folder:**
```
python musicSync.py -k -f /home/username/music
```


