

key = 'ICE'


def encrypt(message):
    b = message.encode('ascii')
    i = 0
    L = []
    for char in b:
        n = char ^ key[i].encode('ascii')[0]
        i = (i+1) % 3
        L.append(n)
    return bytes(L).hex()


def main():
    message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    print("Message to be encrypted: %s\n"% message)
    encrypted_text = encrypt(message)
    print("Encrypted Text: %s\n"% encrypted_text)


if __name__ == "__main__":
    main()
