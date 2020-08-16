

def fixed_xor(first, second):
    L = []
    b1 = bytearray.fromhex(first)
    b2 = bytearray.fromhex(second)
    print("-->Encoded Word: %s\n" % b1.decode('ascii'))
    print("-->Key: %s\n" % b2.decode('ascii'))
    if len(b1) != len(b2):
        return None
    for i in range(len(b1)):
        L.append(b1[i] ^ b2[i])
    print("-->Secret Word: %s\n" % bytearray(L).decode('ascii'))
    return bytes(L).hex()


def main():
    first_buf = "1c0111001f010100061a024b53535009181c"
    second_buf = "686974207468652062756c6c277320657965"
    print("First Buffer :\t%s\n\nSecond Buffer :\t%s\n" %
          (first_buf, second_buf))
    res = fixed_xor(first_buf, second_buf)
    if res is not None:
        print("Xor Buffer: %s" % res)
    else:
        print("Wrong Answer.")


if __name__ == "__main__":
    main()
