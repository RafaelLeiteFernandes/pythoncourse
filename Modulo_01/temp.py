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

def editar_contato(contatos,indice_contato, nome_contato, telefone_contato, email_contato, novo_nome_contato, novo_numero_contato, novo_email_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >=0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["contato"] = novo_nome_contato
        contatos[indice_contato_ajustado]["telefone"] = novo_numero_contato
        contatos[indice_contato_ajustado]["email"] = novo_email_contato
        print(f"Contato {indice_contato} atualizada para {novo_nome_contato}, {novo_numero_contato}, {novo_email_contato}")
    else:
        print("Índice de tarefa inválido.")
    return


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
        indice_contato = input("Digite o indice do numero que deseja atualizar:")
        novo_nome = input("Digite o novo nome do contato:")
        novo_numero = input("Digite o novo numero do contato:")
        novo_email = input("Digite o novo email do contato:")
        editar_contato(contatos, indice_contato, novo_nome, novo_numero, novo_email)
    elif escolha == "4":
        print("")
    elif escolha == "5":
        print("")
    elif escolha == "6":
        print("")
    elif escolha == "7":
        print("")
    elif escolha == "8":
        break

print("Programa finalizado.")