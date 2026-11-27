import pandas as pd

df = pd.read_csv('salarios.csv')

print(df)


# Traz os primeiros itens
print('-----HEAD-----')
print(df.head())
# informações do DataFrame
print('-----INFO-----')
print(df.info())
# Estatisticas
print('-----DESCRIBE-----')
print(df.describe())

# dois filtros juntos
print("-----FILTROS-----")
print(df[( df['Idade'])>20 & (df['Salario']>6000 )])

# Classificação as pela idade
print('-----Classificador-----')
df['classificacao'] = df['Idade'].apply(
    lambda idade: 'Maior de idade' if idade >= 18 else 'Menor de idade'
)
print(df[['Nome', 'Idade', 'classificacao']])

# Usando LAMBDA com for
print('-----LAMBDA DO FOR-----')
notas = [4, 5, 7, 2, 9]
df2 = pd.DataFrame({'Notas':notas})
df2['Resultado'] = df2['Notas'].apply(
    lambda nota : 'Aprovado' if nota >= 7 else 'Reprovado'
)

print('-----Salarios do maior para o menor-----')
print(df.sort_values(by='Salario', ascending = False))

# Acessar linhas específicas
print('Primeiro funcionario')
print(df.iloc[0])
print('Primeiro 3 funcionario')
print(df.iloc[:3])

# Média das idades
print('-----Idade Média-----')
print(df['Salario'].count())
print(df['Idade'].mean())
print(df['Salario'].sum())
# Alem destes temos: min e max tambem

# Temos duas formas para salvar 

# ou criamos um novo
df.to_csv('salarios_atualizados.csv', index = False)
# ou sobrescrevemos o arquivo original
df.to_csv('salarios.csv', index = False)