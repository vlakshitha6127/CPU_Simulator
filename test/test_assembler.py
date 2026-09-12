from assembler.assembler import Assembler
from cpu.instruction import Instruction


def test_assembler_without_labels():
    assembler = Assembler()

    source = """
    LOAD R1, 10
    ADD R1, R2
    HALT
    """

    program = assembler.assemble(source)

    assert program == [
        Instruction("LOAD", ["R1", 10]),
        Instruction("ADD", ["R1", "R2"]),
        Instruction("HALT", [])
    ]


def test_assembler_with_label():
    assembler = Assembler()

    source = """
    CMP R1, R2
    BEQ EQUAL
    LOAD R3, 10
    HALT
    EQUAL:
    LOAD R3, 20
    HALT
    """

    program = assembler.assemble(source)

    assert assembler.labels["EQUAL"] == 4

    assert program[1] == Instruction(
        "BEQ",
        [4]
    )


def test_register_operands():
    assembler = Assembler()

    source = """
    ADD R1, R2
    """

    program = assembler.assemble(source)

    assert program[0] == Instruction(
        "ADD",
        ["R1", "R2"]
    )


def test_numeric_operands():
    assembler = Assembler()

    source = """
    LOAD R1, 25
    """

    program = assembler.assemble(source)

    assert program[0] == Instruction(
        "LOAD",
        ["R1", 25]
    )