def to_bin(n):
    """Integer -> 8-bit two's complement string."""
    return format(n & 0xFF, '08b')

def to_dec(bits):
    """8-bit two's complement string -> signed integer."""
    v = int(bits, 2)
    return v - 256 if bits[0] == '1' else v

def negate(bits):
    """Two's complement negation: invert all bits, then add 1."""
    inverted = ''.join('1' if b == '0' else '0' for b in bits)
    return to_bin(int(inverted, 2) + 1)

def add(a, b):
    total = int(a, 2) + int(b, 2)
    carry_out = total >> 8
    result = to_bin(total)
    # Overflow: both operands have the same sign but the result differs
    overflow = (a[0] == b[0]) and (result[0] != a[0])
    return result, carry_out, overflow

def subtract(a, b):
    # A - B = A + (two's complement of B)
    result, carry_out, _ = add(a, negate(b))
    # Overflow: operands have different signs and the result sign differs from A
    overflow = (a[0] != b[0]) and (result[0] != a[0])
    return result, carry_out, overflow

def run(label, x, y, op):
    a, b = to_bin(x), to_bin(y)
    print(f"\n=== {label} ===")
    print(f"Operand 1 ({x:+d}) : {a}")
    print(f"Operand 2 ({y:+d}) : {b}")
    if op == '+':
        result, carry, ov = add(a, b)
        expected = x + y
    else:
        print(f"Two's complement of operand 2 (-({y:+d})): {negate(b)}")
        result, carry, ov = subtract(a, b)
        expected = x - y
    print(f"Result (binary)  : {result}")
    print(f"Result (decimal) : {to_dec(result)}")
    print(f"Carry out        : {carry}")
    print(f"Overflow         : {'YES' if ov else 'NO'}")
    ok = (to_dec(result) == expected) and not ov
    print(f"Expected {expected}, verification: {'PASS' if ok else 'FAIL / overflow'}")

run("a) +46 + (+29)", 46, 29, '+')
run("b) (-48) - (-23)", -48, -23, '-')