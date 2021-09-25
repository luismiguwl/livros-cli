from sys import exit
import operacoes
import utils

OPCOES = ['Adicionar livro', 'Remover livro', 'Sair']

def executar_opcao_selecionada(numero_da_opcao: int) -> None:
    opcao_selecionada = OPCOES[numero_da_opcao - 1]

    if opcao_selecionada == 'Adicionar livro':
        operacoes.adicionar_livro()

    if opcao_selecionada == 'Remover livro':
        numero_do_livro_que_sera_removido = utils.obter_numero_do_livro_que_sera_removido()
        operacoes.remover_livro(numero_do_livro_que_sera_removido)

    if opcao_selecionada == 'Sair':
        exit(0)

def obter_acao_selecionada() -> int:
    return int(input('\nNúmero da opção: '))

def exibir() -> None:
    print("=== MENU ===")

    for i in range(len(OPCOES)):
        print(f"{i + 1}. {OPCOES[i]}")