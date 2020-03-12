import hilton_Debugger
from hilton_Debugger import print_Debug_String
from hashlib import pbkdf2_hmac
def hmac_Token(passphrase,salt):
    print_Debug_String(f"Generating token: {passphrase},{salt}")
    key = pbkdf2_hmac(
        hash_name = 'sha1', 
        password = str.encode(passphrase),
        salt = str.encode(salt), 
        iterations = 100, 
        dklen = 32
    )
    print_Debug_String(f"Returned token: {key.hex()}")
    return key