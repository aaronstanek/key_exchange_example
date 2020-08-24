import sys

if sys.version_info.major != 3:
    print("Please use Python version 3")
    exit(0)

from Crypto.PublicKey import RSA

private_key = RSA.generate(1024)
private_string = private_key.exportKey().decode("UTF-8")

print("")
print(private_string)

public_key = private_key.publickey()
public_string = public_key.exportKey().decode("UTF-8")

print("")
print(public_string)

with open("rsa1024_private_key.txt","w") as file:
    file.write(private_string)

with open("rsa1024_public_key.txt","w") as file:
    file.write(public_string)

print("")
print("Keys written to files")
