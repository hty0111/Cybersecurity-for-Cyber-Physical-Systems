import pdfplumber
from MD5 import md5
from SHA1 import sha1
from HMAC import mac
from DES import des
from DES3 import des3
from AES import aes
from RSA import *
import numpy as np
import matplotlib.pyplot as plt
import rsa


# =======================================
# V1.0
# 加密解密普通明文
# 运算结果存入"../cipher.txt" & "../key/"
# =======================================

# 读取明文
with pdfplumber.open("../PPT展示题目.pdf") as pdf:
    plaintext = pdf.pages[0].extract_text()

with open('../cipher.txt', 'w') as f:
    f.write("********明文********\n\n" + plaintext + '\n\n\n')
    f.write("********单向加密（线性散列加密）********\n\n")

md5(plaintext)
sha1(plaintext)
mac(plaintext)

with open('../cipher.txt', 'a') as f:
    f.write("\n********双向加密(对称加密)********\n\n")

# 取前十个字符进行加密解密
des(plaintext[:10])
des3(plaintext[:10])
aes(plaintext[:10])

with open('../cipher.txt', 'a') as f:
    f.write("\n********双向加密(非对称加密)********\n\n")

rsa_encrypt(plaintext[:10])
rsa_signature(plaintext[:10])


# =======================================
# V2.0
# 对各类加密算法的效率进行对比
# =======================================

# 生成1MB量级的随机数据
text = ''
for i in np.arange(1e6):
    text += str(np.random.randint(0, 9))


# 可视化
encrypt_time = [md5(text), sha1(text), mac(text), des(text), des3(text), aes(text)]
algorithm = ["MD5", "SHA1", "HMAC", "DES", "3DES", "AES"]
plt.figure("Efficiency", figsize=(10, 6), dpi=150)
plt.subplot(131)
plt.title("Comparison of digest algorithm")
plt.bar(algorithm[:3], encrypt_time[:3])
plt.xticks(rotation=45)
plt.ylabel("time consuming")
plt.xlabel("algorithms")
plt.subplot(133)
plt.title("Comparison of symmetric encryption")
plt.bar(algorithm[3:], encrypt_time[3:])
plt.xticks(rotation=45)
plt.ylabel("time consuming")
plt.xlabel("algorithms")
plt.subplot(132)
plt.title("On the whole")
plt.bar(algorithm, encrypt_time)
plt.xticks(rotation=45)
plt.ylabel("time consuming")
plt.xlabel("algorithms")
plt.subplots_adjust(wspace=1)
plt.savefig('../efficiency.png')
plt.show()
