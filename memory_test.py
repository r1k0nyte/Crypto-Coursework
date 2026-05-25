import tracemalloc
import os

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = os.urandom(50 * 1024 * 1024)

key = get_random_bytes(32)

cipher = AES.new(key, AES.MODE_GCM)

tracemalloc.start()

cipher.encrypt_and_digest(data)

current, peak = tracemalloc.get_traced_memory()

print(f"Peak memory: {peak / 1024 / 1024:.2f} MB")

tracemalloc.stop()