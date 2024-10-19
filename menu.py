def display_menu(user_manager, user, user_type):
    if user_type == 'administrador':
        admin_menu(user_manager)
    elif user_type == 'professor':
        professor_menu()
    elif user_type == 'aluno':
        student_menu()
    else:
        print("Tipo de usuário inválido.")

def admin_menu(user_manager):
    while True:
        print("\n=== Menu do Administrador ===")
        print("1. Adicionar Professor")
        print("2. Adicionar Aluno")
        print("3. Excluir Usuário")
        print("4. Exibir Usuários")
        print("5. Cadastrar Cursos")
        print("6. Sair do Menu")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            user_manager.add_professor()
        elif choice == '2':
            user_manager.add_student()
        elif choice == '3':
            user_manager.delete_user()
        elif choice == '4':
            user_manager.display_users()
        elif choice == '5':
            print("Cadastro de cursos ainda não implementado.")
        elif choice == '6':
            print("Saindo do menu.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def professor_menu():
    while True:
        print("\n=== Menu do Professor ===")
        print("1. Inserir Notas")
        print("2. Inserir Faltas")
        print("3. Exibir Cursos")
        print("4. Sair do Menu")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            print("Inserção de notas ainda não implementada.")
        elif choice == '2':
            print("Inserção de faltas ainda não implementada.")
        elif choice == '3':
            print("Exibição de cursos ainda não implementada.")
        elif choice == '4':
            print("Saindo do menu.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def student_menu():
    while True:
        print("\n=== Menu do Aluno ===")
        print("1. Exibir Notas")
        print("2. Exibir Carga Horária")
        print("3. Exibir Faltas")
        print("4. Sair do Menu")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            print("Exibição de notas ainda não implementada.")
        elif choice == '2':
            print("Exibição de carga horária ainda não implementada.")
        elif choice == '3':
            print("Exibição de faltas ainda não implementada.")
        elif choice == '4':
            print("Saindo do menu.")
            break
        else:
            print("Opção inválida. Tente novamente.")
