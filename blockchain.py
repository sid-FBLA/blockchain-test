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

    def updateHash(*args):
        hashText = ""
        hash = hashlib.sha256()
        for arg in args
            hashText += str(arg)

        hash.update(hashText.encode('utf-8'))
        return hash.hexdigest()

print(updateHash("Sid"))

    def calculateHash():
