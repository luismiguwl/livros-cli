from livro import Livro

def salvar_linha_no_arquivo_csv(livro: Livro):
	with open('/home/luis/ondrive/livros/livros.csv', 'a') as file:
		file.write(f"\n{livro}")

def adicionar_aspas_duplas_caso_haja_mais_de_um_autor(autor):
	if ',' in autor:
		return f'"{autor}"'
	return autor

def main():
	titulo = input('Título: ').rstrip().strip()
	autor = input('Autor: ').rstrip().strip()
	editora = input('Editora: ').rstrip().strip()
	isbn = int(input('ISBN: '))
	idioma = input('Idioma: ').rstrip().strip()
	ano_de_lancamento = int(input('Ano de lançamento: '))

	autor = adicionar_aspas_duplas_caso_haja_mais_de_um_autor(autor)

	livro = Livro(titulo, autor, editora, isbn, idioma, ano_de_lancamento)
	salvar_linha_no_arquivo_csv(livro)

if __name__ == '__main__':
	main()
