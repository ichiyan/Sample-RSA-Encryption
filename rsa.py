import math
import random
from collections import namedtuple

def main():

    #GIVEN VALUES

    p = 11
    q = 13
    e = 7
    d = 223
    n = p * q
    z = (p-1) * (q-1)

    public_key = {
        "n": n,
        "e": e
    }

    private_key = {
        "n": n,
        "d": d,
    }

    print(f"\nGiven values:\n\t p = {p}\n\t q = {q}\n\t e = {e}\n\t d = {d}\n\t n = {n}\n\t z = {z}")

    print("\n\t PUBLIC KEY", public_key)
    print("\n\t PRIVATE KEY", private_key)

    to_encrypt = input("\nEnter message to be encrypted: ")
    cipher_text = encrypt(e, n, to_encrypt)
    print("\nENCRYPTED MESSAGE CHARACTERS: " , cipher_text.list)
    print("ENCRYPTED MESSAGE: ", cipher_text.string)

    to_decrypt = input("\nEnter message to be decrypted: ")
    plain_text = decrypt(d, n, to_decrypt)
    print("\nDECRYPTED MESSAGE CHARACTERS: ", plain_text.list)
    print("DECRYPTED MESSAGE: ", plain_text.string)


    # GENERATE KEYS THROUGH USER INPUTTED VALUES FOR p AND q

    print("\nGenerate Keys through user inputted values for p and q (uncomment generate_keys_by_user_input in main() if you wish to enter your own values)")

    p = input("\nEnter a large prime number: ")
    while is_valid(p) == False:
        print("\nInvalid number. Number must be a prime number.")
        p = input("\nEnter a large prime number: ")

    p = int(p)

    q = input("\nEnter another large prime number: ")
    q = int(q)
    while is_valid(q) == False or p == q:
        print("\nInvalid number. Number must be ANOTHER prime number.")
        q = input("\nEnter another large prime number: ")
        q = int(q)

    # getting the values for e, d, n, and z through user input
    # if this is uncommented, comment out the next assignment of values
    values = generate_keys_by_user_input(p, q)

    #getting the values for e, d, n, and z directly
    # if this is uncommented, comment out the previous assignment of values
    #values = generate_keys(p, q)

    e = values.e
    d = values.d
    n = values.n
    z = values.z
    public_key = values.public_key
    private_key = values.private_key

    print(f"\nGenerated values:\n\t p = {p}\n\t q = {q}\n\t e = {e}\n\t d = {d}\n\t n = {n}\n\t z = {z}\n")

    print("\nPUBLIC KEY", public_key)
    print("\nPRIVATE KEY", private_key)

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
    
    # this returns readable representaion of printable and non printable characters e.g., null, backspace 
    #and removes single quotation surrounding result
    cipher_string = ascii(''.join(map(str, cipher_list)))[1:-1]
    cipher = namedtuple('cipher', ['list', 'string'])

    return cipher(cipher_list, cipher_string)

def decrypt(d, n, cipher_text):

    cipher_text = cipher_text.encode().decode('unicode-escape')
    plain_text = [chr (ord(ch) ** d % n) for ch in cipher_text]
    plain_text_string = ''.join(map(str, plain_text))
    plain = namedtuple('plain', ['list', 'string'])
    
    return plain(plain_text, plain_text_string)

def generate_keys(p, q):
    n = p * q
    z = (p-1) * (q-1)

    possible_e_values = [i for i in range(1, z) if is_valid_e(i, n, z)]
    e = random.choice(possible_e_values)
    possible_d_values = [j for j in range(1, 1000) if is_valid_d(j, e, z)]
    d = random.choice(possible_d_values)
    
    public_key = {
        "n": n,
        "e": e
    }

    private_key = {
        "n": n,
        "d": d,
    }

    values = namedtuple('values', ['n', 'z', 'e', 'd', 'public_key', 'private_key'])

    return values(n, z, e, d, public_key, private_key)
    

def generate_keys_by_user_input(p, q):
    n = p * q
    z = (p-1) * (q-1)

    e = input(f"\nEnter a number < {n} and has no common factor (other than 1) with {z}: ")

    while is_valid_e(e, n, z) == False:
        print("\nInvalid number.")
        e = input(f"\nEnter a number < {n} and has no common factor (other than 1) with {z}: ")

    e = int(e)
    
    d = input(f"\nEnter a number d that satisfies the condition: {e}(d) - 1 is exactly divisible by {z}: ")

    while is_valid_d(d, e, z) == False:
        print("\nInvalid number.")
        d = input(f"\nEnter a number d that satisfies the condition: {e}(d) - 1 is exactly divisible by {z}: ")
    
    d = int(d)

    public_key = {
        "n": n,
        "e": e
    }

    private_key = {
        "n": n,
        "d": d,
    }

    values = namedtuple('values', ['n', 'z', 'e', 'd', 'public_key', 'private_key'])

    return values(n, z, e, d, public_key, private_key)


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
           return True if math.gcd(num, z) == 1 else False
        else:
            return False
    except ValueError:
        return False

def is_valid_d(num, e, z):
    try:
        num = int(num)
        # same as if (e * num - 1) % z == 0:
        return True if e * num % z == 1 else False
    except ValueError:
        return False


main()