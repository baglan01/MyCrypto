from substitution_key import SubstitutionKey

class SubstitutionDecrypter:
    '''Class for performing substitution cipher decryption with specified key'''

    def decrypt_with_key(self, ciphertext, key):
        '''Return plaintext after decryption of ciphertext with specified key'''
        plaintext = key.encode_text(ciphertext)
        return plaintext

if __name__ == '__main__':
    print('=== Substitution Decrypter ===')

    decrypter = SubstitutionDecrypter()

    print('Ciphertext: ')
    ciphertext = input()

    print('Key:')
    print('- plaintext alphabet:')
    plaintext_abc = input().upper()
    print('- ciphertext alphabet:')
    ciphertext_abc = input().upper()

    key = SubstitutionKey(ciphertext_abc, plaintext_abc)

    print('Plaintext: ')
    plaintext = decrypter.decrypt_with_key(ciphertext, key)
    print(plaintext)

    print('=== FINISHED ===')
