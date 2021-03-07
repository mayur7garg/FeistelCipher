"""StandardCryptFunctions

This script contains some standard functions which can be used in the
implementation of a Feistel Cipher.
    
All functions in this script return an integer
(assuming the functions are called using valid arguments).

Created By - 
Mayur Kr. Garg
"""

def identity(num: int) -> int:
    return num

def add(num: int, key: int) -> int:
    return key + num

def multiply(num: int, key: int) -> int:
    return key * num

def strLength(num: int) -> int:
    return len(str(num))

def power(num: int, key: int) -> int:
    key = abs(key) if num == 0 else key
    return int(pow(num, key))

def reverse(num: int) -> int:
    sign = 1 if num > 0 else -1 
    return int(str(abs(num))[::-1]) * sign

def truncate(num: int, key: int) -> int:
    sign = 1 if num > 0 else -1 
    num = abs(num)
    key = max(1, min(key, len(str(num))))
    return int(str(num)[:key]) * sign

def remainder(num: int, key: int) -> int:
    key = 1 if key == 0 else key
    return num % key

def quotient(num: int, key: int) -> int:
    key = 1 if key == 0 else key
    return num // key

def scaledDistance(num: int, x1: int, x2: int, y1: int, y2: int) -> int:
    return int(num * pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5))