import os
import math

from collections import Counter

from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Cipher import ChaCha20

from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


# ENTROPY FUNCTION

def calculate_entropy(data):

    counter = Counter(data)

    total = len(data)

    entropy = 0

    for count in counter.values():

        probability = count / total

        entropy -= (
            probability *
            math.log2(probability)
        )

    return entropy


# TEST DATA

data = os.urandom(5 * 1024 * 1024)


# AES

aes_key = get_random_bytes(32)

aes_cipher = AES.new(
    aes_key,
    AES.MODE_GCM
)

aes_ciphertext, aes_tag = (
    aes_cipher.encrypt_and_digest(data)
)

aes_entropy = calculate_entropy(
    aes_ciphertext
)

print(
    f"AES entropy: "
    f"{aes_entropy:.6f}"
)


# DES

des_key = get_random_bytes(8)

des_cipher = DES.new(
    des_key,
    DES.MODE_CBC
)

padded_data = pad(data, 8)

des_ciphertext = des_cipher.encrypt(
    padded_data
)

des_entropy = calculate_entropy(
    des_ciphertext
)

print(
    f"DES entropy: "
    f"{des_entropy:.6f}"
)


# CHACHA20

chacha_key = get_random_bytes(32)

nonce = get_random_bytes(12)

chacha_cipher = ChaCha20.new(
    key=chacha_key,
    nonce=nonce
)

chacha_ciphertext = chacha_cipher.encrypt(
    data
)

chacha_entropy = calculate_entropy(
    chacha_ciphertext
)

print(
    f"ChaCha20 entropy: "
    f"{chacha_entropy:.6f}"
)