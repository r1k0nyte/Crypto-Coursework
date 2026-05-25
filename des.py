import os
import time
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# Генерація тестових даних
data = os.urandom(10 * 1024 * 1024)

# Генерація 56-бітного ключа
key = get_random_bytes(8)

# Вирівнювання даних
padded_data = pad(data, 8)

cipher = DES.new(key, DES.MODE_CBC)

start_time = time.time()

ciphertext = cipher.encrypt(padded_data)

end_time = time.time()

encryption_time = end_time - start_time

print("DES encryption completed")
print(f"Encrypted size: {len(ciphertext)} bytes")
print(f"Encryption time: {encryption_time:.6f} seconds")