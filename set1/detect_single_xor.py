from single_xor_cipher import fitting_quotient, decode


def check_decrypted_str(file):
    min_fq, original_text, encrypted_str = None, None, None
    for line in file:
        ans = decode(line)
        if ans is not None:
            fq = fitting_quotient(ans[0])
            if min_fq is None or fq < min_fq:
                min_fq, original_text, encrypted_str, key = fq, ans[0], line, ans[1]
    return original_text, encrypted_str, key


def main():
    try:
        f = open('detect_single_xor.txt', 'r')
        original_text, encrypted_str, key = check_decrypted_str(f)
        print("Founded Encrypted Hex String: %s" % encrypted_str)
        print("Decrypted Hex String with key %s : %s " %
              (key, original_text.decode('ascii')))
        f.close()
    except (FileNotFoundError, IOError):
        print('Wrong file or path!')


if __name__ == "__main__":
    main()
