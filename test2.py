
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
import rlotp  # noqa
from rlotp import utils

# print(utils.normalize(5, 5, 10))  # => 5

totp = rlotp.TOTP('base32secret3232', rdigits=(6, 8), interval=5)

print(totp.now()) # => '492039'
print(totp.provisioning_uri(name='jahid@example.com',issuer_name='Madmin', image='https://example.com/image.png'))

# # OTP verified for current time
# totp.verify('492039') # => True
# time.sleep(30)
# totp.verify('492039') # => False
