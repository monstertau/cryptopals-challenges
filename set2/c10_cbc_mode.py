from Crypto.Cipher import AES
from base64 import b64decode
from c9_implement_pkcs import padding
from Crypto.Util.strxor import strxor
KEY = b"YELLOW SUBMARINE"
IV = b'\x00' * 16


def decrypt_ECB(text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(text)


def encrypt_ECB(text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(text)


def split_to_blocks(text):
    padded_text = padding(text, AES.block_size)
    return [padded_text[b:b+AES.block_size] for b in range(0, len(padded_text), AES.block_size)]


def encrypt_CBC(text, key, iv):
    # cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    # encrypted_text = cipher.encrypt(padding(text, 16))
    # return encrypted_text
    blocks = split_to_blocks(text)
    prev_block = iv
    res = []
    for block in blocks:
        encrypted_block = strxor(block, prev_block)
        cipher_text = encrypt_ECB(encrypted_block, key)
        res.append(cipher_text)
        prev_block = block
    return b''.join(res)


def decrypt_CBC(text, key, iv):
    # cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    # decrypted_text = cipher.decrypt(padding(text, AES.block_size))
    # return decrypted_text
    blocks = split_to_blocks(text)
    prev_block = iv
    res = []
    for block in blocks:
        decrypted_block = decrypt_ECB(block, key)
        plain_text = strxor(decrypted_block, prev_block)
        res.append(plain_text)
        prev_block = block
    return b''.join(res)


if __name__ == "__main__":
    file = open('c10_cbc_mode.txt', 'r')
    data = b64decode(file.read())
    decrypted_data = decrypt_CBC(data, KEY, IV)
    print(decrypted_data)
