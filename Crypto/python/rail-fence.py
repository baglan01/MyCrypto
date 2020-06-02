from functools import reduce as reduce

class RailsCipher:
    def get_valid_list_from_string(self, string):
        '''Validate string and return list'''
        def valid_symbol(x):
            return True
        lst = list(filter(valid_symbol, list(string)))
        return lst

    def print_table(self, table):
        for row in table:
            for x in row:
                if x is None:
                    print(' ', end='')
                else:
                    print(x, end='')
            print()

    def zig_zag_movement(self, table, lst=None, collect=False):
        '''
        Accomplish zig-zag movement through the table,
        if collect is False, cells along the road will be filled with elements of lst,
        otherwise function will return list of collected symbols
        '''

        MOVE_DOWN = 1
        MOVE_UP = -1

        rows = len(table)
        cols = len(table[0])

        if collect:
            lst = []

        i, j = 0, 0
        d = MOVE_DOWN
        while i < cols:
            if collect:
                lst.append(table[j][i])
            else:
                table[j][i] = lst[i]
           
            i, j = i + 1, j + d
            if j == rows:
                d = MOVE_UP
                j = rows - 2
            elif j == -1:
                d = MOVE_DOWN
                j = 1

        if collect:
            return lst
        else:
            return table

    def create_table(self, lst, rows):
        cols = len(lst)
        table = [[None] * cols for _ in range(rows)]
        table = self.zig_zag_movement(table, lst, collect=False)
        return table

    def collect_text_from_table(self, table):
        '''Collect text row-by-row'''
        table = [list(filter(lambda x: x is not None, row)) for row in table]
        lst = reduce(lambda x, y: x + y, table)
        return ''.join(lst)

    def encrypt_text(self, plaintext, key):
        lst = self.get_valid_list_from_string(plaintext)
        table = self.create_table(lst, key)
        return self.collect_text_from_table(table)

    def decrypt_text(self, ciphertext, key):
        lst = self.get_valid_list_from_string(ciphertext)
        table = self.create_table(lst, key)

        rows, cols = len(table), len(table[0])
        k = 0
        for i in range(rows):
            for j in range(cols):
                if table[i][j] is not None:
                    table[i][j] = lst[k]
                    k += 1
        
        lst = self.zig_zag_movement(table, collect=True)
        return ''.join(lst)

if __name__ == '__main__':
    print('=== RAILS CIPHER ===')
    cipher = RailsCipher()
    
    ENCRYPT_MODE = 0
    DECRYPT_MODE = 1

    print('ENCRYPT[0]/DECRYPT[1]:', end=' ')
    mode = int(input())

    if mode == ENCRYPT_MODE:
        print('Plaintext:')
        plaintext = input()
        print('Key:')
        key = int(input())

        ciphertext = cipher.encrypt_text(plaintext, key)

        print('Ciphertext:')
        print(ciphertext)
    elif mode == DECRYPT_MODE:
        print('Ciphertext:')
        ciphertext = input()
        print('Key:')
        key = int(input())

        plaintext = cipher.decrypt_text(ciphertext, key)

        print('Plaintext:')
        print(plaintext)
    else:
        print('ERROR: WRONG MODE')

    print('=== FINISHED ===')
