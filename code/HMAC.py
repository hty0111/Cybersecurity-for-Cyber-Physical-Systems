import hmac
import hashlib
from time import *


def mac(plaintext):
    """
    :param plaintext: plaintext to be encrypted
    :return: encryption time
    """
    key = b'a 8b key'
    begin = time()
    ciphertext = hmac.new(key, plaintext.encode(), hashlib.md5).hexdigest()
    end = time()
    with open("../cipher.txt", "a") as f:
        f.write("HMAC加密：\n" + ciphertext + '\n\n')

    return end - begin
