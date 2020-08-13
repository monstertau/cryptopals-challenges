from collections import Counter

occurance_english = {
    'a': 8.2389258,    'b': 1.5051398,    'c': 2.8065007,    'd': 4.2904556,
    'e': 12.813865,    'f': 2.2476217,    'g': 2.0327458,    'h': 6.1476691,
    'i': 6.1476691,    'j': 0.1543474,    'k': 0.7787989,    'l': 4.0604477,
    'm': 2.4271893,    'n': 6.8084376,    'o': 7.5731132,    'p': 1.9459884,
    'q': 0.0958366,    'r': 6.0397268,    's': 6.3827211,    't': 9.1357551,
    'u': 2.7822893,    'v': 0.9866131,    'w': 2.3807842,    'x': 0.1513210,
    'y': 1.9913847,    'z': 0.0746517
}


def fitting_quotient(byte_array):
    val_english = list(occurance_english.values())
    counter = Counter(byte_array)
    val_text = [(counter.get(ord(ch), 0) * 100) / len(byte_array)
                for ch in occurance_english.keys()]
    return sum([abs(a-b) for a, b in zip(val_english, val_text)]) / len(val_text)


def single_byte_xor(byte_array, k):
    tmp = []
    for ch in byte_array:
        tmp.append(k ^ ch)
    return bytearray(tmp)


def decode(message):
    b = bytearray.fromhex(message)
    original_text, encryption_key, min_fq, fq = None, None, None, None
    try:
        for i in range(256):
            text = single_byte_xor(b, i)
            fq = fitting_quotient(text)
            if min_fq is None or fq < min_fq:
                encryption_key, original_text, min_fq = i, text, fq
        return original_text, encryption_key
    except Exception as e:
        return None


def main():
    message = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    print("Message: %s" % message)
    ans = decode(message)
    if ans is not None:

        print("Decrypted Text: %s" % ans[0].decode('ascii'))
        print("Cipher Key: %s" % ans[1])
    else:
        print("Your Algorithm is not working or the message just non-sense")


if __name__ == "__main__":
    main()
