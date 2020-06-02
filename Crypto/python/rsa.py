# key generation
# choose p and q (primes)
# n = p * q
# m = (p - 1) * (q - 1)
# find e: gcd(e, m) = 1 [Euclidean Algorithm]
# public key: (e, n)
# find d: e * d = 1 (mod m) [Extended Euclidean Algorithm]
# private key: (d, p, q) = (d, n)

def powerModulo(a, n, m):
    '''Find a^n mod m'''
    print(a, n, m)
    if n == 0:
        return 1
    if n % 2 == 0:
        return powerModulo((a ** 2) % m, n // 2, m) % m
    return (a * powerModulo(a, n - 1, m)) % m

def gcd(a, b):
    '''Find largest n which divides both a and b'''
    if b == 0:
        return a
    return gcd(b, a % b)

def coprime(n):
    '''Find m such that gcd(m, n) = 1'''
    m = 2
    while m < n and gcd(m, n) != 1:
        m += 1
    return m

def inverseModulo(n, m):
    '''Find k such that k * n = 1 (mod m)'''
    penult = 0
    ultima = 1
    a = m # a > b hope
    b = n

    while b != 0:
        q = a // b
        a, b = b, a - q * b
        penult, ultima = ultima, penult - q * ultima

    return penult % m

def get_two_large_primes():
    # stub
    return (64662811, 56903261)

def char_to_number(c):
    return ord(c)

def number_to_char(n):
    return chr(n)
    
def generate_keys(p, q):
    #p, q = get_two_large_primes()

    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = coprime(phi)
    d = inverseModulo(e, phi)

    return {
        'public_key': { 'e': e, 'n': n },
        'private_key': { 'd': d, 'n': n }
    }

def encrypt_number(number, public_key):
    e, n = public_key['e'], public_key['n']
    if number >= n:
        raise ValueError('Input number is too large')
    cipher = powerModulo(number, e, n)
    return cipher

def decrypt_number(number, private_key):
    d, n = private_key['d'], private_key['n']
    if number >= n:
        raise ValueError('Input number is too large')
    plain = powerModulo(number, d, n)
    return plain

def encrypt(message, public_key):
    plaintext = map(char_to_number, list(message))
    ciphertext = list(map(lambda x: encrypt_number(x, public_key), plaintext))
    return ciphertext

def decrypt(message, private_key):
    ciphertext = message
    plaintext = map(lambda x: number_to_char(decrypt_number(x, private_key)), ciphertext)
    return ''.join(plaintext)

keys = generate_keys(*get_two_large_primes())
