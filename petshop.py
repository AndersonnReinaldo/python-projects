# coding=UTF-8 
#----------------------INICIO DO PROGAMA---------------------------#
# Armazenamento da indentificacao pessoal e metodo para mostrar no console
nome = "Anderson dos santos Reinaldo"
ru   = "3930112"

def showIndentificacaoPessoal():
    global nome,ru
    print("\nProgama de Agendamento de Banho do {} !\nRU:{}\n".format(nome,ru))
    
showIndentificacaoPessoal()

#Definicao inicial dos tipos de pelos e seus respectivos valores 
tiposPelo = {
 "C" : {"label":"Curto", "value":20.00},
 "M" : {"label": "Medio", "value": 27.50},
 "L" : {"label": "Longo", "value": 35.00},
}

# Pedidos de banho realizado pelo cliente
totalValorPedido = 0
countPedidos = 0
welcomeSelectText = ""

# Monta a tabela de apresentacao de tipos de pelos
for pelo in tiposPelo:
     currentPelo = tiposPelo[pelo.upper()]
     welcomeSelectText += " \n %s - %s \n" % ( pelo,currentPelo['label'])
     
welcomeSelectText += "\nDigite X para sair!\n"
      
                 
#Funcao responsavel por calcular o valor do banho
def calculaValorBanho(tipoPeloSelecionado):
    # Define a variavel no escopo da funcao
    global countPedidos, totalValorPedido
    
    # Busca o valor do banho de acordo com o codigo digitado pelo cliente 
    valorDoPelo = tiposPelo[tipoPeloSelecionado.upper()]["value"]
    subtotal = valorDoPelo
    
    # Solicita o peso do animal 
    pesoAnimal = input("\nEntre com o PESO do seu cachorro! \n\n >>> ")

    # Valida se o peso digitado e valido  e nao e uma string
    if(pesoAnimal.isdigit() == False):
        print('O valor digitado nao e inteiro!')
        calculaValorBanho(tipoPeloSelecionado)
        return
    elif(float(pesoAnimal) < 0 or float(pesoAnimal) == 0 ):
        print('Digite um peso valido maior de que zero(0)!')
        calculaValorBanho(tipoPeloSelecionado)
        return
    else: 
        pesoAnimal = float(pesoAnimal)
        
        # Calcula o valor total de acordo com pelo e com o peso do animal 
        if 0 <= pesoAnimal < 5:
            subtotal *= 1.7
        elif 5 <= pesoAnimal < 12:
            subtotal *= 2.0
        elif 12 <= pesoAnimal < 22:
            subtotal *= 2.4
        elif 22 <= pesoAnimal < 35:
            subtotal *= 2.9
        elif 35 <= pesoAnimal < 50:
            subtotal *= 3.5
        else:
            subtotal *= 4.2

    # Solicita o nome do animal
    nomeAnimal = input("\nQual o nome do seu cachorro! \n\n >>> ")
    
    # Monta o texto de saida ao finalizar o valor do banho de um cachorro
    resText = "\nO Banho do {} ficou R$ {}\n".format(nomeAnimal,subtotal) 
    print(resText)
    
    # Adiciona o valor do animal anterior ao valor total dos pedidos de banho
    totalValorPedido += float(subtotal)
    # Incrementa um indice no contador
    countPedidos += 1
    return 
    
# Ciclo de vida para iniciar o atendimento ao cliente
while True:
    
    # Verifica se o cliente deseja realizar mais algum pedido
    if(countPedidos > 0):
        confirmNextPedido = str(input("Deseja inserir mais algum pedido de banho ? [S/N]: ")).upper()
        if confirmNextPedido == 'N':
            desconto = (totalValorPedido * 0.1) * (countPedidos - 1)
            totalValorPedido = totalValorPedido - desconto
            print("\nO Valor total do(s) {} animais(s) ficou:\n R$ {} (desconto de R${})\n".format(countPedidos,totalValorPedido,round(desconto, 2)))
            showIndentificacaoPessoal()
            break
        elif confirmNextPedido not in ("SN"):
            print("\nCodigo invalido, Digite S para Sim ou N para finalizar o atendimento!")
            continue
        
    # A entrada a baixo e responsavel por pegar o codigo do banho 
    codPeloSelect = str(input("Qual o tipo de pelo do seu cachorro ?:\n %s \n >>> " % (welcomeSelectText))).upper()
    
    
    # Valida se a entrada teve o valor de x, se sim encerra o progama
    if codPeloSelect == 'X':
        print("\nAtendimento encerrado!")
        showIndentificacaoPessoal()
        break
    # Verifica se o codigo e valido
    elif codPeloSelect not in (tiposPelo.keys()):
        print("\nOpção inválida\n")
        continue
        
    calculaValorBanho(codPeloSelect)





















