def brute_force_time(bits, rate):

    seconds = (2 ** bits) / rate

    years = seconds / (60 * 60 * 24 * 365)

    return years

rate = 10**12

aes_years = brute_force_time(256, rate)

des_years = brute_force_time(56, rate)

chacha20_years = brute_force_time(32, rate)

print("AES:", aes_years)
print("DES:", des_years)
print("ChaCha20:", chacha20_years)