import pandas as pd

data = {
    'Nome':['Rafael','Lucas','Leonardo','Caio','Nicole'],
    'Idade':[20,25,35,39,16],
    'Salario':[5000,6000,7000,8000,9000]
}

df = pd.DataFrame(data)
print (f'DataFrame bruto: \n{df}')

print(f'Coluna nome: \n{df['Nome']}')
print('Apenas pessoas 30+')
print(df[df['Idade']>30])

# Adicionar imposto
df['Imposto'] = df['Salario'] *0.1
print(f'O imposto a pagar é: {df}')

df.to_csv('salarios.csv', index = False)
