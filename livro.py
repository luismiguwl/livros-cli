class Livro:
	def __init__(self, titulo: str, autor: str, editora: str, isbn: str, idioma: str, ano_de_lancamento: str, numero_de_paginas: str):
		self.titulo = titulo
		self.autor = self.adicionar_aspas_duplas_caso_haja_mais_de_um_autor(autor)
		self.editora = editora
		self.isbn = isbn
		self.idioma = idioma
		self.ano_de_lancamento = ano_de_lancamento
		self.numero_de_paginas = numero_de_paginas

	def __repr__(self) -> str:
		return f"{self.titulo},{self.autor},{self.editora},{self.isbn},{self.idioma},{self.ano_de_lancamento},{self.numero_de_paginas}"

	def adicionar_aspas_duplas_caso_haja_mais_de_um_autor(self, autor: str) -> str:
		if ',' in autor:
			return f'"{autor}"'
		return autor