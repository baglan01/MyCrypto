from shift_cipher import ShiftCipher
from substitution_key import SubstitutionKey

class ShiftDecrypter(ShiftCipher):
    '''Class for performing shift cipher decryption'''

    def decrypt_with_key(self, ciphertext, key):
        '''Return decrypted message with use of specified key'''

        shifted_letters = self.shift_letters_right(self.LETTERS, key % self.MAX_LETTERS)
        sub_key = SubstitutionKey(self.LETTERS, shifted_letters)

        plaintext = sub_key.encode_text(ciphertext)
        
        return plaintext


if __name__ == '__main__':
    print('=== Shift Decrypter ===')

    decoder = ShiftDecrypter()

    print('Ciphertext:')
    ciphertext = input()
    
    print('Key:')
    key = int(input())

    print('Plaintext:')
    plaintext = decoder.decrypt_with_key(ciphertext, key)

    print(plaintext)

    print('=== FINISHED ===')
