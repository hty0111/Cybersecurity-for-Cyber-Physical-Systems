import hashlib
from time import *


def sha1(plaintext):
    """
    :param plaintext: plaintext to be encrypted
    :return: encryption time
    """
    begin = time()
    ciphertext = hashlib.sha1(plaintext.encode())
    end = time()
    with open("../cipher.txt", "a") as f:
        f.write("SHA1加密：\n" + ciphertext.hexdigest() + '\n\n')     # len = 160/4

    return end - begin
