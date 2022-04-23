from hashlib import sha256

cpf = b"111111111"
print(cpf)
cpf = sha256(cpf)
print(cpf.hexdigest())
