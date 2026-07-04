# Lista onde vamos guardar todos os funcionários
funcionarios = []


# Repetição para cadastrar 10 funcionários
for i in range(10):

    print("\nCadastro do funcionário", i + 1)

    # Pedindo informações ao usuário
    nome = input("Digite o nome: ")
    cargo = input("Digite o cargo: ")
    salario = float(input("Digite o salário: "))


    # Criando um dicionário para guardar os dados do funcionário
    funcionario = {
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    }


    # Adicionando o funcionário na lista
    funcionarios.append(funcionario)


# Mostrando todos os funcionários cadastrados
print("\n--- Funcionários cadastrados ---")


for funcionario in funcionarios:

    print("\nNome:", funcionario["nome"])
    print("Cargo:", funcionario["cargo"])
    print("Salário: R$", funcionario["salario"])