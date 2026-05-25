import os
import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Генерація тестових даних
data = os.urandom(10 * 1024 * 1024)

# Генерація ключа AES-256
key = get_random_bytes(32)

# Створення AES у режимі GCM
cipher = AES.new(key, AES.MODE_GCM)

start_time = time.time()

ciphertext, tag = cipher.encrypt_and_digest(data)

end_time = time.time()

encryption_time = end_time - start_time

print("AES encryption completed")
print(f"Encrypted size: {len(ciphertext)} bytes")
print(f"Encryption time: {encryption_time:.6f} seconds")