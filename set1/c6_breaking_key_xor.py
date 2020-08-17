import base64
from collections import defaultdict
import c3_single_xor_cipher as single_xor
KEY_SIZE = [i for i in range(2, 41)]


def decrypt_base64(text):
    return base64.b64decode(text)


def hamming_distance_bits(str1, str2):
    distance = 0
    for char1, char2 in zip(str1, str2):
        diff = char1 ^ char2
        for i in range(8):
            distance += (diff >> i) & 1
    return distance

def get_lowest_nHD(text):
    dict_HD = {}
    min_HD, candidate_keysize = None, None
    for key_length in KEY_SIZE:
        start = 0
        end = start + key_length
        distance_list = []
        while True:
            first_chunk = text[start:end]
            sec_chunk = text[start+key_length:end+key_length]
            if len(sec_chunk) < key_length:
                break

            distance = hamming_distance_bits(
                first_chunk, sec_chunk) / key_length
            distance_list.append(distance)
            start = end + key_length
            end = start + key_length
        normalize_HD = (sum(distance_list) / len(distance_list))

        dict_HD[key_length] = normalize_HD
        if min_HD is None or min_HD > normalize_HD:
            min_HD, candidate_keysize = normalize_HD, key_length
    return candidate_keysize, min_HD


def transpose_block(text, key_size):
    same_block = []
    for i in range(key_size):
        d = {}
        for j in range(i, len(text), key_size):
            d[j] = text[j]
        same_block.append(d)
    return same_block


def main():
    the_file = open('6_breaking_key_xor.txt', 'r')
    data = the_file.read()

    b64_decoded = base64.b64decode(data)
    key_size, score = get_lowest_nHD(b64_decoded)

    original_text_list = [None] * len(b64_decoded)
    same_block = transpose_block(b64_decoded, key_size)
    map_text = {}
    xor_key_list = []
    for block in same_block:
        key_list = []
        value_list = []
        for k, v in block.items():
            key_list.append(k)
            value_list.append(v)
        decoded, key = single_xor.decode(value_list)
        xor_key_list.append(chr(key))
        for i, k in enumerate(key_list):
            map_text[k] = decoded[i]
    for k, v in map_text.items():
        original_text_list[k] = chr(v)

    original_text = "".join(original_text_list)
    original_key = "".join(xor_key_list)
    print("Original Text: %s\n" % original_text)
    print("Original Key: %s" % original_key)



if __name__ == "__main__":
    main()
