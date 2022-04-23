from hashlib import sha256

usuario_padrao = "35298781dc6efb3dbe57241319cda4e5e1ea4236e0692bc1fa26f9ddd9b359ac"
senha_padrao = "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"

usuario_digitado = input("Digite seu usuário: ").encode("ascii")
senha_digitada = input("Digite sua senha: ").encode("ascii")
usuario_digitado = sha256(usuario_digitado).hexdigest()
senha_digitada = sha256(senha_digitada).hexdigest()

if senha_digitada == senha_padrao and usuario_digitado == usuario_padrao:
    print("Bem vindo ao curso Fatec")
else:
    print("Senha ou Usuário incorreto(s)")