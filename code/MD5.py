import hashlib
from time import *


def md5(plaintext):
    """
    :param plaintext: plaintext to be encrypted
    :return: encryption time
    """
    begin = time()
    ciphertext = hashlib.md5(plaintext.encode())
    end = time()
    with open("../cipher.txt", "a") as f:
        f.write("MD5加密：\n" + ciphertext.hexdigest() + '\n\n')       # len = 128/4

    return end - begin
