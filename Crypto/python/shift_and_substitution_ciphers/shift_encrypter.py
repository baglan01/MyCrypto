from shift_cipher import ShiftCipher
from substitution_key import SubstitutionKey

class ShiftEncrypter(ShiftCipher):
    '''Class for performing shift cipher encryption with specified key'''

    def encrypt(self, plaintext, key):
        '''Return ciphertext after encryption of message with specified key'''

        shifted_letters = self.shift_letters_left(self.LETTERS, key % self.MAX_LETTERS)
        sub_key = SubstitutionKey(self.LETTERS, shifted_letters)

        ciphertext = sub_key.encode_text(plaintext)

        return ciphertext


if __name__ == '__main__':
    print('=== Shift Encrypter ===')

    encoder = ShiftEncrypter()
    
    print('Input plaintext:')
    plaintext = input()

    print('Input key:')
    key = int(input())

    print('\nCiphertext:')
    ciphertext = encoder.encrypt(plaintext, key)
    print(ciphertext)

    print('=== FINISHED ===')
