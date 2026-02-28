import pyotp
import hashlib
import base64


BASE_SECRET = "XPHL7MH3AGI7AS722UOT3TKIKT2FMKM5"
INTERVAL = 60


def normal_totp(secret):
    totp = pyotp.TOTP(secret, digits=4, interval=INTERVAL)
    return totp.now()


def context_totp(secret, context):
    # Create SHA256 hash
    raw_hash = hashlib.sha256(
        (secret + context).encode()
    ).digest()

    # Convert to Base32 (required by pyotp)
    derived_secret = base64.b32encode(raw_hash).decode()

    totp = pyotp.TOTP(derived_secret, digits=4, interval=INTERVAL)
    return totp.now()


if __name__ == "__main__":
    print("Base Secret:", BASE_SECRET)
    print("-" * 50)

    print("NORMAL TOTP (same secret)")
    otp1 = normal_totp(BASE_SECRET)
    otp2 = normal_totp(BASE_SECRET)

    print("Registration OTP:", otp1)
    print("Login OTP       :", otp2)
    print("Same?           :", otp1 == otp2)