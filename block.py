from time import time
from util.printable import Printable


class Block(Printable):

    def __init__(self, index, previous_hash, transactions, proof, timestamp=time()):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time() if timestamp is None else timestamp
        self.transactions = transactions
        self.proof = proof
