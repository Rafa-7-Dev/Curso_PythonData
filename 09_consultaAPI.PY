import json, requests


nomeUsuario = input('Qual o seu nome?\nR: ')
resultado   = requests.get('https://servicodados.ibge.gov.br/api/v2/censos/nomes/{}'.format(nomeUsuario))
estados = '''
    Qual estado que deseja buscar?
    [35] - SP
    [33] - RJ
    [31] - MG
    [43] - RS
    [53] - DF
'''

localidade = 0
while localidade <1 or localidade >2 :
    localidade = int(input ('Você deseja selecionar uma localidade?\nR [1] SIM\n[2] NÃO\n'))
    
if localidade == 1 : #Sim, quero localidade
    uf = input (estados)
    resultado = requests.get('https://servicodados.ibge.gov.br/api/v2/censos/nomes/{}?localidade={}'.format(nomeUsuario,uf))
    
    
if localidade == 2 : #não, quero o território Brasil
    resultado = requests.get('https://servicodados.ibge.gov.br/api/v2/censos/nomes/{}'.format(nomeUsuario))
    
print('''
      escolha o periodo de tempo:
      [1] 1930 - 2010
      [2] 1930 - 1940
      [3] 1940 - 1950
      [4] 1950 - 1960
      [5] 1960 - 1970
      [6] 1970 - 1980
      [7] 1980 - 1990
      [8] 1990 - 2000
      [9] 2000 - 2010
      ''')

periodo = int(input('Selecione o periodo desejado:')) - 1
dados_json  = json.loads(resultado.text)

print(dados_json[0]['res'][periodo])

