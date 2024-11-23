from block import Block
from datetime import datetime

class Blockchain:
    def __init__(self):
        self.chain = [Block(0, datetime.now().timestamp(), 'Genesis Block', '0')]

    def get_previous_hash(self):
        return self.chain[-1].hash

    def is_valid(self, block):
        current_block = self.chain[-1]

        if current_block.index + 1 != block.index:
            return False
        elif block.previous_hash != current_block.hash:
            return False
        elif block.hash != block.calculate_hash():
            return False

        return True

    def add_block(self, data):
        timestamp = datetime.now().timestamp()
        index = len(self.chain)
        previous_hash = self.get_previous_hash()
        new_block = Block(index, timestamp, data, previous_hash)

        if self.is_valid(new_block):
            self.chain.append(new_block)
        else:
            print('ERROR: Block is invalid!')

    def print_blockchain(self):
        for block in self.chain:
            print(f'{block.index}  {block.real_time()}')
            print(block.data)
            print(block.hash)
            print()
