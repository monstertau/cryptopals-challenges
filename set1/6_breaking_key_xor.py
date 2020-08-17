import base64
KEY_SIZE = [i for i in range(2, 41)]


def finding_keysize(text):
    for key_length in range(3,4):
        start = 0
        end = start + key_length
        sum_dis = 0
        while True:
            first_chunk = text[start:end]
            sec_chunk = text[start+key_length:end+key_length]
            distance = hamming_distance_bits(first_chunk,sec_chunk)
            print("%s %s %s"%(first_chunk[2],sec_chunk[2],distance))
            break
def decrypt_base64(text):
    return base64.b64decode(text)


def hamming_distance_bits(str1, str2):
    distance = 0
    for char1, char2 in zip(str1, str2):
        diff = char1 ^ char2
        for i in range(8):
            distance += (diff >> i) & 1
    return distance


def main():
    b64_decoded = []
    with open("6_breaking_key_xor.txt") as file:
        for line in file:

            b64_decoded.append(decrypt_base64(line))
        file.close()
    finding_keysize(b64_decoded[0])
    # for text in b64_decoded:
    #     finding_keysize(text)
    # hamming_distance_bits('this is a test', 'wokka wokka!!!')


if __name__ == "__main__":
    main()
