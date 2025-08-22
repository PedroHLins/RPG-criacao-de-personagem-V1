from Aventura import Aventura
from Personagem import Personagem

def criar_personagem():
    nome = input("Nome do seu personagem: ")
    raca = input("Raça do seu personagem: ")
    classe = input("Classe do seu personagem: ")
    personagem_criado = Personagem(nome, raca, classe)
    return personagem_criado

if __name__ == "__main__":
    personagem = criar_personagem()

    print("Selecione estilo da aventura: ")
    print("\n1 - Estilo Clássico")
    print("2 - Estilo Aventureiro")
    print("3 - Estilo Heróico")

    aventura = input("\n")

    match aventura:
        case "1":
            Aventura.classico(personagem)
            personagem.exibir_personagem()
        case "2":
            Aventura.aventureiro(personagem)
            personagem.exibir_personagem()
        case "3":
            Aventura.heroico(personagem)
            personagem.exibir_personagem()
        case _: print("Selecione uma aventura válida")