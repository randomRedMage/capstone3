from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)

with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

f = Fernet(key)

with open('Default_Fin.csv', 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open('enc_Default_fin.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

os.remove('Default_Fin.csv')

