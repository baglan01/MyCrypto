class VigenereCipher:
    LETTERS = [
	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
	'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    VIGENERE_ENCRYPT_TABLE = None
    VIGENERE_DECRYPT_TABLE = None

    def __init__(self):
        def add_letters(x, y):
            ord_a = ord('A')
            p, q = ord(x) - ord_a, ord(y) - ord_a
            return chr((p + q) % 26 + ord_a)
            
        def generate_encrypt_table():
            table  = dict()
            for x in VigenereCipher.LETTERS:
                table[x] = dict()
                for y in VigenereCipher.LETTERS:
                    table[x][y] = add_letters(x, y)
            return table
            
        def generate_decrypt_table(encrypt_table):
            table = dict()
            for x in encrypt_table.keys():
                table[x] = { encrypt_table[x][y]: y for y in encrypt_table[x].keys() }
            return table

        if not VigenereCipher.VIGENERE_ENCRYPT_TABLE:
            encrypt_table = generate_encrypt_table()
            decrypt_table = generate_decrypt_table(encrypt_table)
            VigenereCipher.VIGENERE_ENCRYPT_TABLE = encrypt_table
            VigenereCipher.VIGENERE_DECRYPT_TABLE = decrypt_table


    def print_vigenere_table(self, table):
        for x in table.keys():
            for y in table[x]:
                print(table[x][y], end=' ')
        print()

    def process_text_with_key(self, text, key, action):
        '''Perform action on each character of text with key and return string'''
        lst = list(text)
        res_lst = []
        i = 0
        for x in lst:
            res_lst.append(action(x, key[i]))
            if x.isalpha():
                i = (i + 1) % len(key)
        
        return ''.join(res_lst)

    def encrypt_text(self, plaintext, key):
        def encrypt_symbol(symbol, key):
            encrypt_table = VigenereCipher.VIGENERE_ENCRYPT_TABLE
            change_case = not symbol.isupper()
            symbol = symbol.upper()
            key = key.upper()
            
            e = encrypt_table[symbol][key] if symbol in encrypt_table.keys() else symbol
            e = e.lower() if change_case else e
            
            return e

        return self.process_text_with_key(plaintext, key, encrypt_symbol)

    def decrypt_text(self, ciphertext, key):
        def decrypt_symbol(symbol, key):
            decrypt_table = VigenereCipher.VIGENERE_DECRYPT_TABLE
            change_case = not symbol.isupper()
            symbol = symbol.upper()
            key = key.upper()
            
            e = decrypt_table[key][symbol] if symbol in decrypt_table.keys() else symbol
            e = e.lower() if change_case else e
            
            return e

        return self.process_text_with_key(ciphertext, key, decrypt_symbol)


if __name__ == '__main__':
    ENCRYPT_MODE = 0
    DECRYPT_MODE = 1

    print('=== VIGINERE CIPHER ===')
    cipher = VigenereCipher()
    
    print('ENCRYPT[0]/DECRYPT[1]:', end=' ')
    mode = int(input())

    if mode == ENCRYPT_MODE:
        print('Plaintext:')
        plaintext = input()
        print('Key:')
        key = input()

        ciphertext = cipher.encrypt_text(plaintext, key)

        print('Ciphertext:')
        print(ciphertext)
    elif mode == DECRYPT_MODE:
        print('Ciphertext:')
        ciphertext = input()
        print('Key:')
        key = input()

        plaintext = cipher.decrypt_text(ciphertext, key)

        print('Plaintext:')
        print(plaintext)
    else:
        print('ERROR: WRONG MODE')
