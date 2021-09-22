from arquivo import obter_lista_de_livros
            
def obter_numero_do_livro_que_sera_removido():
    livros = obter_lista_de_livros()
    
    print('\n=== TÍTULOS ===')
    for i in range(len(livros)):
        print(f"{i + 1}. {livros[i].titulo} ({livros[i].ano_de_lancamento}) por {livros[i].autor}")
    
    numero_do_livro = int(input('Número do livro: '))
    return numero_do_livro