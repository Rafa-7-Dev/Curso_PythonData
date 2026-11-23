# != Diferente
# == Igual
# > Maior
# < Menor
# >= Maior ou Igual
# <= Menor ou Igual

mediaAluno = int(input("Qual a média do aluno? \nR: "))
freqAluno = int(input("Qual a frequência do aluno \nR: "))
mediaCorte = 7
freqCorte = 70

if mediaAluno >= mediaCorte and freqAluno >= freqCorte :
    print ("Aprovado")
else: 
    print ("reprovado")