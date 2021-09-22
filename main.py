import menu

def main():
    while True:
        menu.exibir()        
        opcao = menu.obter_acao_selecionada()
        menu.executar_opcao_selecionada(opcao)

if __name__ == '__main__':
	main()
