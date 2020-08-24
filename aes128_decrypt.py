import version_lock

with open("aes128_key.txt","r") as file:
    key_string = file.read()

with open("ciphertext_in.txt","r") as file:
   ciphertext_string = file.read()

from hex_functions import hex_to_bytes

key = hex_to_bytes(key_string)

from Crypto.Cipher import AES

cipher = AES.new(key, AES.MODE_ECB)

ciphertext = hex_to_bytes(ciphertext_string)

plaintext = cipher.decrypt(ciphertext)

# remove padding
padding = 0
while plaintext[-1-padding] == 0:
    padding += 1
plaintext = plaintext[:-padding]

with open("plaintext_out.txt","wb") as file:
    file.write(plaintext)

print("Decrypted ciphertext_in.txt using aes128_key.txt")
print("Wrote result to plaintext_out.txt")