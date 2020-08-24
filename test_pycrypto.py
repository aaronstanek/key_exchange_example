import sys

if sys.version_info.major != 3:
    print("Please use Python version 3")
    exit(0)

try:
    import Crypto
    print("pycrypto is installed")
except:
    print("pycrypto is NOT installed")