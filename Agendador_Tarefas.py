# ==========================================
# AGENDADOR DE TAREFAS
# Autor: Exemplo para iniciantes
# ==========================================

# Array (Lista) que armazenará todas as tarefas
tarefas = []

import os
import time


# -------------------------
# Limpar terminal
# -------------------------
def limpar_terminal():

    os.system("cls" if os.name == "nt" else "clear")


# -------------------------
# Mensagens do sistema
# -------------------------
def mensagem_sucesso(texto):

    print("\n==============================")
    print("✅ SUCESSO!")
    print(texto)
    print("==============================")

    time.sleep(4)  # espera 3 segundos

    limpar_terminal()



def mensagem_erro(texto):

    print("\n==============================")
    print("❌ ERRO!")
    print(texto)
    print("==============================")

    time.sleep(3)  # espera 3 segundos

    limpar_terminal()


# -------------------------
# Cadastro de tarefa
# -------------------------
def cadastrar_tarefa():

    print("\n===== CADASTRAR TAREFA =====")


    descricao = input("Descrição: ")
    data = input("Data (dd/mm/aaaa): ")
    hora_inicio = input("Hora de início: ")
    hora_termino = input("Hora de término: ")


    if descricao == "":
        mensagem_erro("A descrição não pode estar vazia.")
        return


    if data == "":
        mensagem_erro("A data não pode estar vazia.")
        return


    if hora_inicio == "" or hora_termino == "":
        mensagem_erro("Informe os horários corretamente.")
        return



    tarefa = {

        "descricao": descricao,
        "data": data,
        "inicio": hora_inicio,
        "termino": hora_termino

    }


    tarefas.append(tarefa)


    mensagem_sucesso("Tarefa cadastrada com sucesso!")


# -------------------------
# Listar tarefas
# -------------------------
def listar_tarefas():

    print("\n===== LISTA DE TAREFAS =====")

    if len(tarefas) == 0:
        mensagem_erro("Nenhuma tarefa cadastrada.")
        return

    for i in range(len(tarefas)):

        print(f"\nTarefa {i + 1}")
        print(f"Descrição : {tarefas[i]['descricao']}")
        print(f"Data       : {tarefas[i]['data']}")
        print(f"Início     : {tarefas[i]['inicio']}")
        print(f"Término    : {tarefas[i]['termino']}")


# -------------------------
# Remover tarefa
# -------------------------
def remover_tarefa():

    listar_tarefas()

    try:
   
        numero = int(input("\nDigite o número da tarefa para remover: "))

        if numero >= 1 and numero <= len(tarefas): 
            tarefas.pop(numero - 1)
            mensagem_sucesso("Tarefa removida!")
        else:
            mensagem_erro("Tarefa não encontrada!")

    except:

        mensagem_erro("Digite apenas números.")
        return


# -------------------------
# Pesquisar tarefa
# -------------------------
def pesquisar_tarefa():

    palavra = input("\nDigite uma palavra da descrição: ")

    encontrou = False

    print("\n===== RESULTADO =====")

    for tarefa in tarefas:

        if palavra.lower() in tarefa["descricao"].lower():

            print("----------------------------")
            print("Descrição :", tarefa["descricao"])
            print("Data      :", tarefa["data"])
            print("Início    :", tarefa["inicio"])
            print("Término   :", tarefa["termino"])

            encontrou = True

    if encontrou == False:
        print("Nenhuma tarefa encontrada.")


# -------------------------
# Menu
# -------------------------
def menu():

    while True:

        print("\n==============================")
        print("      AGENDADOR DE TAREFAS")
        print("==============================")
        print("1 - Cadastrar tarefa")
        print("2 - Listar tarefas")
        print("3 - Pesquisar tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")


        opcao = input("\nEscolha uma opção: ")



        if opcao == "1":

            limpar_terminal()
            cadastrar_tarefa()


        elif opcao == "2":

            limpar_terminal()
            listar_tarefas()

            time.sleep(6)
            limpar_terminal()


        elif opcao == "3":

            limpar_terminal()
            pesquisar_tarefa()

            time.sleep(3)
            limpar_terminal()


        elif opcao == "4":

            limpar_terminal()
            remover_tarefa()


        elif opcao == "5":

            limpar_terminal()
            print("\nPrograma encerrado!")
            time.sleep(2)
            break


        else:

            mensagem_erro("Opção inválida!")


# Programa principal
menu()