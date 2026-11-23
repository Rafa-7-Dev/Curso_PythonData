
def minhaFuncao(curso) :
    print("curso de " + curso + " na Clarify")
    
minhaFuncao("Python")
minhaFuncao("SQL")
minhaFuncao("Claude")


cidades = ["São Paulo","Ribeirão Pires", "Cotia", "Mauá", "Poá"]
contador = 0

def minhaFuncaoMelhorada(item01, item02) :
    print(str(item02) + ' - ' + item01)


for cidade in cidades :
    contador = contador + 1
    minhaFuncaoMelhorada(cidade, contador)