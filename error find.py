import random
import matplotlib.pyplot as plt

# Number of qubits
n = 100

# Generate random bits
def generate_bits(n):
    return [random.randint(0,1) for _ in range(n)]

# Generate random bases
def generate_bases(n):
    return [random.choice(['+', 'x']) for _ in range(n)]

# Encode bits
def encode(bits, bases):
    encoded = []
    for bit, base in zip(bits, bases):
        encoded.append((bit, base))
    return encoded

# Measurement function
def measure(encoded, bases):
    results = []
    for (bit, base), measure_base in zip(encoded, bases):
        if base == measure_base:
            results.append(bit)
        else:
            results.append(random.randint(0,1))
    return results

# Alice prepares bits
alice_bits = generate_bits(n)
alice_bases = generate_bases(n)

# Encode photons
encoded_photons = encode(alice_bits, alice_bases)

# Eve (Eavesdropper) intercepts
eve_bases = generate_bases(n)
eve_results = measure(encoded_photons, eve_bases)

# Eve resends photons
eve_encoded = encode(eve_results, eve_bases)

# Bob measures
bob_bases = generate_bases(n)
bob_results = measure(eve_encoded, bob_bases)

# Shared key extraction
shared_key_alice = []
shared_key_bob = []

for i in range(n):
    if alice_bases[i] == bob_bases[i]:
        shared_key_alice.append(alice_bits[i])
        shared_key_bob.append(bob_results[i])

# QBER calculation
errors = 0
for a,b in zip(shared_key_alice, shared_key_bob):
    if a != b:
        errors += 1

qber = errors / len(shared_key_alice) if len(shared_key_alice) > 0 else 0

print("Total bits:", n)
print("Shared Key Length:", len(shared_key_alice))
print("Errors:", errors)
print("Quantum Bit Error Rate (QBER):", qber)

# Graph for QBER
labels = ["Correct Bits","Error Bits"]
values = [len(shared_key_alice)-errors, errors]

plt.bar(labels, values)
plt.title("Quantum Key Distribution Error Analysis")
plt.ylabel("Number of Bits")
plt.show()