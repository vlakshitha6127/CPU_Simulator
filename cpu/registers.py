class Registers:
    def __init__(self, count=8):
        self.registers = [0] * count
        self.pc = 0
        self.ir = None

    def read(self, register_number):
        return self.registers[register_number]

    def write(self, register_number, value):
        self.registers[register_number] = value

    def reset(self):
        self.registers = [0] * len(self.registers)
        self.pc = 0
        self.ir = None