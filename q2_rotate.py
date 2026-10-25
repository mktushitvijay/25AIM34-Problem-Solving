def ror(bits, n):
    print(f"Original: {bits}")
    for i in range(1, n + 1):
        bits = bits[-1] + bits[:-1]          # LSB moves to MSB
        print(f"  Step {i}: {bits}")
    return bits

def rcr(bits, n, carry):
    print(f"Original: {bits}   Initial CF = {carry}")
    for i in range(1, n + 1):
        new_carry = bits[-1]                  # LSB goes into CF
        bits = carry + bits[:-1]              # old CF enters at MSB
        carry = new_carry
        print(f"  Step {i}: {bits}   CF = {carry}")
    return bits, carry

num = "11010101"
n = 3

print("=== a) ROR by 3 ===")
r = ror(num, n)
print(f"Final result: {r}")
print("Verification:", "PASS" if r == num[-n:] + num[:-n] else "FAIL")

for cf in ("0", "1"):
    print(f"\n=== b) RCR by 3 (initial CF = {cf}) ===")
    r, c = rcr(num, n, cf)
    print(f"Final result: {r}   Final CF = {c}")
    # Independent check: treat CF + byte as one 9-bit number and rotate it
    s = cf + num
    s = s[-n:] + s[:-n]
    print("Verification:", "PASS" if (s[1:], s[0]) == (r, c) else "FAIL")