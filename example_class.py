class Pokemon:
    hp = 0
    speed = 0
    type = ""
    name = ""

    def __init__(self, hp : int, speed : int, type : str, name : str):
        self.hp = hp
        self.speed = speed
        self.type = type
        self.name = name
        print(f"{self.name} est apparu")

    def attack(self):
        self.hp = self.hp - 1

    def getName(self) -> str:
        return self.name


class Pokedex:
    listPokemon = []

    def __init__(self) -> None:
        pass

    def add(self, p :Pokemon):
        self.listPokemon.append(p)

    def remove(self, name : str):
        for pokemon in self.listPokemon:
            if pokemon.name == name:
                self.listPokemon.remove(pokemon)


class Trainer:
    name = ""
    age = 0
    pokeballs = 0
    pokedex = any

    def __init__(self, name : str, age : int, pokeballs : int, pokedex : Pokedex):
        self.name = name
        self.age = age
        self.pokeballs = pokeballs


    def capture(self, p : Pokemon) -> str:
        if self.pokeballs > 0:
            self.pokeballs = self.pokeballs - 1
            self.pokedex.add(p)
            return f"{self.name} a réussi à capturer {p.name}"
        return f"{self.name} n'as plus de pokeballs"


Sacha = Trainer("Sacha", 14, 3)
Regis = Trainer("Régis", 15, 5)

Pikachu = Pokemon(20, 100, "Electric", "Pikachu")

print(Sacha.capture(Pikachu))


