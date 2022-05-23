# coding=UTF-8 
#----------------------INICIO DO PROGAMA---------------------------#
# Armazenamento da indentificacao pessoal e metodo para mostrar no console

nome = "Anderson dos santos Reinaldo"
ru   = "3930112"

def showIndentificacaoPessoal():
    global nome,ru
    print("\nBem vindo ao controle de estoque da bicicletaria do {}!\nRU:{}\n".format(nome,ru))
    
showIndentificacaoPessoal()

menuItens = {
 "1" : {"label":"Cadastrar Pecas"},
 "2" : {"label": "Consultar Pecas"},
 "3" : {"label": "Remover Pecas"},
 "4" : {"label": "Sair",}
}

menuItensConsulta = {
 "1" : {"label":"Consulta Todas as Pecas"},
 "2" : {"label": "Consultar Pecas por codigo"},
 "3" : {"label": "Consultar Pecas por fabricante"},
 "4" : {"label": "Retornar"},
}

pecas = []

# Funcao responsavel por cadastro de uma nova peca
def cadastrarPeca():
    global pecas
    
    # Criacao do novo codigo unico da peca
    currentCodigo = 0
    if(len(pecas) > 0):
        if  int(pecas[len(pecas) - 1]["cod"]) < 9:
           newCod = int(pecas[len(pecas) - 1]["cod"]) + 1 
           currentCodigo =  "00{}".format(newCod)
        elif  int(pecas[len(pecas) - 1]["cod"]) >= 9 and int(pecas[len(pecas) - 1]["cod"]) < 99:
           newCod = int(pecas[len(pecas) - 1]["cod"]) + 1 
           currentCodigo =  "0{}".format(newCod)
        elif int(pecas[len(pecas) - 1]["cod"]) >= 99:
           newCod = int(pecas[len(pecas) - 1]["cod"]) + 1 
           currentCodigo =  "{}".format(newCod)
    else:
        currentCodigo = "001"
        
    print("Voce Selecionou a opcao de Cadastrar Peca")
    print("Codigo da Peca {}".format(currentCodigo))
    
    nomePeca = str(input("Por favor entre com o NOME da peca: ")).lower()
    fabricantePeca = str(input("Por favor entre com o FABRICANTE da peca: ")).lower()
    valorPeca = float(input("Por favor entre com o VALOR(R$) da peca: "))
    
    pecas.append({"cod": str(currentCodigo), "nome": nomePeca, "fabricante": fabricantePeca, "preco": valorPeca })
    showMenu()

# Funcao responsavel por consultar as pecas  
def consultarPeca():
    print("Voce Selecionou a opcao de Consulta Pecas")
    showMenuConsultas()
    
    try:    
        acaoSelect = int(input(">>> "))
        
        if(str(acaoSelect) not in menuItens.keys()):
            print("\nOpa, opcao nao encontrada!")
            showMenu()
            
        if(acaoSelect == 1):
            print(30*"-")
            if(len(pecas) > 0):
                for peca in pecas:
                    print("codigo: {}\nnome: {}\nfabricante: {}\nvalor: {}\n".format(peca["cod"],peca["nome"],peca["fabricante"],peca["preco"]))
            else:
                print("Nenhuma peca cadastrada!")
            print(30*"-")
            
        elif(acaoSelect == 2):
            if(len(pecas) > 0):
                codPeca = int(input("Digite o codigo da peca: "))
                print(30*"-")
                for peca in pecas:
                    if(str(codPeca) in peca["cod"]):
                        print("codigo: {}\nnome: {}\nfabricante: {}\nvalor: {}\n".format(peca["cod"],peca["nome"],peca["fabricante"],peca["preco"]))
                        
            else:
                print("Nenhuma peca cadastrada!")
            print(30*"-")
        elif(acaoSelect == 3):
            if(len(pecas) > 0):
                nomeFabricante = str(input("Digite o nome do fabricante: ")).lower()
                print(30*"-")
                for peca in pecas:
                    if(nomeFabricante in peca["fabricante"]):
                        print("codigo: {}\nnome: {}\nfabricante: {}\nvalor: {}\n".format(peca["cod"],peca["nome"],peca["fabricante"],peca["preco"]))
                        
            else:
                print("Nenhuma peca cadastrada!")
            print(30*"-")
        elif(acaoSelect == 4):
            print("Saindo...")
            showMenu()
            return
    except ValueError:
        print("\nO valor digitado nao e inteiro!")
        showMenu()
    consultarPeca()
    
# Funcao responsavel por remover uma peca 
def removerPeca():
    print("Voce Selecionou a opcao de Remover Peca")    
    try:    
        if(len(pecas) > 0):
                codPeca = int(input("Digite o Codigo da Peca a ser removida: "))
                print(30*"-")
                for idx, peca in enumerate(pecas):
                    if(str(codPeca) in peca["cod"]):
                        pecas.pop(idx)
        else:
            print("Nenhuma peca cadastrada!")
            print(30*"-")
    except ValueError:
        print("\nO valor digitado nao e inteiro!")
    showMenu()
    
# Menu principal
def showMenu():
    print("Escolha a opcao desejada:")
    for itemMenu in menuItens:
        print("{} - {}".format(itemMenu,menuItens[itemMenu]["label"]))
    
    try:    
        acaoSelect = int(input(">>> "))
        
        if(str(acaoSelect) not in menuItens.keys()):
            print("\nOpa, opcao nao encontrada!")
            showMenu()
            
        if(acaoSelect == 1):
            cadastrarPeca()
        elif(acaoSelect == 2):
            consultarPeca()
        elif(acaoSelect == 3):
            removerPeca()
        elif(acaoSelect == 4):
            print("Saindo...")
            return
    except ValueError:
        print("\nO valor digitado nao e inteiro!")
        showMenu()

# Menu de consultas
def showMenuConsultas():
    print("Escolha a opcao desejada:")
    for itemMenuConsulta in menuItensConsulta:
        print("{} - {}".format(itemMenuConsulta,menuItensConsulta[itemMenuConsulta]["label"]))
        


showMenu()    