""" Desafio """

#perguntar o nome e ano de nascimento
#retornar saudação com nome e idade

Nome = input("Qual o seu nome?")
Nascimento = input("Quando você nasceu?")
anoAtual = 2026
idade = anoAtual - int(Nascimento)

print ("Olá seu nome é: " + Nome + " e você tem " + str(idade) +" anos.")