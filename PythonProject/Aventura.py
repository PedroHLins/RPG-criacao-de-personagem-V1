from Dado import Dado

class Aventura:
    @staticmethod
    def classico(personagem):
        for key in personagem.atributos.keys():
            resultado = sum(Dado.rolar3d6())
            personagem.atributos[key] = resultado

    @staticmethod
    def aventureiro(personagem):
        valores_disponiveis = []
        atributos_disponiveis = list(personagem.atributos.keys())
        for i in range(6):
            resultado = sum(Dado.rolar3d6())
            valores_disponiveis.append(resultado)

        for j in range(len(personagem.atributos)):

            print("\n<<Atributos disponíveis>>\n")
            for i, v in enumerate(atributos_disponiveis, start=1):
                print(f"{i}. {v}")

            print("\n<<Valores disponíveis>>\n")
            for i, v in enumerate(valores_disponiveis, start=1):
                print(f"{i}. {v}")

            atributo = int(input("\nEscolha atributo pelo numero: ")) - 1
            valor = int(input("Escolha valor pelo numero: ")) - 1

            atributo_escolhido = atributos_disponiveis.pop(atributo)
            valor_escolhido = valores_disponiveis.pop(valor)
            personagem.atributos[atributo_escolhido] = valor_escolhido

    @staticmethod
    def heroico(personagem):
        valores_disponiveis = []
        atributos_disponiveis = list(personagem.atributos.keys())
        for i in range(6):
            dados_list = Dado.rolar4d6()
            dado_menor = min(dados_list)
            dados_list.remove(dado_menor)
            resultado = sum(dados_list)
            valores_disponiveis.append(resultado)

        for j in range(len(personagem.atributos)):

            print("\n<<Atributos disponíveis>>\n")
            for i, v in enumerate(atributos_disponiveis, start=1):
                print(f"{i}. {v}")

            print("\n<<Valores disponíveis>>\n")
            for i, v in enumerate(valores_disponiveis, start=1):
                print(f"{i}. {v}")

            atributo = int(input("\nEscolha atributo pelo numero: ")) - 1
            valor = int(input("Escolha valor pelo numero: ")) - 1

            atributo_escolhido = atributos_disponiveis.pop(atributo)
            valor_escolhido = valores_disponiveis.pop(valor)
            personagem.atributos[atributo_escolhido] = valor_escolhido
