import json

from cpu.instruction import Instruction


class Assembler:
    def __init__(self):
        with open("isa/isa.json", "r") as file:
            self.isa = json.load(file)

        self.labels = {}

    def assemble(self, source):
        lines = source.splitlines()

        self.first_pass(lines)

        program = self.second_pass(lines)

        return program

    def first_pass(self, lines):
        address = 0

        for line in lines:
            line = line.strip()

            if not line:
                continue

            if line.endswith(":"):
                label = line[:-1]
                self.labels[label] = address
            else:
                address += 1

    def second_pass(self, lines):
        program = []

        for line in lines:
            line = line.strip()

            if not line or line.endswith(":"):
                continue

            parts = line.replace(",", " ").split()

            mnemonic = parts[0].upper()
            operands = parts[1:]

            operands = self.convert_operands(operands)

            program.append(
                Instruction(mnemonic, operands)
            )

        return program

    def convert_operands(self, operands):
        converted = []

        for operand in operands:
            if operand in self.labels:
                converted.append(self.labels[operand])

            elif operand.startswith("R"):
                converted.append(operand.upper())

            else:
                converted.append(int(operand))

        return converted