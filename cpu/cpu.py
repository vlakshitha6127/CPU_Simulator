import json

from cpu.registers import Registers
from cpu.memory import Memory
from cpu.flags import Flags
from cpu.alu import ALU
from cpu.instruction import Instruction
from cpu.control_unit import ControlUnit


class CPU:
    def __init__(self):
        self.registers = Registers(count=8)
        self.memory = Memory(size=256)
        self.flags = Flags()
        self.alu = ALU(word_size=16)

        with open("isa/isa.json", "r") as file:
            self.isa = json.load(file)

        self.control_unit = ControlUnit(self.isa)

        self.halted = False

    def load_program(self, program):
        for address, instruction in enumerate(program):
            self.memory.write(address, instruction)

    def fetch(self):
        pc = self.registers.pc
        instruction = self.memory.read(pc)

        self.registers.ir = instruction
        self.registers.pc += 1

        return instruction

    def decode(self, instruction):
        return self.control_unit.decode(instruction)

    def execute(self, instruction):
        mnemonic = instruction.mnemonic
        operands = instruction.operands

        if mnemonic == "ADD":
            rd = self.get_register_number(operands[0])
            rs = self.get_register_number(operands[1])

            result = self.alu.add(
                self.registers.read(rd),
                self.registers.read(rs),
                self.flags
            )

            self.registers.write(rd, result)

        elif mnemonic == "SUB":
            rd = self.get_register_number(operands[0])
            rs = self.get_register_number(operands[1])

            result = self.alu.sub(
                self.registers.read(rd),
                self.registers.read(rs),
                self.flags
            )

            self.registers.write(rd, result)

        elif mnemonic == "AND":
            rd = self.get_register_number(operands[0])
            rs = self.get_register_number(operands[1])

            result = self.alu.AND(
                self.registers.read(rd),
                self.registers.read(rs),
                self.flags
            )

            self.registers.write(rd, result)

        elif mnemonic == "OR":
            rd = self.get_register_number(operands[0])
            rs = self.get_register_number(operands[1])

            result = self.alu.OR(
                self.registers.read(rd),
                self.registers.read(rs),
                self.flags
            )

            self.registers.write(rd, result)

        elif mnemonic == "XOR":
            rd = self.get_register_number(operands[0])
            rs = self.get_register_number(operands[1])

            result = self.alu.XOR(
                self.registers.read(rd),
                self.registers.read(rs),
                self.flags
            )

            self.registers.write(rd, result)

        elif mnemonic == "LOAD":
            rd = self.get_register_number(operands[0])
            address = operands[1]

            value = self.memory.read(address)
            self.registers.write(rd, value)

            self.update_memory_flags(value)

        elif mnemonic == "STORE":
            rs = self.get_register_number(operands[0])
            address = operands[1]

            value = self.registers.read(rs)
            self.memory.write(address, value)

        elif mnemonic == "CMP":
            rs1 = self.get_register_number(operands[0])
            rs2 = self.get_register_number(operands[1])

            self.alu.sub(
                self.registers.read(rs1),
                self.registers.read(rs2),
                self.flags
            )

        elif mnemonic == "JMP":
            self.registers.pc = operands[0]

        elif mnemonic == "BEQ":
            if self.flags.zero:
                self.registers.pc = operands[0]

        elif mnemonic == "BNE":
            if not self.flags.zero:
                self.registers.pc = operands[0]

        elif mnemonic == "HALT":
            self.halted = True

        else:
            raise ValueError(f"Unsupported instruction: {mnemonic}")

    def step(self):
        if self.halted:
            return

        instruction = self.fetch()
        self.decode(instruction)
        self.execute(instruction)

    def run(self):
        while not self.halted:
            self.step()

    def get_register_number(self, register_name):
        if not register_name.startswith("R"):
            raise ValueError(f"Invalid register: {register_name}")

        return int(register_name[1:])

    def update_memory_flags(self, value):
        self.flags.zero = (value == 0)
        self.flags.negative = bool(value & (1 << 15))

    def reset(self):
        self.registers.reset()
        self.memory.reset()
        self.flags.reset()
        self.halted = False