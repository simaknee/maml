#!/usr/bin/env python
# coding: utf-8

# In[6]:


from Crypto import Random
from Crypto.Cipher import AES
import scipy

BLOCK_SIZE=16

class AESCryptoCBC():
    def __init__(self, key):
        #Initial vector를 0으로 초기화하여 16바이트 할당함
        iv = chr(0) * 16
        # aes cbc 생성
        self.crypto = AES.new(key, AES.MODE_CBC, iv)

    def encrypt(self, data):
        #암호화 message는 16의 배수여야 한다.
        enc = self.crypto.encrypt(data)
        return enc

    def decrypt(self, enc):
        #복호화 enc는 16의 배수여야 한다.
        dec = self.crypto.decrypt(enc)
        return dec


# In[5]:


#키 32바이트 = aes 256
#key = [0x10, 0x01, 0x15, 0x1B, 0xA1, 0x11, 0x57, 0x72, 0x6C, 0x21, 0x56, 0x57, 0x62, 0x16, 0x05, 0x3D,
#        0xFF, 0xFE, 0x11, 0x1B, 0x21, 0x31, 0x57, 0x72, 0x6B, 0x21, 0xA6, 0xA7, 0x6E, 0xE6, 0xE5, 0x3F]
key = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
       0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
plaintext0 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
plaintext1 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01]

#키 생성
aes = AESCryptoCBC(bytes(key))
#변경
enc0 = aes.encrypt(bytes(plaintext0))
enc1 = aes.encrypt(bytes(plaintext1))
print("The encrypted value is " + str(list(enc0)))
print("The encrypted value is " + str(list(enc1)))

#키 생성
#aes2 = AESCryptoCBC(bytes(key))
#변경
#dec = aes2.decrypt(bytes(enc))
#print("The decrypted value is " + str(list(dec)))


# In[9]:


def hamming_distance(string1, string2): 
    # Start with a distance of zero, and count up
    distance = 0
    # Loop over the indices of the string
    L = len(string1)
    for i in range(L):
        # Add 1 to the distance if these two characters are not equal
        if string1[i] != string2[i]:
            distance += 1
    # Return the final count of differences
    return distance


# In[10]:


hamming_distance(enc0,enc1)


# In[11]:


version


# In[12]:


--version

