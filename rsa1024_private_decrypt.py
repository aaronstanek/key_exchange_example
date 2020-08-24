import version_lock

with open("rsa1024_private_key.txt","r") as file:
    private_string = file.read()

with open("ciphertext_in.txt","r") as file:
    ciphertext_string = file.read()

from Crypto.PublicKey import RSA

private_key = RSA.importKey(private_string)

from hex_functions import hex_to_bytes

ciphertext = hex_to_bytes(ciphertext_string)

plaintext = private_key.decrypt(ciphertext)

with open("plaintext_out.txt","wb") as file:
    file.write(plaintext)

print("Decrypted ciphertext_in.txt using rsa1024_private_key.txt")
print("Wrote result to plaintext_out.txt")