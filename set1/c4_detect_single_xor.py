import c3_single_xor_cipher as single_xor_cipher

def check_decrypted_str(file):
    min_fq, original_text, encrypted_str = None, None, None
    for line in file:
        b = bytearray.fromhex(line)
        ans = single_xor_cipher.decode(b)
        if ans is not None:
            fq = single_xor_cipher.fitting_quotient(ans[0])
            if min_fq is None or fq < min_fq:
                min_fq, original_text, encrypted_str, key = fq, ans[0], line, ans[1]
    return original_text, encrypted_str, key


def main():
    try:
        f = open('4_detect_single_xor.txt', 'r')
        original_text, encrypted_str, key = check_decrypted_str(f)
        print("Founded Encrypted Hex String: %s" % encrypted_str)
        print("Decrypted Hex String with key %s : %s " %
              (key, original_text.decode('ascii')))
        f.close()
    except (FileNotFoundError, IOError):
        print('Wrong file or path!')


if __name__ == "__main__":
    main()
