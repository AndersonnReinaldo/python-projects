# coding=UTF-8 
#----------------------INICIO DO PROGAMA---------------------------#
# Armazenamento da indentificacao pessoal e metodo para mostrar no console

nome = "Anderson dos santos Reinaldo"
ru   = "3930112"

def showIndentificacaoPessoal():
    global nome,ru
    print("\nBem vindo a companhia de logistica do {}!\nRU:{}\n".format(nome,ru))
    
showIndentificacaoPessoal()

#Definicao inicial das rotas 
rotas = {
 "RS" : {"label":"De Rio de Janeiro até São Paulo", "value":1},
 "SR" : {"label": "De São Paulo até Rio de Janeiro", "value": 1},
 "BS" : {"label": "De Brasília até São Paulo", "value": 1.2},
 "SB" : {"label": "De São Paulo até Brasília", "value": 1.2},
 "BR" : {"label": "De Brasília até Rio de Janeiro", "value": 1.5},
 "RB" : {"label": "Rio de Janeiro até Brasília", "value": 1.5},
}

# Variaveis de controle
valorTotal = 0

# Monta a tabela de apresentacao de rotas
def criarTabelaDeRotas():
    print(14*"*" + " ROTAS "+ 17*"*")
    for rota in rotas:
        print (" {} - {}".format( rota,rotas[rota]["label"]))
        
    print(38*"*")
    print("\nDigite X para sair!\n")     

# Calcula as dimensoes do objeto de acordo com a entrada e o valor definido pelo volume calculado
def dimensoesObjeto():
    global valorTotal
    
    passo = 0
    
    alturaDoObjeto = 0
    comprimentoDoObjeto = 0
    larguraDoObjeto = 0
    volumeDoObjeto = 0
    
    while True:
        if(passo == 0):
            try:
                alturaDoObjeto = int(input("Digite a altura do objeto (em cm): "))
                if(alturaDoObjeto == 0 or alturaDoObjeto < 0):
                    passo = 0
                    print("O valor nao pode ser igual ou menor zero!")
                    print("Entre com o as dimensoes desejadas novamente\n")
                    continue
                passo += 1
            except ValueError: 
                print("Voce digitou uma dimensao com valor nao numerico")
                print("Entre com o as dimensoes desejadas novamente\n")
        elif(passo == 1):
              try:
                comprimentoDoObjeto = int(input("\nDigite o comprimento do objeto (em cm): "))
                if(comprimentoDoObjeto == 0 or comprimentoDoObjeto < 0):
                    passo = 1
                    print("O valor nao pode ser igual ou menor zero!")
                    print("Entre com o as dimensoes desejadas novamente\n")
                    continue
                passo += 1
              except ValueError:
                print("Voce digitou uma dimensao com valor nao numerico")
                print("Entre com o as dimensoes desejadas novamente\n")
        elif(passo == 2):
              try:
                larguraDoObjeto = int(input("\nDigite a largura do objeto em (em cm): "))
                if(larguraDoObjeto == 0 or larguraDoObjeto < 0 ):
                    passo = 2
                    print("O valor nao pode ser igual ou menor zero!")
                    print("Entre com o as dimensoes desejadas novamente\n")
                    continue
                passo += 1
              except ValueError:
                print("Voce digitou uma dimensao com valor nao numerico")
                print("Entre com o as dimensoes desejadas novamente\n")
        elif(passo == 3):
            # Calcula o volume do objeto
            volumeDoObjeto = alturaDoObjeto * larguraDoObjeto * comprimentoDoObjeto
            break
        
    # Calcula o valor do objeto a ser transportado
    if(volumeDoObjeto < 1000):
        valorTotal = 10
    elif(1000 <= volumeDoObjeto < 10000):
        valorTotal = 20
    elif(10000 <= volumeDoObjeto < 30000):
        valorTotal = 30
    elif(30000 <= volumeDoObjeto < 100000):
        valorTotal = 50
    elif(volumeDoObjeto > 100000):
        print("\nO volume do objeto e (em cm3): {}".format(float(volumeDoObjeto)))
        print("Nao aceitamos objetos com dimensoes tao grandes!")
        print("Entre com o as dimensoes desejadas novamente\n")
        return False
    
    print("\nO volume do objeto (em cm3): {}".format(float(volumeDoObjeto)))
    return valorTotal

# Calcula o peso do objeto de acordo com a entrada e o multiplicador
def pesoObjeto():
    global valorTotal
    pesoDoObjeto = 0
    multiplicador = 0
    
    while True:
            try:
                pesoDoObjeto = float(input("Digite o peso do objeto (em kg): "))
                if(pesoDoObjeto == 0 or pesoDoObjeto < 0):
                    print("O valor nao pode ser igual ou menor zero!")
                    print("Por favor entre com o peso desejado novamente\n")
                    continue
            except ValueError: 
                print("Voce digitou o peso com um valor nao numerico")
                continue
            break
        
    # Calcula o valor do objeto a ser transportado
    if(pesoDoObjeto <= 0.1):
        valorTotal *= 1
        multiplicador = 1
    elif(0.1 < pesoDoObjeto <= 1):
        valorTotal *= 1.5
        multiplicador = 1.5
    elif(1 < pesoDoObjeto < 10):
        valorTotal *= 2
        multiplicador = 2
        print("passei aqui")
    elif(10 <= pesoDoObjeto <= 30):
        valorTotal *= 3
        multiplicador = 3
    elif(pesoDoObjeto > 30):
        print("Nao aceitamos objetos tao pesados!")
        return False
        

    return multiplicador

# Calcula a rota do objeto de acordo com a entrada e o multiplicador
def rotaObjeto():
    global valorTotal
    rota = ""
    multiplicador = 0
    
    while True:
            try:
                print("\nSelecione a rota:")
                criarTabelaDeRotas()
                rota = str(input(">>> ")).upper()
                if(rota not in (rotas.keys())):
                    print("Voce digitou uma rota que nao existe!")
                    print("Por favor entre com a rota desejado novamente\n")
                    continue
            except NameError: 
                print("Voce digitou a rota com um valor numerico")
                print("Por favor entre com a rota desejado novamente\n")
                continue
            break
        
    multiplicador = rotas[rota]["value"]
    valorTotal *= multiplicador     
    
    return multiplicador

passo = 1

valorMedidas = 0
multiplicadorPeso = 0
multiplicadorRota = 0

# Inicia o ciclo de vida da aplicacao
while True:
    if(passo == 1):
        valorMedidas = dimensoesObjeto()
        if (valorMedidas == False):
            passo = 1
            continue
        passo += 1
    elif(passo == 2):
        multiplicadorPeso = pesoObjeto()
        if (multiplicadorPeso == False):
            passo = 2
            continue
        passo += 1
    elif(passo == 3):
        multiplicadorRota = rotaObjeto()
        if (multiplicadorRota == False):
            passo = 3
            continue
        passo += 1
    else:
        break
            
# Saida dos valores finais
print("\nTotal a pagar(R$): {} (dimensoes: {} * peso: {} * rota: {})".format(float(valorTotal),valorMedidas,multiplicadorPeso,multiplicadorRota))