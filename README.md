# Feistel Cipher
The Feistel Cipher package can be used to implement a Feistel Cipher using either inbuilt or custom functions for encyrpting and decrypting integers.

*Current Version: 0.2.0*

*Requires: Python 3.5+*

## Inspiration
The creation of the package is both inspired by and based on the explanation given **Dr. Mike Pound** on the **[Computerphile](https://www.youtube.com/user/Computerphile)** YouTube channel in the video titled **[Feistel Cipher - Computerphile](https://youtu.be/FGhj3CGxl8I)**.

## Installation

You can install the **Feistel Cipher** package from **[PyPI](https://pypi.org/project/feistelcipher/)**

    pip install feistelcipher

## Usage

### Import the necessary classes
```python
import feistelcipher.FeistelCipher as fc
import feistelcipher.CryptFunctions as cfs
import feistelcipher.StandardCryptFunctions as scf
```

### Create a `CryptFunctions` object
```python
funcList = cfs.CryptFunctions()
```
### Add functions and associated keys to the `CryptFunctions` object
```python
funcList.addFunc(scf.strLength)
funcList.addFunc(scf.quotient, [7])
funcList.addFunc(scf.power, [3])
funcList.addFunc(scf.truncate, [5])
funcList.addFunc(scf.scaledDistance, [1, 2, 3, 4])
```

### Create a `FeistelCipher` object using the `CryptFunctions` object
```python
cipher = fc.FeistelCipher(funcList)
```

### Encryption
```python
enc = cipher.encrypt(1_234_567)
print(repr(enc))
```
##### Output

    >>> EncryptedObject(437201434, 43067, 4)

### Decryption
```python
dec = cipher.decrypt(enc)
print(dec)
```

##### Output

    >>> 1234567

## Advanced Usage and Explanation
For detailed explanation and usage of this package with custom functions, kindly refer to [Examples.ipynb](https://github.com/mayur7garg/FeistelCipher/blob/main/Examples.ipynb) in the [GitHub repo](https://github.com/mayur7garg/FeistelCipher).

## Upcoming improvements
- Support for Keyword arguments
- Encrypting/Decrypting iterables of integers
- Support for easily saving the `FeistelCipher` object to a pickled or binary file
- Improved Documentation

## Thank You
If you liked this package or found it useful, consider starring the associated GitHub repository.

> Created by - *Mayur Kr. Garg*