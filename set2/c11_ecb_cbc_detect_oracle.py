import random
from Crypto.Cipher import AES
from c9_implement_pkcs import padding


def generate_key():
    b = []
    for _ in range(16):
        rand_char = chr(random.randint(64, 126))
        b.append(rand_char.encode())
    return b''.join(b)


def choosing_AES_mode(key):
    mode = random.randint(0, 1)
    if mode == 0:
        return AES.new(key, AES.MODE_ECB), mode
    else:
        return AES.new(key, AES.MODE_CBC), mode


def append_bytes(plaintext):
    before = random.randint(5, 10)
    after = random.randint(5, 10)
    b = b''
    a = b''
    for _ in range(before):
        b += chr(random.randint(0, 127)).encode()
    for _ in range(after):
        a += chr(random.randint(0, 127)).encode()
    return b + plaintext + a


def encryption_oracle(plaintext):
    key = generate_key()
    cipher, mode = choosing_AES_mode(key)
    text = append_bytes(plaintext)
    return cipher.encrypt(padding(text, AES.block_size)), mode


def aes_detection(plaintext):
    ciphertext, mode = encryption_oracle(plaintext)
    if ciphertext[16:32] == ciphertext[32:48]:
        if mode != 0:
            print('Mode CBC Detected, prediction is wrong')
    elif mode != 1:
        print('Mode ECB Detected, prediction is wrong')


if __name__ == "__main__":
    plaintext = b'A' * (16 * 3)
    trials = 100
    for i in range(trials):
        aes_detection(plaintext)
