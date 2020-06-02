class ShiftCipher:
    '''Base class for shift cipher encrypter&decrypter which provides basic utility methods'''

    MAX_LETTERS = 26
    LETTERS = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                'W', 'X', 'Y', 'Z' ]

    @staticmethod
    def shift_letters_left(letters, n):
        '''Return list of letters shifted left by n'''
        if n == 0:
            return letters.copy()
        return ShiftCipher.shift_letters_left(letters[1:] + letters[:1], n - 1)

    @staticmethod
    def shift_letters_right(letters, n):
        '''Return list of letters shifted right by n'''
        if n == 0:
            return letters.copy()
        return ShiftCipher.shift_letters_right(letters[-1:] + letters[:-1], n - 1)
