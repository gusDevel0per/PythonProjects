agenda={}
lista_dados = ["Nome", "Telefone", "E-mail", "Data de nascimento"]

while 1:
    ope = int(input("""Agenda Pessoal

            1- Salvar Contato
            2- Alterar Contato
            3- Buscar Contato
            4- Apagar Contato
            5- Listar Contato



            Pressione 0 para sair"""))


    if ope == 1:
        print("Salvar Contato")
        contato=[]
        nome = input("Nome")
        contato.append(nome)
        contato.append(input("Telefone"))
        contato.append(input("E-mail"))
        contato.append(input("Data de nascimento"))
        agenda[nome] = contato
    elif ope == 2:
        print("Alterar Contato")
        nome = input("Qual contato: ")
        campo = input("Qual dos dados quer alterar?")
        novo_dado = input("Qual nova informação")
        agenda[nome][lista_dados.index(campo)] = novo_dado
        print(f"O contato foi alterado: {agenda[nome]}")
    elif ope == 3:
        print("Buscar Contato")
        nome = input("Qual contato: ")
        print(agenda[nome])
    elif ope == 4:
        print("Apagar Contato")
        nome = input("Qual contato: ")
        contato=agenda[nome]
        if contato==agenda.pop(nome):
            print(f"{nome} foi apagado!")
    elif ope == 5:
        print("Listar Contato")
        print(f"A agenda tem {len(agenda)}")
        for contato in agenda.values():
            print(contato)
    elif ope == 0:
        break
    else:
        print("")
