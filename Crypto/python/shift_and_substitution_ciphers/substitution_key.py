
class SubstitutionKey:
    '''Class for encoding symbols with use of substition dictionary'''

    def __init__(self, keys, values):
        '''Provide keys and values for substituion dictionary'''
        keys = list(map(lambda x: x.upper(), keys))
        value = list(map(lambda x: x.upper(), values))
        self.sub_dict = dict(map(lambda x, y: [x, y], keys, values))

    def encode_symbol(self, symbol):
        '''Return encoded symbol if its substitution was specified,
            otherwise return it without changing'''
        symbol = symbol.upper()
        if symbol in self.sub_dict.keys():
            return self.sub_dict[symbol]
        else:
            return symbol

    def encode_text(self, text):
        '''Return encoded text with use of internal substitution dictionary'''
        lst = list(text)
        lst = list(map(self.encode_symbol, text))
        return ''.join(lst)

    @staticmethod
    def parsePairs(pairs):
        '''Return SubstitutionKey object after parsing string of pairs'''
        pairs = pairs.split(None)
        dt = dict(map(lambda x: [x[0], x[1]], pairs))
        key = SubstitionKey(list(dt.keys()), list(dt.values()))
        return key

    def __str__(self):
        return str(self.sub_dict)
