class Personagem:
    atributos = {
        "Forca": 0,
        "Destreza": 0,
        "Constituicao": 0,
        "Inteligencia": 0,
        "Sabedoria": 0,
        "Carisma": 0
    }

    def __init__(self, nome, raca, classe):
        self.nome = nome
        self.raca = raca
        self.classe = classe

    def exibir_personagem(self):
        print("\nNome:", self.nome)
        print("Raça:", self.raca)
        print("Classe:", self.classe)
        for atributo in self.atributos:
            print("{:<12} ".format(atributo), end="")
            for i in range(self.atributos[atributo]):
                print("■", end="")
            print(" (", self.atributos[atributo] ,")", "\n" , end="")