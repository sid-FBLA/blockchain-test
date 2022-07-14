from copyreg import constructor
from dataclasses import dataclass
from datetime import date
import hashlib
import json

def updateHash(*args):
    hashText = ""
    hash = hashlib.sha256()
    for arg in args:
        hashText += str(arg)

    hash.update(hashText.encode('utf-8'))
    return hash.hexdigest()

print(updateHash("Sid"))


class Block:
    def __init__(self, data):
        self.nonce = 0
        self.timestamp = str(date.today())
        self.data = data
        self.previousHash = "0" * 64
        self.hash = self.calculateHash()

    def calculateHash(self):
        return updateHash(self.nonce, self.timestamp, self.data, self.previousHash)

    def __str__(self):
        return str(
            "Nonce: " + str(self.nonce) + "\n" +
            "Timestamp: " + self.timestamp + "\n" +
            "Data: " + self.data + "\n" +
            "Hash: " + str(self.hash) + "\n"
            "Previous Hash: " + self.previousHash)


    def getHash(self):
        return self.hash

class BlockChain:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.chain = []

    def addBlock(self, block):
        self.chain.append(block)

    def mineBlock(self, block):
        try:
            block.previousHash = self.chain[-1].getHash()
        except IndexError:
            pass

        while True:
            if block.calculateHash()[:self.difficulty] == "0" * self.difficulty:
                block.hash = block.calculateHash()
                self.addBlock(block)
                break
            else:
                block.nonce += 1

blockchain = BlockChain(4)
database = ["Audienceology", "Crypto", "Ad Fraud", "BlockChain for Ad Fraud"]
for data in database:
    blockchain.mineBlock(Block(data))
for block in blockchain.chain:
    print(block)
