import json
import os
import sys


class TerapiaGuiada:
    def __init__(self):
        self.banco_de_dados = {"usuarios": {}}

    def exibir_menu(self):
        print("")
        print("Seja bem-vindo!")
        print("=== Menu Terapia Guiada ===")
        print("1. Conteúdo")
        print("2. Sobre Nós")
        print("3. O que é")
        print("4. Login")
        print("5. Sair")

    def conteudo(self):
        while True:
            os.system('cls')
            print("")
            print("=== Conteúdo ===")
            print("1. Dependência")
            print("2. Depressão")
            print("3. Ansiedade")

            opcao = input("Escolha uma opção (1-3) ou 'v' para voltar: ")
            if opcao == "1":
                self.dependencia()
            elif opcao == "2" or opcao == "3":
                self.depressao_ansiedade(opcao)
            elif opcao == "v":
                break
            else:
                print("")
                print("Opção inválida!")

    def dependencia(self):
        while True:
            print("")
            print("=== Dependência ===")
            print("1. Cigarro/Tabaco")
            print("2. Bebidas")
            print("3. Drogas")
            print("4. Jogos")

            opcao = input("Escolha uma opção (1-4) ou 'v' para voltar: ")
            if opcao in ["1", "2", "3", "4"]:
                if opcao == "1":
                    os.system('cls')
                    self.pagina_solucao_vicio()
                elif opcao == "2":
                    os.system('cls')
                    self.pagina_solucao_vicio()
                elif opcao == "3":
                    os.system('cls')
                    self.pagina_solucao_vicio()
                elif opcao == "4":
                    os.system('cls')
                    self.pagina_solucao_vicio()
            elif opcao == "v":
                break
            else:
                print("")
                print("Opção inválida!")



    def depressao_ansiedade(self, opcao):
        while True:
            print("")
            print(f"=== { 'Depressão' if opcao == '2' else 'Ansiedade' } ===")
            print("1. Atividades")
            print("2. Meditação")
            print("3. Dicas")
            print("4. Grupo de Apoio")

            opcao = input("Escolha uma opção (1-4) ou 'v' para voltar: ")
            if opcao in ["1", "2", "3", "4"]:
                if opcao == "1":
                    os.system('cls')
                    self.pagina_atividades()
                elif opcao == "2":
                    os.system('cls')
                    self.pagina_meditacao()
                elif opcao == "3":
                    os.system('cls')
                    self.pagina_dicas()
                elif opcao == "4":
                    os.system('cls')
                    self.pagina_apoio()
            elif opcao == "v":
                break
            else:
                print("")
                print("Opção inválida!")



    def pagina_solucao_vicio(self):
        print(" ")
        print("=== 10 motivos de porquê você deve parar com esse vício: ===")
        print(" ")
        print("""1. Lorem ipsum dolor sit amet.
2. Lorem ipsum dolor sit amet.
3. Lorem ipsum dolor sit amet.
4. Lorem ipsum dolor sit amet.
5. Lorem ipsum dolor sit amet.
6. Lorem ipsum dolor sit amet.
7. Lorem ipsum dolor sit amet.
8. Lorem ipsum dolor sit amet.
9. Lorem ipsum dolor sit amet. 
10. Lorem ipsum dolor sit amet.
 """)
        print("")
  
        print("=== Como saber se você é um dependente? ===")
        print("Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sunt earum qui adipisicing elit. Sunt earum qui facilis recusandae ab fuga alias dolores reiciendis nulla similique!")

        print(" ")

        print("=== Como parar? ===")
        print("Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sunt earum qui adipisicing elit. Sunt earum qui facilis recusandae ab fuga alias dolores reiciendis nulla similique!")

        print(" ")

        print("=== O que deve ser feito: ===")
        print("""1. Lorem ipsum dolor sit amet consectetur.
2. Lorem ipsum dolor sit amet consectetur.
3. Lorem ipsum dolor sit amet consectetur.
4. Lorem ipsum dolor sit amet consectetur.
5. Lorem ipsum dolor sit amet consectetur.""")
  
        print(" ")

        print("=== O que não deve ser feito: ===")
        print("""1. Lorem ipsum dolor sit amet consectetur.
2. Lorem ipsum dolor sit amet consectetur.
3. Lorem ipsum dolor sit amet consectetur.
4. Lorem ipsum dolor sit amet consectetur. 
5. Lorem ipsum dolor sit amet consectetur. """)
  
        print(" ")

        print("=== Se você precisa de uma ajuda, entre em contato com um de nossos profissionais: ===")
        print(" ")
        print(""" (11)91234-5678
(12)99876-5432
(11)9988-7766 """)
        print(" ")






    def pagina_atividades(self):
        print(" ")
        print("=== Como controlar: ===")
        print(" ")
        print("== Atividades físicas importantes para o corpo: ==")
        print(" ")
        print("= 1. Jogar futebol =")
        print("Por que é importante?")
        print("Lorem ipsum dolor, sit amet consectetur adipisicing elit. Sit, deleniti.")
        print("")
        print("Como fazer?")
        print("Lorem ipsum dolor, sit amet consectetur adipisicing elit. Sit, deleniti.")

        print("")

        print("= 2. Jogar vôlei =")
        print("Por que é importante?")
        print("Lorem ipsum dolor, sit amet consectetur adipisicing elit. Sit, deleniti.")
        print("")
        print("Como fazer?")
        print("Lorem ipsum dolor, sit amet consectetur adipisicing elit. Sit, deleniti.")

        print("")

        print("= 3. Jogar basquete =")
        print("Por que é importante?")
        print("Lorem ipsum dolor, sit amet consectetur adipisicing elit. Sit, deleniti.")
        print("")
        print("Como fazer?")
        print("Lorem ipsum dolor, sit amet consectetur adipisicing elit. Sit, deleniti.")

        print("")





    def pagina_meditacao(self):
        print("")
        print("=== Meditação ===")
        print("")
        print("== Para que serve? ==")
        print("Lorem ipsum dolor adipisicing elit. Vitae exercitationem asperiores veritatis blanditiis, dolor pariatur minima beatae atque.")

        print("")




    def pagina_dicas(self):
        print("")
        print("=== Como se controlar? ===")
        print(""" 1. Lorem ipsum dolor sit amet.
2. Lorem ipsum dolor sit amet.
3. Lorem ipsum dolor sit amet.
4. Lorem ipsum dolor sit amet.
5. Lorem ipsum dolor sit amet. """)
  
        print("")
        print("=== Um conhecido meu tem, o que eu devo fazer? ===")
        print(""" 1. Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae.
2. Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae.
3. Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae.
4. Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae.
5. Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae. """)
  
        print("")
        print("=== O que eu não devo fazer? ===")
        print(""" 1. Lorem, ipsum dolor.
2. Lorem, ipsum dolor.
3. Lorem, ipsum dolor.
4. Lorem, ipsum dolor.
5. Lorem, ipsum dolor.""")

        print("")




    def pagina_apoio(self):
        print("")
        print("=== Grupos de apoio: ===")
        print("== Por que você deve participar de um grupo de apoio? ==")
        print("Lorem ipsum dolor sit amet consectetur adipisicing elit. Nobis omnis quae ipsam reiciendio libero voluptatum fugiat. Invsum sed.")

        print("")
        print("Se você ainda não tem um, entre em contato com um de nossos parceiros:")
        print("""Instituto grupo de apoio SP:
(11)9977-8866

Instituto grupo de apoio RJ:
(21)9977-5566""")
        print("")





    def sobre_nos(self):
        print("")
        print("=== Sobre nós ===")
        print("Na Terapia Guiada, fundada em 2023, abraçamos uma visão holística da saúde mental. Nosso propósito é oferecer suporte e orientação àqueles que enfrentam desafios como vícios, depressão e ansiedade. Com uma abordagem inovadora, combinamos técnicas terapêuticas avançadas com compaixão, criando um ambiente acolhedor para a cura.")
    
    def oq_e(self):
        print("")
        print("=== O que é ===")
        print("Nosso projeto de terapia guiada é uma plataforma inovadora que oferece suporte emocional personalizado para indivíduos lidando com vícios, dependências, depressão e ansiedade. Lançado em 2023, buscamos melhorar vidas por meio de terapias guiadas acessíveis e adaptadas às necessidades específicas de cada pessoa.")

    def salvar_banco_dados(self):
        with open("banco_dados.json", "w") as arquivo:
            json.dump(self.banco_de_dados, arquivo)

    def carregar_banco_dados(self):
        try:
            with open("banco_dados.json", "r") as arquivo:
                self.banco_de_dados = json.load(arquivo)
        except FileNotFoundError:
            pass

    def executar(self):
        self.carregar_banco_dados()

        while True:
            self.exibir_menu()
            opcao = input("Escolha uma opção (1-5): ")

            if opcao == "1":
                self.conteudo()
            elif opcao == "2":
                os.system('cls')
                self.sobre_nos()
            elif opcao == "3":
                os.system('cls')
                self.oq_e()
            elif opcao == "4":
                os.system('cls')
                self.login()
            elif opcao == "5":
                print("Saindo do sistema.")
                self.salvar_banco_dados()
                break
            else:
                print("")
                print("Opção inválida!")

    def registrar_usuario(self):
        self.carregar_banco_dados()
        
        print("")
        nome_usuario = input("Digite um nome de usuário: ")
        senha = input("Digite uma senha: ")
        if nome_usuario not in self.banco_de_dados["usuarios"]:
            self.banco_de_dados["usuarios"][nome_usuario] = senha
            print("")
            print("Usuário registrado com sucesso!")
            self.salvar_banco_dados()
        else:
            print("")
            print("Nome de usuário já existe. Escolha outro.")


    def login(self):
        print("")
        print("1. Fazer Login")
        print("2. Registrar Novo Usuário")
        opcao = input("Escolha uma opção (1-2) ou 'v' para voltar: ")

        if opcao == "1":
            print("")
            nome_usuario = input("Digite seu nome de usuário: ")
            senha = input("Digite sua senha: ")

            if nome_usuario in self.banco_de_dados["usuarios"] and self.banco_de_dados["usuarios"][nome_usuario] == senha:
                print("")
                print("Login bem-sucedido!")
            else:
                print("")
                print("Usuário ou senha incorretos.")
        elif opcao == "2":
            self.registrar_usuario()
        elif opcao == "v":
            print("")
            sys.exit
        else:
            print("Opção inválida!")



sistema = TerapiaGuiada()
sistema.executar()
