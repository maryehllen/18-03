def exibir_menu():
    print("bem-vindo ao menu de cadastro")
    print("1 - novo cadastro")
    print("2 - ver cadastro")
    print("3 - sair")
    print("-----------------------------------------------------------")

def cadastrar_pessoa(cadastros):
    nome = input("nome:")
    idade = input("idade:")
    turma = input("turma:")
    curso = input("curso:")
    cadastros.append({"nome": nome, "idade": idade, "turma": turma, "curso": curso})
