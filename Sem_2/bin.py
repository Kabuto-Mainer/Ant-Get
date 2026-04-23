def decimal_to_bits(value: int, bits: int) -> list[int]:
    """Преобразовать число в список битов от старшего к младшему."""
    return [(value >> i) & 1 for i in range(bits - 1, -1, -1)]

def bits_to_dec(bits: list[int]):
    num = 0
    counter = 0
    for i in bits:
        num += i * 2**counter
        counter += 1

    return num

def decimal2binary(value):

    return [int(bit) for bit in bin(value)[2:].zfill(8)]

# print(decimal_to_bits(277, 10))
print(bits_to_dec(reversed([1,0,1,0,1,0,1,0])))
