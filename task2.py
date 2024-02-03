import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import re
from bcrypt import *
from nltk.corpus import words




#takes in a word from the dictionary
#hashes it with 29 character (user + worktime + salt) 
#need to check if the hash generated is same as the one in the string (portion after the 22 char salt)
# print(hashpw(b"registration", b"$2b$08$J9FW66ZdPI2nrIMcOxFYI.")) 
#n input a word as the first parameter and the entire hash (both as bytes) to verify if the hash resulted from the given plaintext word. 
# print(checkpw (b"registrationsucks",b'$2b$08$J9FW66ZdPI2nrIMcOxFYI.zKGJsUXmWLAYWsNmIANUy5JbSjfyLFu'))


sample = "Bilbo:$2b$08$J9FW66ZdPI2nrIMcOxFYI.qx268uZn.ajhymLP/YHaAsfBGP3Fnmq"

result = "$2b$08$J9FW66ZdPI2nrIMcOxFYI.qx268uZn.ajhymLP/YHaAsfBGP3Fnmq"

word_list = words.words()

salt = b"$2b$08$J9FW66ZdPI2nrIMcOxFYI."

# 6 - 10 letter word list

filtered_list = [word.lower() for word in word_list if 6 <= len(word) <= 10]

for i in range (len(filtered_list)):
    word_bytes = filtered_list[i].encode('utf-8') #converting every word into bytes
    hash = hashpw(word_bytes, salt )
    if hash == result.encode('utf-8'):
        print("Hash found")
        print(filtered_list[i])
    

