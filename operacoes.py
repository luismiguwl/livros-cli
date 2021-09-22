from livro import Livro
import utils

def adicionar_livro():
	titulo = input('Título: ').rstrip().strip()
	autor = input('Autor: ').rstrip().strip()
	editora = input('Editora: ').rstrip().strip()
	isbn = int(input('ISBN: '))
	idioma = input('Idioma: ').rstrip().strip()
	ano_de_lancamento = int(input('Ano de lançamento: '))
	numero_de_paginas = int(input('Número de páginas: '))

	livro = Livro(titulo, autor, editora, isbn, idioma, ano_de_lancamento, numero_de_paginas)
	utils.salvar_linha_no_arquivo_csv(livro)

def remover_livro(posicao_do_livro):
	livros = utils.obter_lista_de_livros()
 
	del livros[posicao_do_livro - 1]
 
	utils.reescrever_arquivo_com_lista_de_livros_atualizada(livros)
