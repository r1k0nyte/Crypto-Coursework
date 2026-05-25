import os
import time
import statistics

from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Cipher import ChaCha20

from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


sizes_mb = [1, 5, 10, 25]


# AES

print("\n - AES - \n")

for size in sizes_mb:

    times = []

    for _ in range(5):

        data = os.urandom(size * 1024 * 1024)

        key = get_random_bytes(32)

        cipher = AES.new(
            key,
            AES.MODE_GCM
        )

        start = time.perf_counter()

        ciphertext, tag = (
            cipher.encrypt_and_digest(data)
        )

        end = time.perf_counter()

        times.append(end - start)

    avg_time = statistics.mean(times)

    speed = size / avg_time

    print(f"File size: {size} MB")
    print(f"Average encryption time: {avg_time:.6f} s")
    print(f"Encryption speed: {speed:.2f} MB/s")
    print()


# DES

print("\n - DES - \n")

for size in sizes_mb:

    times = []

    for _ in range(5):

        data = os.urandom(size * 1024 * 1024)

        padded_data = pad(data, 8)

        key = get_random_bytes(8)

        cipher = DES.new(
            key,
            DES.MODE_CBC
        )

        start = time.perf_counter()

        ciphertext = cipher.encrypt(
            padded_data
        )

        end = time.perf_counter()

        times.append(end - start)

    avg_time = statistics.mean(times)

    speed = size / avg_time

    print(f"File size: {size} MB")
    print(f"Average encryption time: {avg_time:.6f} s")
    print(f"Encryption speed: {speed:.2f} MB/s")
    print()


# CHACHA20

print("\n - ChaCha20 - \n")

for size in sizes_mb:

    times = []

    for _ in range(5):

        data = os.urandom(size * 1024 * 1024)

        key = get_random_bytes(32)

        nonce = get_random_bytes(12)

        cipher = ChaCha20.new(
            key=key,
            nonce=nonce
        )

        start = time.perf_counter()

        ciphertext = cipher.encrypt(data)

        end = time.perf_counter()

        times.append(end - start)

    avg_time = statistics.mean(times)

    speed = size / avg_time

    print(f"File size: {size} MB")
    print(f"Average encryption time: {avg_time:.6f} s")
    print(f"Encryption speed: {speed:.2f} MB/s")
    print()