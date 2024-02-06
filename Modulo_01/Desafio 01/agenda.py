def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {"contato": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome_contato} adicionado com sucesso!")
    return

def ver_contatos(contatos):
    print("\nLista de contatos")
    for indice, contato in enumerate(contatos, start=1):
        favorito = "Favorito [✓]" if contato["favorito"] else "Favorito [ ]"
        nome_contato = contato["contato"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"{indice}. {favorito} {nome_contato} {telefone_contato} {email_contato}")
    return

def editar_contato(contatos, indice_contato, novo_nome_contato, novo_numero_contato, novo_email_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["contato"] = novo_nome_contato
        contatos[indice_contato_ajustado]["telefone"] = novo_numero_contato
        contatos[indice_contato_ajustado]["email"] = novo_email_contato
        print(f"Contato {indice_contato} atualizado para {novo_nome_contato}, {novo_numero_contato}, {novo_email_contato}")
    else:
        print("Índice de contato inválido.")
    return

def marcar_favorito(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["favorito"] = True
        print(f"Contato {indice_contato} marcado como favorito.")
    else:
        print("Índice de contato inválido.")

def desmarcar_favorito(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["favorito"] = False
        print(f"Contato {indice_contato} desmarcado como favorito.")
    else:
        print("Índice de contato inválido.")

def ver_favoritos(contatos):
    favoritos = [contato for contato in contatos if contato["favorito"]]
    if favoritos:
        print("\nLista de contatos favoritos:")
        for indice, contato in enumerate(favoritos, start=1):
            nome_contato = contato["contato"]
            telefone_contato = contato["telefone"]
            email_contato = contato["email"]
            print(f"{indice}. {nome_contato} {telefone_contato} {email_contato}")
    else:
        print("\nNenhum contato favorito encontrado.")

def apagar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        nome_contato = contatos[indice_contato_ajustado]["contato"]
        del contatos[indice_contato_ajustado]
        print(f"Contato {nome_contato} apagado com sucesso.")
    else:
        print("Índice de contato inválido.")

contatos = []
while True:
    print("\nAgenda de contatos:")
    print("1. Adicionar novo contato")
    print("2. Visualizar lista de contatos")
    print("3. Editar contato")
    print("4. Marcar contato como favorito")
    print("5 .Desmarcar contato como favorito")
    print("6. Ver lista de contatos favoritos")
    print("7. Apagar contato")
    print("8. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_contato = input("Nome do contato:  ")
        telefone_contato = input("Número de telefone:  ")
        email_contato = input("Email do contato:  ")
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
    elif escolha == "2":
        ver_contatos(contatos)
    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o índice do contato que deseja atualizar:")
        novo_nome = input("Digite o novo nome do contato:")
        novo_numero = input("Digite o novo número do contato:")
        novo_email = input("Digite o novo email do contato:")
        editar_contato(contatos, indice_contato, novo_nome, novo_numero, novo_email)
    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o índice do contato que deseja marcar como favorito: ")
        marcar_favorito(contatos, indice_contato)
    elif escolha == "5":
        ver_contatos(contatos)
        indice_contato = input("Digite o índice do contato que deseja desmarcar como favorito: ")
        desmarcar_favorito(contatos, indice_contato)
    elif escolha == "6":
        ver_favoritos(contatos)
    elif escolha == "7":
        ver_contatos(contatos)
        indice_contato = input("Digite o índice do contato que deseja apagar: ")
        apagar_contato(contatos, indice_contato)
    elif escolha == "8":
        break
print("Programa finalizado.")
