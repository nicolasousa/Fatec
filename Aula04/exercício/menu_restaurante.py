with open("estoque.csv", "r") as file:
    dados_do_banco = file.read() # pegando os dados em formato de 
    dados_do_estoque = dados_do_banco.split("\n") #quebrando em linhas
    menu = dados_do_estoque[0]
    quantidade_no_estoque = dados_do_estoque[1]
    print(menu)
 
#abrindo um banco
#with open("estoque.csv", "a") as file:
#    pass

