
import os, string
import sys, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
import rlotp  # noqa
from rlotp import utils

# print(utils.normalize(5, 5, 10))  # => 5

totp = rlotp.TOTP('base32secret3232', rdigits=(6, 10), period=5, digest=hashlib.sha256, chargroup='alpha')

print(totp.now()) # => '492039'
print(totp.provisioning_uri(name='jahid@example.com',issuer_name='Madmin', image='https://example.com/image.png'))


hotp = rlotp.HOTP('base32secret3232', rdigits=(6, 10), digest=hashlib.sha256, chargroup='alpha')

print(hotp.at(3)) # => '492039'
print(hotp.provisioning_uri(name='jahid@example.com',issuer_name='Madmin', image='https://example.com/image.png'))

# # OTP verified for current time
# totp.verify('492039') # => True
# time.sleep(30)
# totp.verify('492039') # => False


# print(pick_chars('492039', string.digits + string.ascii_uppercase)) # => '4J2A0I'
