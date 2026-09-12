from cpu.cpu import CPU
from cpu.instruction import Instruction


def test_add():
    cpu = CPU()

    cpu.registers.write(1, 10)
    cpu.registers.write(2, 20)

    program = [
        Instruction("ADD", ["R1", "R2"]),
        Instruction("HALT", [])
    ]

    cpu.load_program(program)
    cpu.run()

    assert cpu.registers.read(1) == 30


def test_sub():
    cpu = CPU()

    cpu.registers.write(1, 20)
    cpu.registers.write(2, 5)

    program = [
        Instruction("SUB", ["R1", "R2"]),
        Instruction("HALT", [])
    ]

    cpu.load_program(program)
    cpu.run()

    assert cpu.registers.read(1) == 15


def test_load_store():
    cpu = CPU()

    cpu.memory.write(10, 42)

    program = [
        Instruction("LOAD", ["R1", 10]),
        Instruction("STORE", ["R1", 20]),
        Instruction("HALT", [])
    ]

    cpu.load_program(program)
    cpu.run()

    assert cpu.registers.read(1) == 42
    assert cpu.memory.read(20) == 42


def test_cmp_equal():
    cpu = CPU()

    cpu.registers.write(1, 10)
    cpu.registers.write(2, 10)

    program = [
        Instruction("CMP", ["R1", "R2"]),
        Instruction("HALT", [])
    ]

    cpu.load_program(program)
    cpu.run()

    assert cpu.flags.zero is True


def test_beq():
    cpu = CPU()

    cpu.registers.write(1, 10)
    cpu.registers.write(2, 10)

    program = [
        Instruction("CMP", ["R1", "R2"]),
        Instruction("BEQ", [4]),
        Instruction("LOAD", ["R3", 10]),
        Instruction("HALT", []),
        Instruction("LOAD", ["R3", 20]),
        Instruction("HALT", [])
    ]

    cpu.load_program(program)
    cpu.run()

    assert cpu.registers.read(3) == 20


def test_bne():
    cpu = CPU()

    cpu.registers.write(1, 10)
    cpu.registers.write(2, 20)

    program = [
        Instruction("CMP", ["R1", "R2"]),
        Instruction("BNE", [4]),
        Instruction("LOAD", ["R3", 10]),
        Instruction("HALT", []),
        Instruction("LOAD", ["R3", 20]),
        Instruction("HALT", [])
    ]

    cpu.load_program(program)
    cpu.run()

    assert cpu.registers.read(3) == 20


def test_jmp():
    cpu = CPU()

    program = [
        Instruction("JMP", [3]),
        Instruction("LOAD", ["R1", 10]),
        Instruction("HALT", []),
        Instruction("LOAD", ["R1", 50]),
        Instruction("HALT", [])
    ]

    cpu.load_program(program)
    cpu.run()

    assert cpu.registers.read(1) == 50


def test_halt():
    cpu = CPU()

    program = [
        Instruction("HALT", [])
    ]

    cpu.load_program(program)
    cpu.run()

    assert cpu.halted is True