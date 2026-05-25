from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Cipher import ChaCha20

from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


# =========================================
# BIT DIFFERENCE FUNCTION
# =========================================

def bit_difference(data1, data2):

    diff = 0

    for b1, b2 in zip(data1, data2):

        xor = b1 ^ b2

        diff += bin(xor).count("1")

    return diff


# =========================================
# TEST DATA
# =========================================

data = b"Hello world 1234"


# =========================================
# AES
# =========================================

print("\n================ AES ================\n")

aes_key1 = bytearray(get_random_bytes(32))
aes_key2 = bytearray(aes_key1)

aes_key2[0] ^= 0b00000001

aes_cipher1 = AES.new(
    bytes(aes_key1),
    AES.MODE_ECB
)

aes_cipher2 = AES.new(
    bytes(aes_key2),
    AES.MODE_ECB
)

aes_ciphertext1 = aes_cipher1.encrypt(data)
aes_ciphertext2 = aes_cipher2.encrypt(data)

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


# =========================================
# DES
# =========================================

print("\n================ DES ================\n")

des_key1 = bytearray(get_random_bytes(8))
des_key2 = bytearray(des_key1)

des_key2[0] ^= 0b00000010

des_cipher1 = DES.new(
    bytes(des_key1),
    DES.MODE_ECB
)

des_cipher2 = DES.new(
    bytes(des_key2),
    DES.MODE_ECB
)

padded_data = pad(data, 8)

des_ciphertext1 = des_cipher1.encrypt(
    padded_data
)

des_ciphertext2 = des_cipher2.encrypt(
    padded_data
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


# =========================================
# CHACHA20
# =========================================

print("\n============= ChaCha20 =============\n")

chacha_key1 = bytearray(
    get_random_bytes(32)
)

chacha_key2 = bytearray(
    chacha_key1
)

chacha_key2[0] ^= 0b00000001

nonce = get_random_bytes(12)

chacha_cipher1 = ChaCha20.new(
    key=bytes(chacha_key1),
    nonce=nonce
)

chacha_cipher2 = ChaCha20.new(
    key=bytes(chacha_key2),
    nonce=nonce
)

chacha_ciphertext1 = (
    chacha_cipher1.encrypt(data)
)

chacha_ciphertext2 = (
    chacha_cipher2.encrypt(data)
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