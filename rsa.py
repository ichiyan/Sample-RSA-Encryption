from collections import namedtuple

def main():
    p = 11
    q = 13
    e = 7
    d = 223
    n = p * q
    z = (p-1) * (q-1)

    cipher_text = encrypt(e, n, "RASTAMAN")
    print(cipher_text.string)

    plain_text = decrypt(d, n, cipher_text.list)
    print(plain_text.string)

def encrypt(e, n, plain_text):
    cipher_list = [chr (ord(ch) ** e % n) for ch in plain_text]
    #cipher_text_string = ''.join(map(str, cipher_text))
    cipher_string = ''.join([ chr(9608) if ord(char) > 126 or ord(char) < 33 else str(char) for char in cipher_list])
    cipher = namedtuple('cipher', ['list', 'string'])

    return cipher(cipher_list, cipher_string)

def decrypt(d, n, cipher_text):
    plain_text = [chr (ord(ch) ** d % n) for ch in cipher_text]
    plain_text_string = ''.join(map(str, plain_text))
    plain = namedtuple('plain', ['list', 'string'])
    
    return plain(plain_text, plain_text_string)
   
main()