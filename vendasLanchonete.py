
# coding=UTF-8 
#----------------------INICIO DO PROGAMA---------------------------#
# Armazenamento da indentificacao pessoal e metodo para mostrar no console
nome = "Anderson dos santos Reinaldo"
ru   = "3930112"

def showIndentificacaoPessoal():
    global nome,ru
    print("\nBem vindo ao lanchonete do {} !\nRU:{}\n".format(nome,ru))
    
showIndentificacaoPessoal()

#Definicao inicial dos tipos de lanches e seus respectivos valores 
lanches = {
 "100" : {"label":"Cachorro-Quente", "value":9.00},
 "101" : {"label": "Cachorro-Quente Duplo", "value": 11.00},
 "102" : {"label": "X-Egg", "value": 12.00},
 "103" : {"label": "X-Salada", "value": 13.00},
 "104" : {"label": "X-Bacon", "value": 14.00},
 "105" : {"label": "X-Tudo", "value": 17.00},
 "200" : {"label": "Refrigerante Lata", "value": 5.00},
 "201" : {"label": "Chá Gelado", "value": 4.00},
}

# Pedidos de banho realizado pelo cliente
totalValorPedido = 0
countPedidos = 0
erroCode = False

# Monta a tabela de apresentacao de tipos de lanches
def criarTabela():
    print(12*"*" + " CARDAPIO DO DIA "+ 12*"*")
    print ("|{:<8}|\t{:<15}\t| {:<5} |".format('Codigo','Descricao','Valor'))

    for lanche in lanches:
        print ("|{:<8}|{:<15}\t| {:<5} |".format( lanche,lanches[lanche]["label"],lanches[lanche]["value"]))
        
    print("\nDigite X para sair!\n")     
               
#Funcao responsavel por calcular o valor do lanche
def calculaValorLanche(tipoPeloSelecionado):
    # Define a variavel no escopo da funcao
    global countPedidos, totalValorPedido
    
    # Busca o valor do lanche de acordo com o codigo digitado pelo cliente 
    valorDoLanche = lanches[tipoPeloSelecionado.upper()]["value"]
        
    # Monta o texto de saida ao finalizar o valor do lanche
    resText = "\nVoce pediu um  {} no valor de  R${:.2f} Reais\n".format(lanches[tipoPeloSelecionado.upper()]["label"],valorDoLanche) 
    print(resText)
    
    # Adiciona o valor do lanche anterior ao valor total dos pedidos de lanche
    totalValorPedido += float(valorDoLanche)
    # Incrementa um indice no contador
    countPedidos += 1
    return 
    
# Ciclo de vida para iniciar o atendimento ao cliente
while True:
    
    # Verifica se o cliente deseja realizar mais algum pedido
    if(countPedidos > 0 and erroCode == False):
        confirmNextPedido = str(input("Deseja pedir mais alguma coisa? \n 1 - SIM \n 2 - NAO\n>>> ")).upper()
        if confirmNextPedido == '2':
            totalValorPedido = totalValorPedido 
            print("\nO Valor total do(s) {} lanche(s) ficou: R${:.2f} Reais\n".format(countPedidos,totalValorPedido))
            showIndentificacaoPessoal()
            break
        elif confirmNextPedido not in ("12"):
            print("\nCodigo invalido, Digite 1 para Sim ou 2 para finalizar o atendimento!")
            continue
        
    # A entrada a baixo e responsavel por pegar o codigo do lanche
    if(countPedidos == 0): 
        criarTabela();
    codPeloSelect = str(input("\nEntre com o codigo desejado:\n >>> ")).upper()
    
    
    # Valida se a entrada teve o valor de x, se sim encerra o progama
    if codPeloSelect == 'X':
        print("\nAtendimento encerrado!")
        showIndentificacaoPessoal()
        break
    # Verifica se o codigo e valido
    elif codPeloSelect not in (lanches.keys()):
        print("\nOpção inválida\n")
        erroCode = True
        continue
    
    # Reseta os erros de codigo do lanche
    erroCode = False
     
    calculaValorLanche(codPeloSelect)





















