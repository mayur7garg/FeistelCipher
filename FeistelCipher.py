from typing import Tuple
from CryptFunctions import CryptFunctions

class FeistelCipher():
    class EncryptedObject():
        def __init__(self, left: int, right: int, blockLength: int):
            self.left = left
            self.right = right
            self.blockLength = blockLength

        def __str__(self) -> str:
            return str(self.left) + str(self.right)

    def __init__(self, cryptFuncs: CryptFunctions):
        self.cryptFuncs = cryptFuncs

    def execCipherBlock(self, left: int, right: int, cryptFunc: CryptFunctions.CryptFunctionBlock) -> Tuple[int, int]:
        temp = left ^ cryptFunc.execute(right)
        return (right, temp)

    def encrypt(self, numToEncrypt: int) -> 'EncryptedObject':
        numToEncrypt = str(numToEncrypt)
        if len(numToEncrypt) % 2 == 1:
            numToEncrypt = '0' + numToEncrypt

        blockLength = len(numToEncrypt)//2
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
            (leftHalf, rightHalf) = self.execCipherBlock(
                leftHalf, rightHalf, cryptFunc)

        leftHalf = str(leftHalf).rjust(blockLength, '0')
        rightHalf = str(rightHalf).rjust(blockLength, '0')

        return int(leftHalf+rightHalf)
