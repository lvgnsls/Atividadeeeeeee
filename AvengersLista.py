#"MA1A Atividade" - Lívia Rodrigues Gonsales

#FunçãoProdutoValor01

prod = str(input('Insira o produto desejado: '))
preco = [4.00, 4.50, 5.00, 6.00, 0.50]
def prodValor():

    if prod == 'Salgado':
         return Preco == 4.0
    elif prod == 'Refrigerante':
         return Preco == 4.5
    elif prod == 'Suco':
         return Preco == 5.0
    elif prod == 'Sorvete':
         return Preco == 6.0
    elif prod == 'Café':
         return Preco == 4.0
    elif prod == 'Capuccino':
         return Preco == 6.0
    elif prod == 'Bolo':
         return Preco == 4.5
    elif prod == 'Dadinho':
         return Preco == 0.5
    else:
         print('Desculpe, não temos esse produto')
print(prodValor(Preco))


#FilaCantina02

clientes = []
prod = []

def clienteProd():
    for i in range(7):
        nome = input('Forneça seu nome: ')
        produto = input('Insira o produto desejado: ')
        clientes.append(nome)
        prod.append(produto)

#PessoaPedidoPreço03

prodValor()
clienteProd()

print('Clientes --- Produto --- Preço')
n = 0
valor = []
while n<=7:
    print(clientes[n],'---', prod[n], '---', preco)
    n = n+1

            






























                

