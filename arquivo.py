from csv import DictWriter, DictReader
from livro import Livro

DESTINO = '/home/luis/ondrive/livros-cli/livros.csv'

def salvar_linha_no_arquivo_csv(linha: str) -> None:
    with open(DESTINO, 'a', encoding='utf-8') as file:
        file.write(f"{linha}")

def reescrever_arquivo_com_lista_de_livros_atualizada(livros: list) -> None:
    with open(DESTINO, 'w', encoding='utf-8') as file:
        writer = DictWriter(file, fieldnames=['titulo', 'autor', 'editora', 'isbn', 'idioma', 'anoDeLancamento', 'numeroDePaginas'])
        
        writer.writeheader()
        
        for livro in livros:
            writer.writerow({'titulo': livro.titulo, 'autor': livro.autor, 'editora': livro.editora, 'isbn': livro.isbn, 'idioma': livro.idioma, 'anoDeLancamento': livro.ano_de_lancamento, 'numeroDePaginas': livro.numero_de_paginas})
    
def obter_lista_de_livros() -> list:
    with open(DESTINO, encoding='utf-8') as file:
        reader = DictReader(file)
        livros = list()
        
        for line in reader:
            titulo = line['titulo']
            autor = line['autor']
            editora = line['editora']
            isbn = line['isbn']
            idioma = line['idioma']
            ano_de_lancamento = line['anoDeLancamento']
            numero_de_paginas = line['numeroDePaginas']
            
            livro = Livro(titulo, autor, editora, isbn, idioma, ano_de_lancamento, numero_de_paginas)
            
            livros.append(livro)
        
        return livros
