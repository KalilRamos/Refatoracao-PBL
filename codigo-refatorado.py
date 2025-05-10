biblioteca = {
    1: {"titulo": "Dom Casmurro", "emprestado": False},
    2: {"titulo": "1984", "emprestado": True},  # já emprestado
    3: {"titulo": "O Senhor dos Anéis", "emprestado": False},
    4: {"titulo": "Harry Potter", "emprestado": True}  # já emprestado
}

def exibir_menu():
    print("\n1 - Empréstimo")
    print("2 - Devolução")
    print("3 - Listar Livros")
    print("4 - Sair")
    return input("Escolha uma opção: ")

def listar_livros(disponivel=True):
    titulo = "Livros disponíveis" if disponivel else "Livros emprestados"
    print(f"\n{titulo}:")
    encontrados = False
    for id_livro, info in biblioteca.items():
        if info["emprestado"] != disponivel:
            continue
        print(f"{id_livro} - {info['titulo']}")
        encontrados = True
    if not encontrados:
        print("- Nenhum livro.")

def emprestar_livro():
    listar_livros(disponivel=True)
    escolha = input("Digite o ID do livro para empréstimo: ")
    if escolha.isdigit():
        escolha = int(escolha)
        if escolha in biblioteca and not biblioteca[escolha]["emprestado"]:
            biblioteca[escolha]["emprestado"] = True
            print(f"Livro '{biblioteca[escolha]['titulo']}' emprestado!")
        else:
            print("ID inválido ou livro já emprestado!")
    else:
        print("Digite um número válido!")

def devolver_livro():
    listar_livros(disponivel=False)
    escolha = input("Digite o ID do livro para devolução: ")
    if escolha.isdigit():
        escolha = int(escolha)
        if escolha in biblioteca and biblioteca[escolha]["emprestado"]:
            biblioteca[escolha]["emprestado"] = False
            print(f"Livro '{biblioteca[escolha]['titulo']}' devolvido!")
        else:
            print("ID inválido ou livro não está emprestado!")
    else:
        print("Digite um número válido!")

def main():
    opcao = exibir_menu()
    if opcao == "1":
        emprestar_livro()
    elif opcao == "2":
        devolver_livro()
    elif opcao == "3":
        listar_livros(disponivel=True)
        listar_livros(disponivel=False)
    elif opcao == "4":
        print("Saindo...")
        return
    else:
        print("Opção inválida!")

    main()  # Chamada recursiva para repetir o menu

# Execução do programa
main()
