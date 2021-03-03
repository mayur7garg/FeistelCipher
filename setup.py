import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name = "feistelcipher",
    version = "0.1.0",
    description = "Naive implementation of Feistel Cipher using Python",
    long_description = README,
    long_description_content_type = "text/markdown",
    url = "https://github.com/mayur7garg/FeistelCipher",
    author = "Mayur Kr. Garg",
    author_email = "mayur7garg@gmail.com",
    license = "MIT",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages = ["feistelcipher"]
)