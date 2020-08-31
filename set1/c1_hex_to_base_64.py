

base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def encode(hex_str, base64_str):
    L = []
    b = bytearray.fromhex(hex_str)
    # print("Secret Word: %s\n" % b.decode('ascii'))
    pad_count = len(b) % 3
    for i in range(0, len(b), 3):
        # shift the first of 3 digits to first 8 bits of 24 bits number
        n = b[i] << 16
        if i+1 < len(b):
            n += b[i+1] << 8
        if i+2 < len(b):
            n += b[i+2]
        n1 = (n >> 18) & 63
        n2 = (n >> 12) & 63
        n3 = (n >> 6) & 63
        n4 = n & 63
        L.append(base64_chars[n1])
        L.append(base64_chars[n2])
        if i+1 < len(b):
            L.append(base64_chars[n3])
        if i+2 < len(b):
            L.append(base64_chars[n4])
    if pad_count > 0:
        while pad_count < 3:
            L.append("=")
            pad_count += 1
    encoded = "".join(L)
    print(encoded)
    if encoded == base64_str:
        return True
    return False


def main():
    hex_str = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
    base64_str = 'MG5seSBuMDBiIGM0bid0IDNuYzBkMyB0aDFzIHN0cjFuOS4='
    print("hex string:\t%s\n\nbase64 string:\t%s\n" % (hex_str, base64_str))
    if encode(hex_str, base64_str):
        print("Successfully encoded hex string!")
    else:
        print("You failed.")


if __name__ == "__main__":
    main()
