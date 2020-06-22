import crypto
import sys
sys.modules['Crypto'] = crypto
import Crypto.Random
from Crypto.Cipher import AES
import hashlib
import binascii


# salt size in bytes
SALT_SIZE = 16

# number of iterations in the key generation
NUMBER_OF_ITERATIONS = 20

# the size multiple required for AES
AES_MULTIPLE = 16
# # From https://github.com/mitsuhiko/python-pbkdf2
# from pbkdf2 import pbkdf2_bin

def make_hash(device, salt, iterations):
    assert iterations > 0

    if device:
        passcord = device.device_type + device.os + device.version

    key = passcord + salt
    key = key.encode('utf-8')
    for i in range(iterations):
        key = hashlib.sha256(key).digest()  

    return key
# # Parameters to PBKDF2. Only affect new passwords.

# KEY_LENGTH = 24
# HASH_FUNCTION = 'sha256'  # Must be in hashlib.
# # Linear to the hashing time. Adjust to be high but take a reasonable
# # amount of time on your server. Measure with:
# # python -m timeit -s 'import passwords as p' 'p.make_hash("something")'
# COST_FACTOR = 10000

# def make_hash(salt, device):
#     """Generate a random salt and return a new hash for the password."""
#     if isinstance(password, unicode):
#         password = password.encode('utf-8')
#     salt = b64encode(salt)
#     return 'PBKDF2${}${}${}${}'.format(
#         HASH_FUNCTION,
#         COST_FACTOR,
#         salt,
#         b64encode(pbkdf2_bin(password, salt, COST_FACTOR, KEY_LENGTH,
#                              getattr(hashlib, HASH_FUNCTION))))

