class Memory:
    def __init__(self, size=256):
        self.data = [0] * size

    def read(self, address):
        return self.data[address]

    def write(self, address, value):
        self.data[address] = value

    def reset(self):
        self.data = [0] * len(self.data)