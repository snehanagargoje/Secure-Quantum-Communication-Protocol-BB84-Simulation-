import random

# Generate random bits
def generate_bits(n):
    return [random.randint(0,1) for _ in range(n)]

# Generate random bases
def generate_bases(n):
    return [random.choice(['+', 'x']) for _ in range(n)]

# Encode bits with bases
def encode(bits, bases):
    encoded = []
    for bit, base in zip(bits, bases):
        encoded.append((bit, base))
    return encoded

# Measure bits
def measure(encoded, bases):
    measured = []
    for (bit, base), measure_base in zip(encoded, bases):
        if base == measure_base:
            measured.append(bit)
        else:
            measured.append(random.randint(0,1))
    return measured

n = 10

alice_bits = generate_bits(n)
alice_bases = generate_bases(n)

encoded = encode(alice_bits, alice_bases)

bob_bases = generate_bases(n)
bob_results = measure(encoded, bob_bases)

shared_key = []

for i in range(n):
    if alice_bases[i] == bob_bases[i]:
        shared_key.append(alice_bits[i])

print("Alice Bits:", alice_bits)
print("Bob Results:", bob_results)
print("Shared Key:", shared_key)