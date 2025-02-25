"""
    Vamos criar uma estrutura para cadastrar os dados
    das pessoas que serao armazenadas em uma lista os dados
    que estarao dentro de um map, cpf, nome, telefone,
    data nascimento, para isso teremos funcoes para adicionar,
    procurar,listar e excluir.
"""
import tkinter

# criar uma lista de pessoas vazia
pessoas = []


# funcao usada para adicionar o map na lista
def adicionar():
    cpf = input('Digite o CPF: ')
    nome = input('Digite o Nome: ')
    telefone = input('Digite o Telefone: ')
    data_nascimento = input('Digite o Data de Nascimento:(DD/MM/YYYY): ')
    # add o map na list
    pessoas.append({'cpf': cpf,
                    'nome': nome,
                    'telefone': telefone,
                    'data_nascimento': data_nascimento})

# funcao para procurar a pessoa pelo cpf
def fynd_by_cpf():
    cpf = input('Informe o CPF a procurar: ')
    for pessoa in pessoas:
        if pessoa['cpf'] == cpf:
            print_pessoa(pessoa)
            return
    print("CPF nao exéste")
#funcao para imprimir os dados da pessoa
def print_pessoa(pessoa):
    #Deve imprimir da seguinte froma
    #Nome - CPF: XXXXX - Telefone: XX XXXX-XXXX - Data Nascimeto: XX/XX/XXXX
    print(f"{pessoa['nome']} - "
          f"CPF: {pessoa['cpf']} - "
          f"Telefone {pessoa['telefone']} - "
          f"Data Nascimento: {pessoa['data_nascimento']}")

    # fazer a funcao para imprimir a lista na seguinte forma
    #vai dar 3 linhas e nao pode usar print
    # NOME - CPF: XXXXXXX - Telefone: XX XXXX_XXXX _ Data Nascimento: XX/XX/XXXX
def listar():
    for pessoa in pessoas:
        print_pessoa(pessoa)

def excluir():
    cpf = input('Digite o CPF: ')
    for pessoa in pessoas:
        if pessoa['cpf'] == cpf:
            pessoas.remove(pessoa)
            print(f"{pessoa['nome']} removida com sucesso!")
            return
    tkinter.messagebox.showinfo(message="CPF nao existe!",
                                title= "Aviso")

if __name__== '__main__':
    print("Informe os dados da primeira pessoa")
    adicionar()
    print("Informe os dados da segunda pessoa")
    adicionar()
    print("Procurar por cpf")
    fynd_by_cpf()
    print("Listando 1")
    listar()
    print("Excluir por cpf")
    excluir()
    print("Listando2")
    listar()

