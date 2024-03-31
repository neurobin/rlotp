
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
import rlotp  # noqa


totp = rlotp.TOTP('base32secret3232')

print(totp.now()) # => '492039'

# # OTP verified for current time
# totp.verify('492039') # => True
# time.sleep(30)
# totp.verify('492039') # => False
