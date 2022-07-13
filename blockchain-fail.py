from copyreg import constructor
from dataclasses import dataclass
import hashlib
import json

class Block:
    def __init__(self, index, timestamp, data, previousHash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.calculateHash()

    def calculateHash(self):
        return str(hashlib.sha256(str(self.index).encode('utf-8') + str(self.previousHash).encode('utf-8') + str(self.timestamp).encode('utf-8') + json.dumps(self.data).encode('utf-8')))

    def printBlock(self):
        return str(self.index) + " " + str(self.timestamp) + " " + str(self.data) + " " + str(self.previousHash) + " " + str(self.hash)


class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]
    
    def createGenesisBlock(self):
        return Block(0, "07/12/2022", "Genesis Block", "0")
    
    def getLatestBlock(self):
        return self.chain[len(self.chain) - 1]

    def addBlock(self, newBlock):
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.hash = newBlock.calculateHash()
        self.chain.append(newBlock)

sidCoin = Block(1, "07/12/2022", 4)
sidCoin.addBlock(Block(1, "07/12/2022", 4))
#sidCoin.addBlock(Block(2, "07/12/2022", 7))

print(sidCoin.printBlock())