import os
import csv
import datetime

def busca_contatos():
    pass

def lista_contatos(contatos):
    print(f"A agenda tem {len(contatos)} contatos")
    for nome in contato.keys():
        print(busca_contato(nome))
        
if os.path.isdir("/Users/gustavo.csilva/Desktop/python/agenda"):
    pass
else:
    os.mkdir("/Users/gustavo.csilva/Desktop/python/agenda")
    os.chdir("/Users/gustavo.csilva/Desktop/python/agenda")

def salva_agenda(saida):
    with open("agenda.csv", "w", newline="") as arquivo_csv:
        saida = csv.writer(arquivo_csv)
        saida.writerows(agenda.values())

def leitura_agenda() :
    with open("agenda.csv") as arquivo_csv:
        entrada = csv.reader(arquivo_csv)

        for contato in entrada:
            agenda[contato[0]]=contato
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
        print("Sua data de nascimento: ")
        ano= int(input("Ano: "))
        mes= int(input("Mês: "))
        dia= int(input("Dia: "))
        datanasc= datetime.date(year=ano,month=mes,day=dia)
        contato.append(datanasc)
        dataredister = datetime.datetime.today()
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
        leitura_agenda()
        print(f"A agenda tem {len(agenda)}")
        
        for contato in agenda.values():
            print(contato)
    elif ope == 0:
        salva_agenda(agenda)
        break
    else:
        print("")
