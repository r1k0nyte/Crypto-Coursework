from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def bit_difference(data1, data2):

    diff = 0

    for b1, b2 in zip(data1, data2):

        xor = b1 ^ b2

        diff += bin(xor).count("1")

    return diff


original = b"Hello world 1234"
modified = b"Jello world 1234"

key = get_random_bytes(32)

cipher1 = AES.new(key, AES.MODE_GCM)
ciphertext1, tag1 = cipher1.encrypt_and_digest(original)

cipher2 = AES.new(key, AES.MODE_GCM, nonce=cipher1.nonce)
ciphertext2, tag2 = cipher2.encrypt_and_digest(modified)

difference = bit_difference(ciphertext1, ciphertext2)

total_bits = len(ciphertext1) * 8

avalanche = (difference / total_bits) * 100

print(f"Avalanche effect: {avalanche:.2f}%")