from typing import Tuple
from .CryptFunctions import CryptFunctions

class FeistelCipher():
    class EncryptedObject():
        def __init__(self, left: int, right: int, blockLength: int):
            self.left = left
            self.right = right
            self.blockLength = blockLength

        def __str__(self) -> str:
            return str((self.left, self.right, self.blockLength))

        def __repr__(self) -> str:
            return self.__class__.__name__ + str((self.left, self.right, self.blockLength))

    def __init__(self, cryptFuncs: CryptFunctions):
        self.cryptFuncs = cryptFuncs

    def execCipherBlock(self, left: int, right: int, cryptFunc: CryptFunctions.CryptFunctionBlock) -> Tuple[int, int]:
        temp = left ^ cryptFunc.execute(right)
        return (right, temp)

    def printCipherBlock(self):
        print(self.cryptFuncs)

    def encrypt(self, numToEncrypt: int) -> 'EncryptedObject':
        signOffset = 1 if numToEncrypt < 0 else 0
        numToEncrypt = str(numToEncrypt)

        if len(numToEncrypt) % 2 == 1:
            numToEncrypt = numToEncrypt[:signOffset] + '0' + numToEncrypt[signOffset:]

        blockLength = len(numToEncrypt) // 2

        if (blockLength == 1 and signOffset == 1) or (int(numToEncrypt[:blockLength]) == 0):
            leftHalf = int(numToEncrypt)
            rightHalf = 0
        else:
            leftHalf = int(numToEncrypt[blockLength:])
            rightHalf = int(numToEncrypt[:blockLength])

        for cryptFunc in self.cryptFuncs:
            (leftHalf, rightHalf) = self.execCipherBlock(leftHalf, rightHalf, cryptFunc)

        return self.EncryptedObject(rightHalf, leftHalf, blockLength)

    def decrypt(self, encryptedObject: EncryptedObject) -> int:
        leftHalf = encryptedObject.left
        rightHalf = encryptedObject.right
        blockLength = encryptedObject.blockLength

        for cryptFunc in self.cryptFuncs[::-1]:
            (leftHalf, rightHalf) = self.execCipherBlock(leftHalf, rightHalf, cryptFunc)

        leftHalf = str(leftHalf)
        rightHalf = str(rightHalf).rjust(blockLength, '0')

        return int(rightHalf) if int(leftHalf) == 0 else int(leftHalf + rightHalf)
