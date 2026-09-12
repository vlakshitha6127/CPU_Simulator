from cpu.cpu import CPU
from cpu.instruction import Instruction


cpu = CPU()

program = [
    Instruction("CMP", ["R1", "R2"]),   # 0
    Instruction("BNE", [4]),            # 1
    Instruction("LOAD", ["R3", 10]),    # 2
    Instruction("JMP", [5]),            # 3
    Instruction("LOAD", ["R3", 20]),    # 4
    Instruction("HALT", [])             # 5
]

cpu.registers.write(1, 10)
cpu.registers.write(2, 20)

cpu.load_program(program)
cpu.run()

print("R1 =", cpu.registers.read(1))
print("R2 =", cpu.registers.read(2))
print("R3 =", cpu.registers.read(3))
print("Z =", cpu.flags.zero)
print("PC =", cpu.registers.pc)
print("HALTED =", cpu.halted)