class ControlUnit:
    def __init__(self, isa):
        self.isa = isa

    def decode(self, instruction):
        mnemonic = instruction.mnemonic

        if mnemonic not in self.isa["instructions"]:
            raise ValueError(f"Unknown instruction: {mnemonic}")

        return self.isa["instructions"][mnemonic]