class ALU:
    def __init__(self, word_size=16):
        self.word_size = word_size
        self.max_value = (1 << word_size) - 1

    def update_flags(self, result, flags):
        flags.zero = (result == 0)
        flags.negative = bool(result & (1 << (self.word_size - 1)))

    def add(self, a, b, flags):
        full_result = a + b
        result = full_result & self.max_value

        flags.carry = full_result > self.max_value

        sign_a = bool(a & (1 << (self.word_size - 1)))
        sign_b = bool(b & (1 << (self.word_size - 1)))
        sign_result = bool(result & (1 << (self.word_size - 1)))

        flags.overflow = (
            sign_a == sign_b and sign_a != sign_result
        )

        self.update_flags(result, flags)

        return result

    def sub(self, a, b, flags):
        result = (a - b) & self.max_value

        flags.carry = a >= b

        sign_a = bool(a & (1 << (self.word_size - 1)))
        sign_b = bool(b & (1 << (self.word_size - 1)))
        sign_result = bool(result & (1 << (self.word_size - 1)))

        flags.overflow = (
            sign_a != sign_b and sign_a != sign_result
        )

        self.update_flags(result, flags)

        return result

    def AND(self, a, b, flags):
        result = a & b

        flags.carry = False
        flags.overflow = False

        self.update_flags(result, flags)

        return result

    def OR(self, a, b, flags):
        result = a | b

        flags.carry = False
        flags.overflow = False

        self.update_flags(result, flags)

        return result

    def XOR(self, a, b, flags):
        result = a ^ b

        flags.carry = False
        flags.overflow = False

        self.update_flags(result, flags)

        return result