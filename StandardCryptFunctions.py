"""StandardCryptFunctions

This script contains some standard functions which can be used in the
implementation of a Feistel Cipher.

All functions in this script accept two arguments -

    key : int 
        This value acts as an encoding key for the function.
        It must be a non-negative integer.
        Not all functions may utilise this argument but it must always
        be provided to keep the function signatures consistent.

    num : int
        This value acts as the value on which the function acts.
        It must be a non-negative integer.

All functions in this script return a non-negative integer
(assuming the functions are called using valid arguments).

This script also contains a list containing references to all the
functions in this script which can be used to randomly add a function
block to the Feistel Cipher.

Created By - 
Mayur Kr. Garg
"""


def identity(key: int, num: int) -> int:
    return num


def add(key: int, num: int) -> int:
    return key + num


def multiply(key: int, num: int) -> int:
    return key*num


def addThenMultiply(key: int, num: int) -> int:
    return (num+key)*key


def strLength(key: int, num: int) -> int:
    return len(str(num))


def power(key: int, num: int) -> int:
    return pow(num, key)


def reverse(key: int, num: int) -> int:
    return int(str(num)[::-1])


def truncate(key: int, num: int) -> int:
    if key <= 0:
        key = 1
    return int(str(num)[:key])


def remainder(key: int, num: int) -> int:
    if key <= 0:
        key = 1
    return num % key


def quotient(key: int, num: int) -> int:
    if key <= 0:
        key = 1
    return num//key


ALL_FUNCTIONS = [identity, add, multiply, addThenMultiply,
                 strLength, power, reverse, truncate, remainder, quotient]
