import version_lock

with open("rsa1024_public_key.txt","r") as file:
    public_string = file.read()

with open("plaintext_in.txt","rb") as file:
    plaintext = file.read()

from Crypto.PublicKey import RSA

public_key = RSA.importKey(public_string)

ciphertext = public_key.encrypt(plaintext,0)

from hex_functions import bytes_to_hex

ciphertext_string = bytes_to_hex(ciphertext[0])

with open("ciphertext_out.txt","w") as file:
    file.write(ciphertext_string)

print("Encrypted plaintext_in.txt using rsa1024_public_key.txt")
print("Wrote result to ciphertext_out.txt")