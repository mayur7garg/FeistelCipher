import feistelcipher.FeistelCipher as fc
import feistelcipher.StandardCryptFunctions as scf
import feistelcipher.CryptFunctions as cfs
import random as rnd

if __name__ == '__main__':
    funcList = cfs.CryptFunctions()

    print()

    for i in range(rnd.randint(1, 10)):
        func = rnd.choice(scf.ALL_FUNCTIONS)
        key = rnd.randint(1, 10)
        print(f"Adding function '{func.__name__}' with key {key}.")
        funcList.addFunc(func, key)

    cipher = fc.FeistelCipher(funcList)

    numsToEncrypt = [rnd.randint(0, 9_999_999) for i in range(5)]
    encryptedNums = []
    decryptedNums = []

    print()

    for num in numsToEncrypt:
        enc = cipher.encrypt(num)
        encryptedNums.append(enc)
        print(f"Encrypted {num} as {enc}.")

    print()

    for enc in encryptedNums:
        dec = cipher.decrypt(enc)
        decryptedNums.append(dec)
        print(f"Decrypted {enc} as {dec}.")

    print()

    if numsToEncrypt == decryptedNums:
        print("Encryption/Decryption using Feistel Cipher was successful.")

    print()
