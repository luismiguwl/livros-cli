from operacoes import adicionar_livro


class Livro:
	def __init__(self, titulo, autor, editora, isbn, idioma, ano_de_lancamento, numero_de_paginas):
		self.titulo = titulo
		self.autor = self.adicionar_aspas_duplas_caso_haja_mais_de_um_autor()
		self.editora = editora
		self.isbn = isbn
		self.idioma = idioma
		self.ano_de_lancamento = ano_de_lancamento
		self.numero_de_paginas = numero_de_paginas

	def __repr__(self):
		return f"{self.titulo},{self.autor},{self.editora},{self.isbn},{self.idioma},{self.ano_de_lancamento},{self.numero_de_paginas}"

	def adicionar_aspas_duplas_caso_haja_mais_de_um_autor(self, autor):
		if ',' in self.autor:
			return f'"{autor}"'
		return autor
