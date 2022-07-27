
def cc_encrypt(message, key):
    encryption = ""
    for c in message:
        encryption = encryption + chr((ord(c) + key) % 26 + 65) 
    return encryption


def cc_decrypt(encrypted_message, key):
    decryption = ""
    if key < 0:
        key *= -1
    for c in encrypted_message:
        #Convert to ASCII code
        c = ord(c)
        #Convert to position in the alphabet
        c -= 65
        #Apply decrpytion
        c -= key
        c%=26
        #Back to ASCII code
        c += 65
        #Back to character
        c = chr(c)
        decryption += c
         

    return decryption


def run_tests():
    print(cc_decrypt("ALZAPUN", 7))
    print(cc_decrypt("JXKAQYXKH ", 23))
    print(cc_decrypt("BSUOHWJS", -14))
    print(cc_decrypt("HUQBBOBEDWJUNJMYJXRYWDKCRUH", 135762))


if __name__ == '__main__':
    run_tests()
