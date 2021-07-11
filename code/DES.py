from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from time import *


def des(plaintext):
    """
    :param plaintext: plaintext to be encrypted
    :return: encryption time
    """
    key = b'a 8b key'  # 秘钥长度为8Byte
    begin = time()
    plaintext_pad = pad(plaintext.encode(), 16, style='pkcs7')
    Des = DES.new(key, DES.MODE_ECB)    # 生成一个DES对象
    end = time()
    ciphertext = Des.encrypt(plaintext_pad)
    Des = DES.new(key, DES.MODE_ECB)
    decrypt_text = Des.decrypt(ciphertext).decode()
    with open("../cipher.txt", "a") as f:
        f.write("DES加密：\n" + ciphertext.hex() + '\n')
        f.write("DES解密：\n" + decrypt_text[:len(plaintext)] + "\n\n")

    return end - begin
