
class classeJogador:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    
    def escrever(self, attack):
        print(f"O {self.tipo} atacou usando {attack}")

player = classeJogador("Kevin", 23, "mago")
attack = ""

if player.tipo == "guerreiro":
    attack = "uma espada"
elif player.tipo == "mago":
    attack = "magia"
elif player.tipo == "monge":
    attack = "artes marciais"
elif player.tipo == "ninja":
    attack = "shuriken"

player.escrever(attack)