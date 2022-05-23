import os
# coding=UTF-8 
#----------------------INICIO DO PROGAMA---------------------------#
# Armazenamento da indentificacao pessoal e metodo para mostrar no console

nome = "Anderson dos santos Reinaldo"
ru   = "3930112"

def showIndentificacaoPessoal():
    global nome,ru
    print("\nBem vindo a Loja do {}!\nRU:{}\n".format(nome,ru))
    
showIndentificacaoPessoal()

# Calcula o desconto a ser aplicado no produto
def aplicarDesconto(valorProduto, qtdeProduto):
    
    valorSemDesconto = valorProduto * qtdeProduto
    valorComDesconto = valorProduto * qtdeProduto
    desconto = 0
    
    if (qtdeProduto > 0 and qtdeProduto <= 9):
        valorComDesconto =  valorSemDesconto - valorComDesconto * 0
        desconto = 0
    elif (qtdeProduto >= 10  and qtdeProduto <= 99):
        valorComDesconto = valorSemDesconto - valorComDesconto * 0.5
        desconto = 5
    elif (qtdeProduto >= 100  and qtdeProduto <= 999):
        valorComDesconto = valorSemDesconto - valorComDesconto * 0.10
        desconto = 10
    else:
        valorComDesconto = valorSemDesconto - valorComDesconto * 0.15
        desconto = 15
    
    # Mostra o resultado final no console junto com o identificador
    print("\nO valor sem desconto foi: R${} \nO Valor com desconto foi: R${:.2f} (desconto {}%)".format(valorSemDesconto, valorComDesconto, desconto))
    showIndentificacaoPessoal()
    
def validaInput(value):
# Valida a entrada de valores
    if(value.isdigit() == False):
        os.system('clear') or None
        showIndentificacaoPessoal()
        print('O valor digitado nao e inteiro!\n')
        return False
    elif(int(value) < 0 or int(value) == 0):
        showIndentificacaoPessoal()
        print("O valornao pode ser menor ou igual a zero(0)\n")
        return False

#Inicial o processo para calculo dos produtos
while True: 
    valorProduto = input("Entre com o valor do produto: ")
    
    #Valida o retorno dos inputs 
    if(validaInput(valorProduto) == False):
        continue
    qtdeProduto = input("Entre com a quantidade do produto: ")
    if(validaInput(qtdeProduto) == False):
        continue
    valorProduto = int(valorProduto)
    qtdeProduto = int(qtdeProduto)
    
    # Chama a funcao para calcular o desconto e aplicar o resultado na tela
    aplicarDesconto(valorProduto,qtdeProduto)
    break
    