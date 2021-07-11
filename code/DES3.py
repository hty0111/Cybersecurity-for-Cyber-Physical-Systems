from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
from time import *


def des3(plaintext):
    """
    :param plaintext: plaintext to be encrypted
    :return: encryption time
    """
    key = b'this is a 16 key'       # 秘钥长度为16或24Byte
    begin = time()
    plaintext_pad = pad(plaintext.encode(), 16, style='pkcs7')
    Des3 = DES3.new(key, DES3.MODE_ECB)    # 生成一个DES3对象
    ciphertext = Des3.encrypt(plaintext_pad)
    end = time()
    Des3 = DES3.new(key, DES3.MODE_ECB)
    decrypt_text = Des3.decrypt(ciphertext).decode()
    with open("../cipher.txt", "a") as f:
        f.write("DES3加密：\n" + ciphertext.hex() + '\n')
        f.write("DES3解密：\n" + decrypt_text[:len(plaintext)] + "\n\n")

    return end - begin
