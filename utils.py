from csv import DictReader, DictWriter
from livro import Livro

def obter_lista_de_livros():
    with open('/home/luis/ondrive/livros/livros.csv', encoding='utf-8') as file:
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
            
def obter_numero_do_livro_que_sera_removido():
    livros = obter_lista_de_livros()
    
    print('\n=== TÍTULOS ===')
    for i in range(len(livros)):
        print(f"{i + 1}. {livros[i].titulo} ({livros[i].ano_de_lancamento}) por {livros[i].autor}")
    
    numero_do_livro = int(input('Número do livro: '))
    return numero_do_livro

def salvar_linha_no_arquivo_csv(linha):
    with open('/home/luis/ondrive/livros/livros.csv', 'a', encoding='utf-8') as file:
        file.write(f"{linha}")

def reescrever_arquivo_com_lista_de_livros_atualizada(livros):
    with open('/home/luis/ondrive/livros/livros.csv', 'w', encoding='utf-8') as file:
        writer = DictWriter(file, fieldnames=['titulo', 'autor', 'editora', 'isbn', 'idioma', 'anoDeLancamento', 'numeroDePaginas'])
        
        writer.writeheader()
        
        for livro in livros:
            writer.writerow({'titulo': livro.titulo, 'autor': livro.autor, 'editora': livro.editora, 'isbn': livro.isbn, 'idioma': livro.idioma, 'anoDeLancamento': livro.ano_de_lancamento, 'numeroDePaginas': livro.numero_de_paginas})
