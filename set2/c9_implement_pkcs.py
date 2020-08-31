from Crypto.Util.number import bytes_to_long


def padding(text, block_size):
    pad_num = block_size - len(text) % block_size
    pad_str = pad_num * chr(pad_num)
    padded_text = text + pad_str.encode()
    return padded_text


def main():
    plaintext = b"YELLOW SUBMARINE"
    padded_text = padding(plaintext, 20)
    print(padded_text)

if __name__ == "__main__":
    main()
