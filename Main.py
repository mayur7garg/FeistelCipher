import feistelcipher.FeistelCipher as fc
import feistelcipher.StandardCryptFunctions as scf
import feistelcipher.CryptFunctions as cfs
import random as rnd

if __name__ == '__main__':
    numToEncrypt = rnd.randint(-9_999, 9_999)

    funcList = cfs.CryptFunctions()

    funcList.addFunc(scf.identity)
    funcList.addFunc(scf.add, [rnd.randint(-10, 10)])
    funcList.addFunc(scf.multiply, [rnd.randint(-10, 10)])
    funcList.addFunc(scf.strLength)
    funcList.addFunc(scf.power, [rnd.randint(-10, 10)])
    funcList.addFunc(scf.reverse)
    funcList.addFunc(scf.truncate, [rnd.randint(-10, 10)])
    funcList.addFunc(scf.remainder, [rnd.randint(-10, 10)])
    funcList.addFunc(scf.quotient, [rnd.randint(-10, 10)])
    funcList.addFunc(scf.scaledDistance, [rnd.randint(-10, 10) for i in range(4)])

    cipher = fc.FeistelCipher(funcList)
    cipher.printCipherBlock()

    enc = cipher.encrypt(numToEncrypt)
    print(f"Encrypted {numToEncrypt} as {enc}.")

    dec = cipher.decrypt(enc)
    print(f"Decrypted {enc} as {dec}.")

    if dec == numToEncrypt:
        print("Encryption/Decryption using Feistel Cipher was successful.")
