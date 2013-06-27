import os
import time
import re
import hashlib
import sys

def makeHash(fileName): #given a filename and path, computes hash of file
    tHash = hashlib.sha256()
    somefile = open(fileName, 'rb')
    tempString = somefile.readline()
    while(len(tempString)!=0):
        tHash.update(tempString)
        tempString = somefile.readline()
    return tHash.hexdigest()

class tree():
    def __init__(self, path):
        self.hashtable = dict()
        self.addChild(path)
    def addChild(self, path):
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
        for phile in files:
            if(len(re.findall(".*(mp3|wav|mp4)+", phile)) != 0):
                self.hashtable[makeHash(os.path.join(path, phile))] = os.path.join(path, phile)
        for folder in folders:
            self.addChild(os.path.join(path, folder))
    def compare(self, otherTree):
        actions = {"added": [], "moved": [], "removed": []}
        for fileHash in self.hashtable:
            if(fileHash in otherTree.hashtable):
                if(self.hashtable[fileHash] == otherTree.hashtable[fileHash]):
                    quiet = otherTree.hashtable.pop(fileHash) # remove the found file so it is not marked as 'added'
                else:
                    actions["moved"].append([fileHash, self.hashtable[fileHash], otherTree.hashtable[fileHash]]) # file hash, old location, new location
                    quiet = otherTree.hashtable.pop(fileHash)
            else:
                actions["removed"].append([fileHash, self.hashtable[fileHash]]) # file hash, location of file
        for fileHash in otherTree.hashtable:
            actions["added"].append([fileHash, otherTree.hashtable[fileHash]]) # file hash, location of file
        return actions

def buildTree(path):
    print "Building tree of", path
    start = time.clock()
    trie = tree(path)
    print "Done building tree. Time taken: ", time.clock()-start, " Size is: ", len(trie.hashtable)
    return trie

def dumpTree(tree):
    curTime = datetime.datetime.now()
    date = str(curTime.month) + "-" + str(curTime.day)+ "-" + str(curTime.year)
    pickle.dump( trie , open( date+".p", "wb" ))

def loadTree(path):
    return pickle.load( open( path, "rb" ) )

def dumpAdded(actions):
    curTime = datetime.datetime.now()
    date = str(curTime.month) + "-" + str(curTime.day)+ "-" + str(curTime.year)
    fh = open(date + ".added", "w") 
    for fileData in actions["added"]:
        fh.write(fileData[0] + "," + fileData[1] + "\n")

def loadAdded(path):
    fh = open(path, "r")
    fileData = []
    for line in fh:
        a, b = line.split(",")
        fileData.append([a,b])
    fh.close()
    return fileData

def downloadTree(host, port):

def downloadSongs(host, port, actions):

def serveFiles(port):
    

# possible command line args:
# -host hosname or -h hostname : host who has the pickle and music to be downloaded
# -port # or -p: port on which to contact the host. Defaults to 7355.
# -hashtree path or -t path : location on disk of pickle file to be used
# -download false or -d false: option to download the files. Defaults to true.
# -folder path or -f path: location on disk where files will be downloaded to and compared to
# -delete false or -x false: if files should be removed if they don't exist anymore. Defaults to true.
# -add path or -a path: location of added files to fetch. Requires host and path to be specified.

# -server or -s: instructs the program to host music for download. Requires path. If port is specified, use it. Otherwise default to 7355.


args = sys.argv[1:][::-1]
hasHost, hasPort, hasDump, hasFolder, hasAdd, download, delete, isServer  = False, False, False, False, False, False, False, False
while(len(args) != 0):
    flag = args.pop()
    if(flag == "-h" or flag == "-host"):
        hostname = args.pop()
        hasHost = True
    if(flag == '-p' or flag == '-port'):
        port = args.pop()
        hasPort = True
    if(flag == '-t' or flag == '-hashtree'):
        hashDump = args.pop()
        hasDump = True
    if(flag == '-f' or flag == '-folder'):
        folder = args.pop()
        hasFolder = True
    if(flag == '-a' or flag == '-add'):
        addedFile = args.pop()
        hasAdd = True
        
    if(flag == '-d' or flag == '-download'):
        b = args.pop()
        download = (b == 't' or b == 'true')
    if(flag == '-x' or flag == '-delete'):
        b = args.pop()
        delete = (b == 't' or b == 'true')
    if(flag == '-s' or flag == '-server'):
        isServer = True


if(not hasPort):
    port = 7355
if(isServer):
    serveFiles(port)
if(hasAdd and hasHost):
    actions = {}
    actions["added"] = loadAdded(path)
    downloadSongs(host, port, actions)
    sys.exit(0)
if(not hasAdd and not hasFolder):
    print "Folder not defined"
    sys.exit(1)
if(hasDump):
    old = buildTree(folder)
    new = loadTree(hashDump)
    actions = old.compare(new)
    for fileData in actions["moved"]:
        os.rename(fileData[1], fileData[2])
    if(delete):
        for fileData in actions["removed"]:
            os.remove(fileData[1])
    if(hasHost):
        if(download):
            downloadSongs(host, port, actions)
            sys.exit(0)
        else:
            dumpAdded(actions)
            sys.exit(0)
    else:
        dumpAdded(actions)
        sys.exit(0)
if(hasHost):
    new = downloadTree(host, port)
    old = buildTree(folder)
    actions = old.compare(new)
    if(delete):
        for fileData in actions["removed"]:
            os.remove(fileData[1])
    if(download):
        downloadSongs(host, port, actions)
        sys.exit(0)
    else:
        dumpAdded(actions)
        sys.exit(0)
    

#path = "C:\\.D\\Music"
