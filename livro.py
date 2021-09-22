class Livro:
	def __init__(self, titulo, autor, editora, isbn, idioma, ano_de_lancamento):
		self.titulo = titulo
		self.autor = autor
		self.editora = editora
		self.isbn = isbn
		self.idioma = idioma
		self.ano_de_lancamento = ano_de_lancamento

	def __repr__(self):
		return f"{self.titulo},{self.autor},{self.editora},{self.isbn},{self.idioma},{self.ano_de_lancamento}"