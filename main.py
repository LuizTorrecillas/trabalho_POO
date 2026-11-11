from modelos import Filme, Serie

catalogo = []

while True:
    print("\n--- Catálogo de Séries e Filmes ---")
    print("1. Adicionar Mídia")
    print("2. Listar Mídias")
    print("3. Atualizar Mídia")
    print("4. Remover Mídia")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("A encerrar o sistema...")
        break

    elif opcao == "1":
        print("\n--- Adicionar Mídia ---")
        tipo = input("Digite 1 para Filme ou 2 para Série: ")

        nome = input("Título: ")
        ano = input("Ano de lançamento: ")
        genero = input("Género: ")

        if not nome or not genero or not ano:
            print("Erro: Nenhum dos campos pode ficar vazio")
            continue

        if not ano.isdigit():
            print("Erro: O ano de lançamento deve ser um número.")
            continue

        if tipo == "1":
            duracao = input("Duração (em minutos): ")
            if not duracao.isdigit():
                print("Erro: A duração deve ser um número.")
                continue
            novo_filme = Filme(nome, ano, genero, duracao)
            catalogo.append(novo_filme)
            print(f"Filme '{nome}' adicionado com sucesso")

        elif tipo == "2":
            temporadas = input("Número de temporadas: ")
            if not temporadas.isdigit():
                print("Erro: O número de temporadas deve ser um número.")
                continue
            nova_serie = Serie(nome, ano, genero, temporadas)
            catalogo.append(nova_serie)
            print(f"Série '{nome}' adicionada com sucesso!")

        else:
            print("Tipo de mídia inválido.")

    elif opcao == "2":
        print("\n--- Lista de Mídias ---")
        if not catalogo:
            print("O catálogo ainda está vazio.")
        else:
            for indice, midia in enumerate(catalogo):
                print(f"[{indice}] - {midia}")

    elif opcao == "3":
        print("\n--- Atualizar Mídia ---")
        if not catalogo:
            print("O catálogo ainda está vazio.")
            continue

        for indice, midia in enumerate(catalogo):
            print(f"[{indice}] - {midia}")

        indice_str = input("Digite o índice da mídia que deseja atualizar: ")

        if not indice_str.isdigit() or int(indice_str) not in range(len(catalogo)):
            print("Erro: Índice inválido.")
            continue

        indice = int(indice_str)
        midia = catalogo[indice]

        print("Deixe o campo em branco para manter o valor atual.")
        nome = input(f"Novo título [{midia._nome}]: ")
        ano = input(f"Novo ano de lançamento [{midia._ano_lancamento}]: ")
        genero = input(f"Novo género [{midia._genero}]: ")

        if ano and not ano.isdigit():
            print("Erro: O ano de lançamento deve ser um número.")
            continue

        if isinstance(midia, Filme):
            duracao = input(f"Nova duração em minutos [{midia._duracao}]: ")
            if duracao and not duracao.isdigit():
                print("Erro: A duração deve ser um número.")
                continue
            midia.atualizar(nome, ano, genero, duracao)

        elif isinstance(midia, Serie):
            temporadas = input(f"Novo número de temporadas [{midia._temporadas}]: ")
            if temporadas and not temporadas.isdigit():
                print("Erro: O número de temporadas deve ser um número.")
                continue
            midia.atualizar(nome, ano, genero, temporadas)

        print("Mídia atualizada com sucesso!")

    elif opcao == "4":
        print("\n--- Remover Mídia ---")
        if not catalogo:
            print("O catálogo ainda está vazio.")
            continue

        for indice, midia in enumerate(catalogo):
            print(f"[{indice}] - {midia}")

        indice_str = input("Digite o índice da mídia que deseja remover: ")

        if not indice_str.isdigit() or int(indice_str) not in range(len(catalogo)):
            print("Erro: Índice inválido.")
            continue

        indice = int(indice_str)
        confirmacao = input(f"Tem certeza que deseja remover '{catalogo[indice]._nome}'? (s/n): ")

        if confirmacao.lower() == "s":
            removida = catalogo.pop(indice)
            print(f"Mídia '{removida._nome}' removida com sucesso!")
        else:
            print("Remoção cancelada.")

    else:
        print("Opção inválida! Tenta novamente.")