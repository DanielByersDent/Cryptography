import hashlib
import base64


iterations = 45454
salt_alice = "128".encode()
password_alice = "type password here".encode()
value_alice = base64.b64encode(hashlib.pbkdf2_hmac("sha512", password_alice, salt_alice, iterations, dklen=256))
print(value_alice, salt_alice, iterations)

salt_bob = "777".encode()
password_bob = "type password here".encode()
value_bob = base64.b64encode(hashlib.pbkdf2_hmac("sha512", password_bob, salt_bob, iterations, dklen=256))
print(value_bob, salt_bob, iterations)