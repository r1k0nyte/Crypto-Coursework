from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Cipher import ChaCha20

from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


# BIT DIFFERENCE FUNCTION

def bit_difference(data1, data2):

    diff = 0

    for b1, b2 in zip(data1, data2):

        xor = b1 ^ b2

        diff += bin(xor).count("1")

    return diff


# TEST DATA

original = b"Hello world 1234"
modified = b"Jello world 1234"


# AES

aes_key = get_random_bytes(32)

aes_cipher1 = AES.new(
    aes_key,
    AES.MODE_GCM
)

aes_ciphertext1, aes_tag1 = (
    aes_cipher1.encrypt_and_digest(original)
)

aes_cipher2 = AES.new(
    aes_key,
    AES.MODE_GCM,
    nonce=aes_cipher1.nonce
)

aes_ciphertext2, aes_tag2 = (
    aes_cipher2.encrypt_and_digest(modified)
)

aes_difference = bit_difference(
    aes_ciphertext1,
    aes_ciphertext2
)

aes_total_bits = len(aes_ciphertext1) * 8

aes_avalanche = (
    aes_difference /
    aes_total_bits
) * 100

print(
    f"AES Avalanche effect: "
    f"{aes_avalanche:.2f}%"
)


# DES

des_key = get_random_bytes(8)

des_cipher1 = DES.new(
    des_key,
    DES.MODE_CBC
)

padded_original = pad(original, 8)
padded_modified = pad(modified, 8)

des_ciphertext1 = des_cipher1.encrypt(
    padded_original
)

des_cipher2 = DES.new(
    des_key,
    DES.MODE_CBC,
    iv=des_cipher1.iv
)

des_ciphertext2 = des_cipher2.encrypt(
    padded_modified
)

des_difference = bit_difference(
    des_ciphertext1,
    des_ciphertext2
)

des_total_bits = len(des_ciphertext1) * 8

des_avalanche = (
    des_difference /
    des_total_bits
) * 100

print(
    f"DES Avalanche effect: "
    f"{des_avalanche:.2f}%"
)


# CHACHA20

chacha_key = get_random_bytes(32)

nonce = get_random_bytes(12)

chacha_cipher1 = ChaCha20.new(
    key=chacha_key,
    nonce=nonce
)

chacha_ciphertext1 = (
    chacha_cipher1.encrypt(original)
)

chacha_cipher2 = ChaCha20.new(
    key=chacha_key,
    nonce=nonce
)

chacha_ciphertext2 = (
    chacha_cipher2.encrypt(modified)
)

chacha_difference = bit_difference(
    chacha_ciphertext1,
    chacha_ciphertext2
)

chacha_total_bits = (
    len(chacha_ciphertext1) * 8
)

chacha_avalanche = (
    chacha_difference /
    chacha_total_bits
) * 100

print(
    f"ChaCha20 Avalanche effect: "
    f"{chacha_avalanche:.2f}%"
)