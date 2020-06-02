import PySimpleGUI as sg


# RSA Algorithm
def prime_num(n):
    if n < 2:
        return False
    x = 2
    while x ** 2 <= n:
        if n % x == 0:
            return False
        x += 1
    return True


def RSA(p, q):
    # Pick p and q

    N = p * q  # Mod for cipher
    F = (p - 1) * (q - 1)  # Euler function
    prime_factors = []

    while not F == 1:
        for i in range(2, F + 1):
            if F % i == 0:
                prime_factors.append(i)
                F //= i
                break

    # Pick e
    e = int
    for i in range(2, (p - 1) * (q - 1)):
        if i not in prime_factors and prime_num(i):
            e = i

    # Pick d
    d = 1
    while (e * d) % ((p - 1) * (q - 1)) != 1:
        d += 1

    return e, N, d,


def E_str_RSA(text, e, N):
    if len(text) < N:
        return [(ord(c) % 122 - 31) ** e % N for c in text]
    else:
        print("Text is too large")


def D_str_RSA(secret, d, N):
    return ''.join(chr((c ** d % N) % 122 + 31) for c in secret)
sg.theme('DarkAmber')

layout1 = [[sg.Text("Enter the Text")],
           [sg.InputText(size=(30, 30), key='text')],
           [sg.Button('Encrypt'), sg.Button('Decrypt')]]

window1 = sg.Window('RSA').Layout(layout1)

while True:
    event1, text = window1.Read()

    if event1 == 'Encrypt':
        layout2 = [[sg.Text('Enter 2 prime numbers :')],
                   [sg.Text('P :'), sg.InputText(size=(15, 15), key='p'), sg.Text('Q:'),
                    sg.InputText(size=(15, 15), key='q')],
                   [sg.Button('Ok')]]

        window2 = sg.Window('RSA Encryption').Layout(layout2)

        while True:
            event2, values = window2.Read()
            p, q = int(values['p']), int(values['q'])

            
            if event2 == 'Ok':
                if not (prime_num(p) and prime_num(q)):
                    if not prime_num(p):
                        sg.Print("p is not prime number \n", "click Reset")
                    if not prime_num(q):
                        sg.Print("q is not prime number \n", "click Reset")
                else:
                    E, n, D = RSA(p, q)
                    secret = str(E_str_RSA(text=str(text['text']), e=E, N=n))
                    sg.Print("Secret message :", secret.replace(",", ""), "\n Key D :", D, "N :", n)

    if event1 == 'Decrypt':
        layout3 = [[sg.Text("Key D :"), sg.InputText(size=(15, 15), key='d'), sg.Text("Enter N:"),
                    sg.InputText(size=(15, 15), key='N')],
                   [sg.Button('Ok')]]

        window3 = sg.Window('RSA Decryption').Layout(layout3)

        while True:
            event3, values = window3.Read()
            D, N = int(values['d']), int(values['N'])

            

            if event3 == 'Ok':
                sg.Print(D_str_RSA([int(c) for c in text['text'].split()], D, N))
