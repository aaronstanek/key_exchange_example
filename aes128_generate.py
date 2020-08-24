import version_lock

import random

key = []

while len(key) < 16:
    key.append(random.randint(0,255))

from hex_functions import bytes_to_hex

key_string = bytes_to_hex(bytes(key))

with open("aes128_key.txt","w") as file:
    file.write(key_string)

print("Key written to file")