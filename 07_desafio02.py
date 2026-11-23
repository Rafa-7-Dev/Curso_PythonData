#Desafio02
executar = True
while executar :
    nome        = input("digite o seu nome:")
    anoAtua     = int(input("digite o ano atual:"))
    anoNasc     = int(input("digite o seu ano de nascimento:"))
    idades      = anoAtua - anoNasc
    print("olá " + nome + "você tem " + str(idades) + " anos.")
    opcao = input("Você deseja testar novamente? \n[1] Sim ou [2] não?")
    if opcao == "2" or opcao == "Não" or opcao == "não" or opcao == "nao" or opcao == "Nao" :
        executar = False