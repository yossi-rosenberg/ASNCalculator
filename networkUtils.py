import socket, struct

def mask_to_int(ip_address):
    packedIP = socket.inet_aton(ip_address)
    return struct.unpack("!L", packedIP)[0]