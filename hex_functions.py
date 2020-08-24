def hex_numeral_to_hex(n):
    if n >= 10:
        return chr(n+55)
    else:
        return chr(n+48)

def byte_to_hex(n):
    msh = hex_numeral_to_hex(n >> 4)
    lsh = hex_numeral_to_hex(n & 15)
    return msh+lsh

def bytes_to_hex(b):
    output = ""
    for n in b:
        output += byte_to_hex(n)
    return output

def hex_unit_to_numeral(h):
    n = ord(h)
    if n >= 65:
        return n - 55
    else:
        return n - 48

def hex_pair_to_byte(pair):
    msh = hex_unit_to_numeral(pair[0])
    lsh = hex_unit_to_numeral(pair[1])
    return (msh*16) + lsh

def hex_to_bytes(h):
    output = []
    for i in range(0,len(h),2):
        pair = h[i:i+2]
        output.append(hex_pair_to_byte(pair))
    return bytes(output)
