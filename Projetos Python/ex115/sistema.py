from ex115.lib.interface import *
from time import sleep
from ex115.lib.arquivo import *

arq = 'arquivodetexto.txt'
if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso')
else:
    print('Arquivo não encontrado')
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        print('Saindo do sistema... Até logo!')
        break
    elif resposta != 1 or 2 or 3:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(2)
