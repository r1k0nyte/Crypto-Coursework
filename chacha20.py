import os
import time
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

# Генерація тестових даних
data = os.urandom(10 * 1024 * 1024)

# Генерація ключа
key = get_random_bytes(32)

# Генерація nonce
nonce = get_random_bytes(12)

cipher = ChaCha20.new(key=key, nonce=nonce)

start_time = time.time()

ciphertext = cipher.encrypt(data)

end_time = time.time()

encryption_time = end_time - start_time

print("ChaCha20 encryption completed")
print(f"Encrypted size: {len(ciphertext)} bytes")
print(f"Encryption time: {encryption_time:.6f} seconds")