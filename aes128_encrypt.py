import version_lock

with open("aes128_key.txt","r") as file:
    key_string = file.read()

with open("plaintext_in.txt","rb") as file:
    plaintext = file.read()

from hex_functions import hex_to_bytes

key = hex_to_bytes(key_string)

from Crypto.Cipher import AES

cipher = AES.new(key, AES.MODE_ECB)

# add padding
if len(plaintext) % 16 != 0:
    diff = 16 - (len(plaintext) % 16)
    plaintext += bytes([0]*diff)

ciphertext = cipher.encrypt(plaintext)

from hex_functions import bytes_to_hex

ciphertext_string = bytes_to_hex(ciphertext)

with open("ciphertext_out.txt","w") as file:
    file.write(ciphertext_string)

print("Encrypted plaintext_in.txt using aes128_key.txt")
print("Wrote result to ciphertext_out.txt")