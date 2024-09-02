
id_global = 3320213
lista_funcionarios = []

def cadastrar_funcionario(p_id):
    global lista_funcionarios
    
    #a. Pergunta nome, setor, salario do funcionário;
    print("Menu Cadastrar Funcionario:")
    print("Id do funcionario:", p_id)
    m_nome = input("Qual o nome do funcionario? >>")
    m_setor = input("Qual o setor do funcionario? >>")
    m_salario = None
    while not m_salario:
        m_salario = input("Qual o salario do funcionario? >>")
        try:
            m_salario = int(m_salario)
        except Exception:
            print("Valor Invalido!")
            m_salario = None
            continue
    #b. Armazena o id (este é fornecido via parâmetro da função), nome, setor, salario dentro de um dicionário;
    novo_funcionario = {
            "id": p_id,
            "nome": m_nome,
            "setor": m_setor,
            "salario": m_salario}
    #c. Copiar o dicionário para dentro da lista_funcionarios (utilizar o copy);
    lista_funcionarios.append(novo_funcionario.copy())
    return p_id

def consultar_funcionarios():
    global lista_funcionarios
    escolha_do_menu = None

    #a. Deve-se perguntar qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor / 4. Retornar ao menu):
    print("Menu Consultar Funcionario:")
    while not escolha_do_menu:
        escolha_do_menu= input("""
Menu Principal:
1 - Consultar todos os funcionarios
2 - Consultar funcionario por ID
3 - Consultar funcionario por setor
4 - Retornar
>>""")
        if escolha_do_menu == "4":
            #iv. Se Retornar ao menu, deve-se retornar ao menu principal (return);
            return
        elif escolha_do_menu == "1":
            #i. Se Consultar Todos, apresentar todos os funcionários com todos os seus dados cadastrados;
            for f in lista_funcionarios:
                print("id:", f.get("id"))
                print("nome:", f.get("nome"))
                print("setor:", f.get("setor"))
                print("salario:", f.get("salario"))
        elif escolha_do_menu == "2":
            #ii. Se Consultar por Id, solicitar ao usuário que informe um id, e apresentar o funcionário específico com todos os seus dados cadastrados;
            id_f = None
            while not id_f:
                id_f = input("Qual o ID do funcionario para consulta? >>")
                try:
                    id_f = int(id_f)
                except Exception:
                    print("Valor Invalido!")
                    id_f = None
                    continue
            for f in lista_funcionarios:
                if f.get("id") == id_f:
                    print("id:", f.get("id"))
                    print("nome:", f.get("nome"))
                    print("setor:", f.get("setor"))
                    print("salario:", f.get("salario"))
        elif escolha_do_menu == "3":
            #iii. Se Consultar por Setor, solicitar ao usuário que informe o setor, e apresentar o(s) funcionário(s) do setor com todos os seus dados cadastrados;
            m_setor = input("Qual o setor do funcionario para consulta? >>")
            for f in lista_funcionarios:
                if m_setor in f.get("setor"):
                    print("id:", f.get("id"))
                    print("nome:", f.get("nome"))
                    print("setor:", f.get("setor"))
                    print("salario:", f.get("salario"))
        else:
            #v. Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta D.a.
            print("Opção Invalida!")
        #vi. Enquanto o usuário não escolher a opção 4, o menu consultar funcionários deve se repetir
        escolha_do_menu = None
        continue
    
def remover_funcionario():
    global lista_funcionarios 
    registros_excluido = False
    
    print("Menu Remover Funcionario:")
    while not registros_excluido:
        #a. Deve-se pergunta pelo id do funcionário a ser removido;
        id_f = None
        while not id_f:
            id_f = input("Qual o ID do funcionario para exclusão? >>")
            try:
                id_f = int(id_f)
            except Exception:
                print("Valor Invalido!")
                id_f = None
                continue
        #b. Remover o funcionário da lista_funcionarios;
        for index, funcionário in enumerate(lista_funcionarios):
            if funcionário.get("id") == id_f:
                # evitar iterator invalidation
                del lista_funcionarios[index]
                registros_excluido = True
        #c. Se o id fornecido não for de um funcionário da lista, printar “Id inválido” e repetir a pergunta E.a.
        if not registros_excluido:
            print("Id invalido!")
            registros_excluido = None
            continue

def main():
    # Gerenciamento de funcionários

    # Dados
    global id_global
    escolha_do_menu = None

    print("Bem Vindo ao Estabelecimento do Vinicius Eduardo Carvalho da Cruz de Moura")

    # Rotinas
    while True:
        # Perguntar qual a opção desejada
        while not escolha_do_menu:
            escolha_do_menu= input("""
Menu Principal:
1 - Cadastrar Funcionario
2 - Consultar Funcionarios
3 - Remover Funcionario
4 - Sair
>>""")
        if escolha_do_menu == "4":
            #iv. Se Encerrar Programa, sair do menu (e com isso acabar a execução do código);
            break
        elif escolha_do_menu == "1":
            #i. Se Cadastrar Funcionário, incrementar em um id_global e chamar a função cadastrar_funcionario(id_global);
            id_global += 1
            cadastrar_funcionario(id_global)
        elif escolha_do_menu == "2":
            #ii. Se Consultar Funcionário, chamar função consultar_funcionario ();
            consultar_funcionarios()
        elif escolha_do_menu == "3":
            #iii. Se Remover Funcionário, chamar função remover_funcionario();
            remover_funcionario()
        else:
            #v. Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta F.a.
            print("Opção Invalida!")
        #vi. Enquanto o usuário não escolher a opção 4, o menu deve se repetir.
        escolha_do_menu = None
        continue

if __name__ == '__main__':
    main()
