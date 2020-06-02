from substitution_key import SubstitutionKey

class SubstitutionEncrypter:
    '''Class for performing substitution cipher encryption with specified key'''

    def encrypt(self, plaintext, key):
        '''Return ciphertext after encryption of plaintext with specified key'''
        ciphertext = key.encode_text(plaintext)
        return ciphertext


if __name__ == '__main__':
    print('=== Substitution encrypter ===')

    encrypter = SubstitutionEncrypter()

    print('Plaintext:')
    plaintext = input()

    print('Key:')
    print('- plaintext alphabet:')
    plaintext_abc = input().upper()
    print('- ciphertext alphabet:')
    ciphertext_abc = input().upper()

    key = SubstitutionKey(list(plaintext_abc), list(ciphertext_abc))

    print('Ciphertext:')
    ciphertext = encrypter.encrypt(plaintext, key)
    print(ciphertext)

    print('=== FINISHED ===')

