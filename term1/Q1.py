# q1
def encrypt_ceasar(plaintext: str, shift: int):
    encrypt = ""
    for char in plaintext:
        asci = ord(char)
        # for Uppers
        if 65 <= asci <= 90:
            shifted_asci = asci + shift
            if shifted_asci > 90:
                shifted_asci = (65 + (shifted_asci - 90))
            encrypt += (chr(shifted_asci))
        # for lowers
        elif 97 <= asci <= 122:
            shifted_asci = asci + shift
            if shifted_asci > 122:
                shifted_asci = (97 + (shifted_asci - 122))
            encrypt += (chr(shifted_asci))
        # another characters
        else:
            a = ord(char)
            encrypt += (chr(a))

    return encrypt

def decrypt_ceasar(ciphertext: str, shift: int):
    decrypt = ""
    for char in ciphertext:
        asci = ord(char)
        # for uppers
        if 65 <= asci < 65 + shift:
            shifted_asci = 90 - (shift - (asci - shift))
            decrypt += chr(shifted_asci)
            # for lowers
        elif 97 <= asci < 97 + shift:
            shifted_asci = 122 - (shift - (asci - shift))
            decrypt += chr(shifted_asci)
            # another characters
        else:
            decrypt += chr(asci)

    return decrypt

plaintext = input("input_encrypt: ")
shift = int(input("shift : "))
print(encrypt_ceasar(plaintext, shift))
ciphertext = input("ciphertext: ")
shift2 = int(input("shift: "))
print(decrypt_ceasar(plaintext, shift))
