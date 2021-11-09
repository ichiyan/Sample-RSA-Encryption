from collections import namedtuple

def main():
    p = 11
    q = 13
    e = 7
    d = 223
    n = p * q
    z = (p-1) * (q-1)

    to_encrypt = input("Enter message to be encrypted: ")
    cipher_text = encrypt(e, n, to_encrypt)
    print("ENCRYPTED MESSAGE CHARACTERS: " , cipher_text.list)
    print("ENCRYPTED MESSAGE: ", cipher_text.string)

    to_decrypt = input("Enter message to be decrypted: ")
    plain_text = decrypt(d, n, to_decrypt)
    print("DECRYPTED MESSAGE CHARACTERS: ", plain_text.list)
    print("DECRYPTED MESSAGE: ", plain_text.string)


def encrypt(e, n, plain_text):

    cipher_list = [chr (ord(ch) ** e % n) for ch in plain_text]

    # this prints a vertical rectangle for non printable values but copying the encrypted 
    # message and pasting it as input for the message to be decrypted won't yield the correct 
    # results since the rectangle does not hold the value of the encrypted character.
    
    # cipher_string = ''.join([ chr(9608) if ord(char) > 126 or ord(char) < 33 else str(char) for char in cipher_list])
    
    cipher_string = ascii(''.join(map(str, cipher_list)))[1:-1]
    cipher = namedtuple('cipher', ['list', 'string'])

    return cipher(cipher_list, cipher_string)

def decrypt(d, n, cipher_text):

    cipher_text = cipher_text.encode().decode('unicode-escape')
    plain_text = [chr (ord(ch) ** d % n) for ch in cipher_text]
    plain_text_string = ''.join(map(str, plain_text))
    plain = namedtuple('plain', ['list', 'string'])
    
    return plain(plain_text, plain_text_string)
   
main()