import os
import time
import re
import hashlib

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
        

path = "C:\\.D\\Music"
if(): # TODO not downloading
    print "Building tree of", path # TODO figure out path
    start = time.clock()
    trie = tree(path)
    print "Done building tree. Time taken: ", time.clock()-start, " Size is: ", len(trie.hashtable)
    if(): # TODO is dumping pickle file
        pickle.dump( trie , open( "time.p", "wb" ) ) # TODO figure out today's date from datetime
    else:
        newTree = pickle.load( open( picklePath, "rb" ) ) # TODO load pickle file
        actions = trie.compare(newTree)
        if(): # TODO figure out if we're doing deletions
            for fileData in actions["removed"]:
                os.remove(fileData[1])
        for fileData in actions["moved"]:
            os.rename(fileData[1], fileData[2])
        
        if(): # TODO figure out if we're doing dump
            fh = open("time.added", "w") # TODO figure out today's date from datetime
            for fileData in actions["added"]:
                fh.write(fileData[0] + "," + fileData[1] + "\n")
        else:
            # connect to server, and download everything to path
                
