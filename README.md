MusicSync
=========

Keeps my music synced between multiple computers, acting much like a revision control system.

Create index of all music. Map name to hash. Store in tree. Pickle tree on dump.
Create main interface. Take directory that will hold music, and take in pickle file. If no pickle file is specified, the program will save a pickle file of the directory to disk with current date as name. If pickle file is specified, load it and compare it to the directory. All differences are moved to new list. This new list is then split in to three parts: removed, moved, and added. Moved files are ones that do not exist in the original location anymore, but the hash shows up somewhere else new. Moved files are then moved to their new location, removed files are deleted off the hard drive, and added files are then dumped to a file. If a server is specified, download the added files from the server. Otherwise, end.
The program can also be started in pure download mode where it takes in an added file, and a server address.
Alternately, an ftp server, the path to the music library on the ftp server, and an added file can be specified, and it will fetch the files by path and check the hash when it finishes the download.

The server software can do two things: if the index is requested, it will rebuild the hash tree, pickle it, and then send that pickle file across the network. If a specific file is requested, then it locates it and sends it back. Ideally, it will have a cached copy of the music library.