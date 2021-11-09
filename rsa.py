import math

from collections import namedtuple

def main():
    p = 11
    q = 13
    e = 7
    d = 223
    n = p * q
    z = (p-1) * (q-1)

    #TEST BY USER INPUT

    # p = input("\nEnter a large prime number: ")

    # while is_valid(p) == False:
    #     print("\nInvalid number.")
    #     p = input("\nEnter a large prime number: ")

    # q = input("\nEnter another large prime number: ")

    # while is_valid(q) == False:
    #     print("\nInvalid number.")
    #     q = input("\nEnter another large prime number: ")

    # p = int(p)
    # q = int(q)
    # n = p * q
    # z = (p-1) * (q-1)

    # e = input(f"\nEnter a number < {n} and has no common factor (other than 1) with {z}: ")

    # while is_valid_e(e, n, z) == False:
    #     print("\nInvalid number.")
    #     e = input(f"\nEnter a number < {n} and has no common factor (other than 1) with {z}: ")

    # e = int(e)
    
    # d = input(f"\nEnter a number d that satisfies the condition: {e}(d) - 1 is exactly divisible by {z}: ")

    # while is_valid_d(d, e, z) == False:
    #     print("\nInvalid number.")
    #     d = input(f"\nEnter a number d that satisfies the condition: {e}(d) - 1 is exactly divisible by {z}: ")
    
    # d = int(d)

    # public_key = (n, e)
    # private_key = (n, d)

    to_encrypt = input("\nEnter message to be encrypted: ")
    cipher_text = encrypt(e, n, to_encrypt)
    print("\nENCRYPTED MESSAGE CHARACTERS: " , cipher_text.list)
    print("ENCRYPTED MESSAGE: ", cipher_text.string)

    to_decrypt = input("\nEnter message to be decrypted: ")
    plain_text = decrypt(d, n, to_decrypt)
    print("\nDECRYPTED MESSAGE CHARACTERS: ", plain_text.list)
    print("DECRYPTED MESSAGE: ", plain_text.string)


def encrypt(e, n, plain_text):

    cipher_list = [chr (ord(ch) ** e % n) for ch in plain_text]

    # this prints a vertical rectangle for non printable values but copying the encrypted 
    # message and pasting it as input for the message to be decrypted won't yield the correct 
    # results since the rectangle does not hold the value of the encrypted character.

    # cipher_string = ''.join([ chr(9608) if ord(char) > 126 or ord(char) < 33 else str(char) for char in cipher_list])
    
    # this returns readable representaion of non printable characters e.g., null, backspace
    cipher_string = ascii(''.join(map(str, cipher_list)))[1:-1]
    cipher = namedtuple('cipher', ['list', 'string'])

    return cipher(cipher_list, cipher_string)

def decrypt(d, n, cipher_text):

    cipher_text = cipher_text.encode().decode('unicode-escape')
    plain_text = [chr (ord(ch) ** d % n) for ch in cipher_text]
    plain_text_string = ''.join(map(str, plain_text))
    plain = namedtuple('plain', ['list', 'string'])
    
    return plain(plain_text, plain_text_string)

def is_valid(num):
    try:
        num = int(num)
        if num > 1:
            for i in range(2, num):
                if num%i == 0:
                    return False
        else:
            return False
    except ValueError:
        return False

def is_valid_e(num, n, z):
    try:
        num = int(num)
        if num < n:
           if math.gcd(num, z) == 1:
               return True
        else:
            return False
    except ValueError:
        return False

def is_valid_d(num, e, z):
    try:
        num = int(num)
        if (e * num - 1) % z == 0:
            return True
        else:
            return False
    except ValueError:
        return False
        

main()