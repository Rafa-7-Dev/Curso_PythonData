palavra = "Rafael"
contador = 1

for letra in palavra : 
    print(str(contador) + "-" + letra)
    contador = contador + 1

cidades = ["São Paulo","Ribeirão Pires", "Cotia", "Mauá", "Poá"]
print(cidades[2])

for cidade in cidades :
    print(cidade)
    
botaoExecutar = True
contador = 0
    
while botaoExecutar : #while = enquanto
    print(contador)
    contador = contador + 1
    if contador >= 10 :
        botaoExecutar = False