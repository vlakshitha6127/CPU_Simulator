class Flags:
    def __init__(self):
        self.zero = False
        self.carry = False
        self.negative = False
        self.overflow = False

    def reset(self):
        self.zero = False
        self.carry = False
        self.negative = False
        self.overflow = False