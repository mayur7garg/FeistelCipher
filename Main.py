import FeistelCipher as fc
import StandardCryptFunctions as scf
import CryptFunctions as cfs

if __name__ == '__main__':
    numToEncrypt = 1_234_567

    funcList = cfs.CryptFunctions()

    funcList.addFunc(scf.identity, 0)
    funcList.addFunc(scf.add, 1)
    funcList.addFunc(scf.multiply, 2)
    funcList.addFunc(scf.addThenMultiply, 3)
    funcList.addFunc(scf.strLength, 4)
    funcList.addFunc(scf.power, 5)
    funcList.addFunc(scf.reverse, 6)
    funcList.addFunc(scf.truncate, 7)
    funcList.addFunc(scf.remainder, 8)
    funcList.addFunc(scf.quotient, 9)

    cipher = fc.FeistelCipher(funcList)

    enc = cipher.encrypt(numToEncrypt)
    print(f"Encrypted {numToEncrypt} as {enc}.")

    dec = cipher.decrypt(enc)
    print(f"Decrypted {enc} as {dec}.")

    if dec == numToEncrypt:
        print("Encryption/Decryption using Feistel Cipher was successful.")
