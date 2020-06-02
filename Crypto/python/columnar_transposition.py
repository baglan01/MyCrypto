from random import randint

LETTERS = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z'
]

def clean_text(text):
    def valid_symbol(x):
        return x.isalpha()

    return ''.join(list(filter(valid_symbol, list(text))))

def random_letter():
    n = len(LETTERS)
    return LETTERS[randint(0, n - 1)]

def get_key_order(key):
    lst = list(key.upper())

    k = 0
    for i in range(len(LETTERS)):
        x = LETTERS[i]
        for j in range(len(lst)):
            if lst[j] == x:
                lst[j] = k
                k += 1

    return lst

def encrypt(plaintext, key):
    plaintext = clean_text(plaintext)

    n = len(plaintext)
    k = len(key)

    if n % k != 0:
        t = k - n % k
        for _ in range(t):
            plaintext += random_letter()
        n += t

    rows = n // k
    matrix = [[] for _ in range(k)]
    for i in range(rows):
        for j in range(k):
            matrix[j].append(plaintext[k * i + j])

    order = get_key_order(key)
    key_dict = { order[i]: matrix[i] for i in range(k) }

    lst = []
    for x in sorted(key_dict.keys()):
        lst.extend(key_dict[x] + [' '])

    return ''.join(lst)

def decrypt(ciphertext, key):
    k = len(key)
    lst = ciphertext.split(None)

    if len(lst) != k:
        raise ValueError('WHAT DA HECK: WRONG KEY')

    order = get_key_order(key)

    matrix = [[] for _ in range(k)]

    for i in range(k):
        matrix[i] = list(lst[order[i]])

    rows = len(matrix[0]) if len(matrix) > 0 else 0

    res_lst = []
    for i in range(rows):
        for j in range(k):
            res_lst.append(matrix[j][i])

    return ''.join(res_lst)


if __name__ == '__main__':
    print('=== Columnar cipher ===')
    
    ENCRYPT_MODE = 0
    DECRYPT_MODE = 1

    print('Encrypt/Decrypt (0/1)?')
    mode = int(input())

    if mode == ENCRYPT_MODE:
        print('Plaintext:')
        plaintext = input()
        print('Key:')
        key = input()
        ciphertext = encrypt(plaintext, key)
        print('Ciphertext:')
        print(ciphertext)
    else:
        print('Ciphertext:')
        ciphertext = input()
        print('Key:')
        key = input()
        plaintext = decrypt(ciphertext, key)
        print('Plaintext:')
        print(plaintext)

    print('=== Finished ===')
