from Crypto.Cipher import AES
from Crypto import Random
from time import *


def aes(plaintext):
    """
    :param plaintext: plaintext to be encrypted
    :return: encryption time
    """
    key = b'this is a 16 key'   # 密钥长度为16或24或32Byte
    begin = time()
    iv = Random.new().read(AES.block_size)      # 生成长度等于AES块大小的不可重复的密钥向量
    aes_ecp = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = iv + aes_ecp.encrypt(plaintext.encode())
    end = time()
    aes_dcp = AES.new(key, AES.MODE_CFB, iv)
    decrypt_text = aes_dcp.decrypt(ciphertext[16:]).decode()
    with open("../cipher.txt", "a") as f:
        f.write("AES加密：\n" + ciphertext.hex() + '\n')
        f.write("AES解密：\n" + decrypt_text + "\n\n")

    return end - begin
