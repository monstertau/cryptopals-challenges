
KEY_SIZE = [i for i in range(2, 41)]


def hamming_distance_bits(str1, str2):
    b1 = str1.encode('ascii')
    b2 = str2.encode('ascii')
    distance = 0
    for char1, char2 in zip(b1, b2):
        diff = char1 ^ char2
        for i in range(8):
            distance += (diff >> i) & 1
    return distance


def main():

    hamming_distance_bits('this is a test', 'wokka wokka!!!')
    print(KEY_SIZE)

if __name__ == "__main__":
    main()
