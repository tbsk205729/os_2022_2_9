# password_generator

import string
import secrets

def pw_gen(length):
    pw_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(pw_chars) for x in range(length))
    print(password)
    return

pw_gen(12)

#print(pw_gen(12))