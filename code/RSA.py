from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Sign_pkcs1
import base64
from Crypto.Hash import SHA
from time import *

rsa = RSA.generate(1024, Random.new().read)
private_key = rsa.exportKey()
with open("../key/privateKey.pem", "wb") as f:
    f.write(private_key)

public_key = rsa.publickey().exportKey()
with open("../key/publicKey.pem", "wb") as f:
    f.write(public_key)


def rsa_encrypt(plaintext):
    """
    :param plaintext: plaintext to be encrypted
    :return:
    """
    public_key = RSA.importKey(open("../key/publicKey.pem").read())
    cipher = Cipher_pkcs1_v1_5.new(public_key)  # 创建用于执行pkcs1_v1_5加密或解密的密码
    begin = time()
    ciphertext = base64.b64encode(cipher.encrypt(plaintext.encode()))
    end = time()

    rsakey = RSA.importKey(open("../key/privateKey.pem").read())
    cipher = Cipher_pkcs1_v1_5.new(rsakey)      # 创建用于执行pkcs1_v1_5加密或解密的密码
    decrypt_text = cipher.decrypt(base64.b64decode(ciphertext), b"Fail to decrypt")

    with open("../cipher.txt", "a") as f:
        f.write("RSA加密：\n")
        for i in range(len(ciphertext.hex())):
            f.write(ciphertext.hex()[i])
            if i % 100 == 0 and i > 0:
                f.write('\n')
        f.write("\nRSA解密：\n" + decrypt_text.decode() + "\n\n")

    return end - begin


def rsa_signature(plaintext):
    """
    :param plaintext: plaintext to be signed
    :return: NULL
    """
    rsakey = RSA.importKey(open("../key/privateKey.pem").read())
    signer = Sign_pkcs1.new(rsakey)
    digest = SHA.new()
    digest.update(plaintext.encode())
    sign = signer.sign(digest)
    signature = base64.b64encode(sign)

    rsakey = RSA.importKey(open("../key/publicKey.pem").read())
    verifier = Sign_pkcs1.new(rsakey)
    hsmsg = SHA.new()
    hsmsg.update(plaintext.encode())
    is_verify = verifier.verify(hsmsg, base64.b64decode(signature))

    with open("../cipher.txt", "a") as f:
        f.write("RSA加签：\n")
        for i in range(len(signature.hex())):
            f.write(signature.hex()[i])
            if i % 100 == 0 and i > 0:
                f.write('\n')
        f.write("\nRSA解签：\n" + str(is_verify) + "\n\n")

