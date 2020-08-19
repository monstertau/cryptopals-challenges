import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode


def decrypt_AES(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    text = cipher.decrypt(message)
    return text.decode('ascii')


def main():
    file = open('c7_aes_in_ecb_mode.txt', 'r')
    data = b64decode(file.read())
    key = b'YELLOW SUBMARINE'
    b64_message = decrypt_AES(data, key)
    print(b64_message)


if __name__ == "__main__":
    main()
