import version_lock

try:
    import Crypto
    print("pycrypto is installed")
except:
    print("pycrypto is NOT installed")