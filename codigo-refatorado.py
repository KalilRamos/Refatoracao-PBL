import json

ARQUIVO_JSON = "biblioteca.json"

def carregar_biblioteca():
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            return {int(k): v for k, v in json.load(f).items()}
    except FileNotFoundError:
        return {}

def salvar_biblioteca(biblioteca):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(biblioteca, f, indent=4, ensure_ascii=False)

def exibir_menu():
    print("\n📚 MENU DA BIBLIOTECA")
    print("1 - Empréstimo")
    print("2 - Devolução")
    print("3 - Listar Livros")
    print("4 - Sair")
    return input("Escolha uma opção: ")

def listar_livros(biblioteca, disponivel=True):
    titulo = "Livros disponíveis" if disponivel else "Livros emprestados"
    print(f"\n{titulo}:")
    encontrados = False
    for id_livro, info in biblioteca.items():
        if info["emprestado"] == (not disponivel):
            print(f"{id_livro} - {info['titulo']}")
            encontrados = True
    if not encontrados:
        print("- Nenhum livro.")

def emprestar_livro(biblioteca):
    listar_livros(biblioteca, disponivel=True)
    escolha = input("Digite o ID do livro para empréstimo: ")
    if escolha.isdigit():
        escolha = int(escolha)
        if escolha in biblioteca and not biblioteca[escolha]["emprestado"]:
            biblioteca[escolha]["emprestado"] = True
            salvar_biblioteca(biblioteca)
            print(f"✅ Livro '{biblioteca[escolha]['titulo']}' emprestado!")
        else:
            print("❌ ID inválido ou livro já emprestado!")
    else:
        print("❌ Digite um número válido!")

def devolver_livro(biblioteca):
    listar_livros(biblioteca, disponivel=False)
    escolha = input("Digite o ID do livro para devolução: ")
    if escolha.isdigit():
        escolha = int(escolha)
        if escolha in biblioteca and biblioteca[escolha]["emprestado"]:
            biblioteca[escolha]["emprestado"] = False
            salvar_biblioteca(biblioteca)
            print(f"✅ Livro '{biblioteca[escolha]['titulo']}' devolvido!")
        else:
            print("❌ ID inválido ou livro não está emprestado!")
    else:
        print("❌ Digite um número válido!")

def main(biblioteca):
    opcao = exibir_menu()

    if opcao == "1":
        emprestar_livro(biblioteca)
    elif opcao == "2":
        devolver_livro(biblioteca)
    elif opcao == "3":
        listar_livros(biblioteca, disponivel=True)
        listar_livros(biblioteca, disponivel=False)
    elif opcao == "4":
        print("👋 Saindo...")
        return
    else:
        print("❌ Opção inválida!")

    main(biblioteca)  
