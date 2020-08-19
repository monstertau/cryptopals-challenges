BLOCK_SIZE = 16


def block_chunks(data):
    maxnum_repetition, aes_text = None, None
    for ciphertext in data:
        blocks = []
        for i in range(0, len(ciphertext), BLOCK_SIZE):
            block = ciphertext[i:i+BLOCK_SIZE]
            blocks.append(block)
        num_repetition = len(blocks) - len(set(blocks))
        if maxnum_repetition is None or maxnum_repetition < num_repetition:
            maxnum_repetition, aes_text = num_repetition, ciphertext
    return aes_text, maxnum_repetition


def main():
    with open('c8_detect_aes_in_ecb.txt', 'r') as file:
        data = [bytes.fromhex(line) for line in file]
    text, repetition = block_chunks(data)
    print("Cipher Text Encrypted With AES: %s" % text)
    print("Repetition: ", repetition)


if __name__ == "__main__":
    main()
