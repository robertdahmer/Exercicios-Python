dados_pessoa = dict()
dados_pessoa['Nome'] = str(input('Nome: ')).capitalize()
dados_pessoa['Ano'] = int(input('Ano de nascimento: '))
dados_pessoa['Carteira de Trabalho'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados_pessoa['Carteira de Trabalho'] == 0:
    for k, v in dados_pessoa.items():
        print(f'    - {k} tem o valor {v}')
else:
    dados_pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    dados_pessoa['Salário'] = int(input('Salário: R$'))
    idade = dados_pessoa['Ano de contratação'] - dados_pessoa['Ano']
    aposentadoria = 65 - idade
    dados_pessoa['Aposentadoria'] = aposentadoria
    for k, v in dados_pessoa.items():
        print(f'    - {k} tem o valor {v}')

