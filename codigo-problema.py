# Sistema de Biblioteca (Versão Bagunçada)  
biblioteca = ["Dom Casmurro", "1984", "O Senhor dos Anéis", "Harry Potter"]  
emprestados = []  

while True:  
    print("\n1 - Empréstimo\n2 - Devolução\n3 - Listar Livros\n4 - Sair")  
    opcao = input("Escolha uma opção: ")  

    if opcao == "1":  
        print("Livros disponíveis:")  
        for i, livro in enumerate(biblioteca):  
            print(f"{i+1} - {livro}")  
        escolha = input("Digite o número do livro: ")  
        if escolha.isdigit():  
            escolha = int(escolha) - 1  
            if 0 <= escolha < len(biblioteca):  
                livro_escolhido = biblioteca.pop(escolha)  
                emprestados.append(livro_escolhido)  
                print(f"Livro '{livro_escolhido}' emprestado!")  
            else:  
                print("Número inválido!")  
        else:  
            print("Digite um número!")  

    elif opcao == "2":  
        if not emprestados:  
            print("Nenhum livro emprestado!")  
        else:  
            print("Livros emprestados:")  
            for i, livro in enumerate(emprestados):  
                print(f"{i+1} - {livro}")  
            escolha = input("Digite o número do livro para devolver: ")  
            if escolha.isdigit():  
                escolha = int(escolha) - 1  
                if 0 <= escolha < len(emprestados):  
                    livro_devolvido = emprestados.pop(escolha)  
                    biblioteca.append(livro_devolvido)  
                    print(f"Livro '{livro_devolvido}' devolvido!")  
                else:  
                    print("Número inválido!")  
            else:  
                print("Digite um número!")  

    elif opcao == "3":  
        print("\nLivros disponíveis:")  
        for livro in biblioteca:  
            print(f"- {livro}")  
        print("\nLivros emprestados:")  
        for livro in emprestados:  
            print(f"- {livro}")  

    elif opcao == "4":  
        print("Saindo...")  
        break  

    else:  
        print("Opção inválida!")  
