class UserManager:
    def __init__(self):
        # Armazena usuários no formato {username: {"password": senha, "type": tipo}}
        self.users = {}

    def register_user(self):
        username = input("Digite o nome de usuário: ")
        if username in self.users:
            print("Usuário já existe.")
            return

        password = input("Digite a senha: ")
        user_type = selecionar_usertype() 
        if user_type not in ['administrador', 'professor', 'aluno']:
            print("Tipo de usuário inválido.")
            return

        self.users[username] = {"password": password, "type": user_type}
        print(f"Usuário {user_type} cadastrado com sucesso.")

    def login(self):
        username = input("Digite seu nome de usuário: ")
        password = input("Digite sua senha: ")

        if username in self.users and self.users[username]["password"] == password:
            print(f"Login realizado com sucesso como {self.users[username]['type']}.")
            return username, self.users[username]["type"]
        else:
            print("Nome de usuário ou senha incorretos.")
            return None, None

    def add_professor(self):
        # Função específica para adicionar professores, disponível apenas para administradores.
        print("Adicionar um novo professor.")
        self.register_user()

    def add_student(self):
        # Função específica para adicionar alunos, disponível apenas para administradores.
        print("Adicionar um novo aluno.")
        self.register_user()

    def delete_user(self):
        username = input("Digite o nome de usuário que deseja excluir: ")
        if username in self.users:
            del self.users[username]
            print("Usuário excluído com sucesso.")
        else:
            print("Usuário não encontrado.")

    def display_users(self):
        if not self.users:
            print("Nenhum usuário cadastrado.")
            return

        print("=== Usuários Cadastrados ===")
        for username, info in self.users.items():
            print(f"Usuário: {username} - Tipo: {info['type']}")

def selecionar_usertype():
    print("Selecione o tipo de usuário:")
    print("1 - Admin")
    print("2 - Prof")
    print("3 - aluno")

    while True:
        opcao = input("Digite o número correspondente ao tipo de usuário: ")
        if opcao == '1':
            return 'administrador'
        elif opcao == '2':
            return 'professor'
        elif opcao == '3':
            return 'aluno'
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")