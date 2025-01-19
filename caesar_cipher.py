#!/usr/bin/env python3


def encrypt(msg: str, key: int):
    """
    encrypt(msg: str, key: int)
    ===========================
    Encrypt using Caesar Cipher.

    Accept:
        msg: String: Message to be encrypted.
        key: Integer: The number of rotation to be done in forward.

    Return:
        ciphertext: String: The encrypted text (ciphertext)
    """
    ciphertext: str = ""
    for i in msg:
        x = ord(i) + key
        if x > ord('z'):
            x = ord('a') + (x - ord('z') - 1)
        ciphertext += chr(x)

    return ciphertext

def decrypt(ciphertext: str, key: int):
    """
    decrypt(ciphertext: str, key: int)
    ==================================
    Decrypt using Caesar Cipher.

    Accept:
        ciphertext: String: The encrypted text
        key: Integer: The number of rotation to be done in reverse.

    Return:
        plaintext: String: The decrypted text (plaintext)
    """
    plaintext = ""
    for i in ciphertext:
        x = ord(i) - key
        if x < ord('a'):
            x = ord('z') - (ord('a') - x - 1)
        plaintext += chr(x)

    return plaintext

if __name__ == '__main__':
    # Run if run as a script.
    print('Encrypted message:\t', encrypt(input('Enter the message:\t'), int(input('Enter the key:\t'))))
    print('Decrypted message:\t', decrypt(input('Enter the ciphertext:\t'), int(input('Enter key:\t'))))
