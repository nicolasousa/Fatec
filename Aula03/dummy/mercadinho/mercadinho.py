# author: nicolas alves
# version: 1.0.1
# date: abr/09/22
# description: este programa cadastra usuários
# name: mercadinho fatec

from hashlib import sha256
import sys
from time import sleep

# mensagem e boas-vindas
mensagem = "Olá seja bem-vindo ao mercadinho Fatec"

# imprimindo as opções do menu
for letra in mensagem:
    sys.stdout.write(letra)
    sys.stdout.flush()
    sleep(0.1)
print()

# setando as opções do menu
opcoes_de_menu = ["sign-in", "sign-up", "deletar usuário", "esqueci a senha"]

# imprimindo menu de ações
count = 1
for opcao in opcoes_de_menu:
    print(f"[{count}] - [{opcao}]")
    count += 1                    # count = count + 1
    
opcao_digitada = input("Qual a opcção desejada?")

with open("../mercadinho/dbmercadinho.csv") as arquivo:
    print(arquivo.read())
  
