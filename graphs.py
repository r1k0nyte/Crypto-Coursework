import os
import time
import math
import tracemalloc

import matplotlib.pyplot as plt

from collections import Counter

from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Cipher import ChaCha20

from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


# ENTROPY

def calculate_entropy(data):

    counter = Counter(data)

    total = len(data)

    entropy = 0

    for count in counter.values():

        probability = count / total

        entropy -= probability * math.log2(probability)

    return entropy


# AVALANCHE EFFECT

def bit_difference(data1, data2):

    diff = 0

    for b1, b2 in zip(data1, data2):

        xor = b1 ^ b2

        diff += bin(xor).count("1")

    return diff


# TEST SIZES

sizes = [1, 5, 10, 25, 50]

aes_encrypt_times = []
des_encrypt_times = []
chacha_encrypt_times = []

aes_memory = []
des_memory = []
chacha_memory = []

aes_entropy = []
des_entropy = []
chacha_entropy = []


# MAIN TEST LOOP

for size in sizes:

    print(f"\nTesting {size} MB")

    data = os.urandom(size * 1024 * 1024)

    # AES

    aes_key = get_random_bytes(32)

    aes_cipher = AES.new(aes_key, AES.MODE_GCM)

    tracemalloc.start()

    start = time.perf_counter()

    aes_ciphertext, aes_tag = aes_cipher.encrypt_and_digest(data)

    end = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    aes_encrypt_times.append(end - start)

    aes_memory.append(peak / 1024 / 1024)

    aes_entropy.append(
        calculate_entropy(aes_ciphertext)
    )

    # DES

    des_key = get_random_bytes(8)

    des_cipher = DES.new(des_key, DES.MODE_CBC)

    padded_data = pad(data, 8)

    tracemalloc.start()

    start = time.perf_counter()

    des_ciphertext = des_cipher.encrypt(padded_data)

    end = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    des_encrypt_times.append(end - start)

    des_memory.append(peak / 1024 / 1024)

    des_entropy.append(
        calculate_entropy(des_ciphertext)
    )

    # CHACHA20

    chacha_key = get_random_bytes(32)

    nonce = get_random_bytes(12)

    chacha_cipher = ChaCha20.new(
        key=chacha_key,
        nonce=nonce
    )

    tracemalloc.start()

    start = time.perf_counter()

    chacha_ciphertext = chacha_cipher.encrypt(data)

    end = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    chacha_encrypt_times.append(end - start)

    chacha_memory.append(peak / 1024 / 1024)

    chacha_entropy.append(
        calculate_entropy(chacha_ciphertext)
    )


# ENCRYPTION TIME GRAPH

plt.figure(figsize=(10, 6))

plt.plot(
    sizes,
    aes_encrypt_times,
    marker='o',
    label="AES"
)

plt.plot(
    sizes,
    des_encrypt_times,
    marker='o',
    label="DES"
)

plt.plot(
    sizes,
    chacha_encrypt_times,
    marker='o',
    label="ChaCha20"
)

plt.xlabel("File Size (MB)")
plt.ylabel("Encryption Time (s)")
plt.title("Encryption Time Comparison")

plt.grid(True)

plt.legend()

plt.show()


# MEMORY GRAPH

plt.figure(figsize=(10, 6))

plt.plot(
    sizes,
    aes_memory,
    marker='o',
    label="AES"
)

plt.plot(
    sizes,
    des_memory,
    marker='o',
    label="DES"
)

plt.plot(
    sizes,
    chacha_memory,
    marker='o',
    label="ChaCha20"
)

plt.xlabel("File Size (MB)")
plt.ylabel("Memory Usage (MB)")
plt.title("Memory Usage Comparison")

plt.grid(True)

plt.legend()

plt.show()


# ENTROPY GRAPH

plt.figure(figsize=(10, 6))

plt.plot(
    sizes,
    aes_entropy,
    marker='o',
    label="AES"
)

plt.plot(
    sizes,
    des_entropy,
    marker='o',
    label="DES"
)

plt.plot(
    sizes,
    chacha_entropy,
    marker='o',
    label="ChaCha20"
)

plt.xlabel("File Size (MB)")
plt.ylabel("Entropy")

plt.title("Ciphertext Entropy")

plt.grid(True)

plt.legend()

plt.show()