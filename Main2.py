import feistelcipher.FeistelCipher as fc
import feistelcipher.StandardCryptFunctions as scf
import feistelcipher.CryptFunctions as cfs
import random as rnd

ALL_FUNCS = [(scf.identity, 0), (scf.add, 1), (scf.multiply, 1), 
    (scf.strLength, 0), (scf.power, 1), (scf.reverse, 0), (scf.truncate, 1), 
    (scf.remainder, 1), (scf.quotient, 1), (scf.scaledDistance, 4)]

NUM_RANGE = 9_999
NUM_COUNT = 1_000
MAX_FUNC_COUNT = 10

if __name__ == '__main__':

    rnd.shuffle(ALL_FUNCS)

    funcList = cfs.CryptFunctions()

    for i in range(rnd.randint(1, MAX_FUNC_COUNT)):
        func, keyCount = rnd.choice(ALL_FUNCS)
        key = [rnd.randint(-10, 10) for i in range(keyCount)]
        funcList.addFunc(func, key)

    cipher = fc.FeistelCipher(funcList)
    cipher.printCipherBlock()

    numsToEncrypt = [0] + [rnd.randint(-NUM_RANGE, NUM_RANGE) for i in range(NUM_COUNT)]
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
    else:
        print("ERROR")
        for i in range(len(numsToEncrypt)):
            if numsToEncrypt[i] != decryptedNums[i]:
                print(numsToEncrypt[i], encryptedNums[i], decryptedNums[i])
    print()