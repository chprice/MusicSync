MusicSync
=========

Keeps my music synced between multiple computers, acting much like a revision control system.

# possible command line args:
# -host hosname or -h hostname : host who has the pickle and music to be downloaded
# -port # or -p: port on which to contact the host. Defaults to 7355.
# -hashtree path or -t path : location on disk of pickle file to be used
# -download false or -d false: option to download the files. Defaults to true.
# -folder path or -f path: location on disk where files will be downloaded to and compared to
# -delete false or -x false: if files should be removed if they don't exist anymore. Defaults to true.
# -add path or -a path: location of added files to fetch. Requires host and path to be specified.

# -server or -s: instructs the program to host music for download. Requires path. If port is specified, use it. Otherwise default to 7355.