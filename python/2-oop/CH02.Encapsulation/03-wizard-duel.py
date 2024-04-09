class Wizard:
    def cast_fireball(self, target):
        fireball_cost = 20
        if self.__mana < fireball_cost:
            raise Exception(f"{self.name} tries to cast fireball but only has {self.__mana} left")
        else:
            self.__mana -= 20
            target.get_fireballed()
            return f"{self.name} casts fireball at {target.name}"

    # don't touch below this line

    def __init__(self, name):
        self.__mana = 45
        self.__health = 65
        self.name = name

    def get_mana(self):
        return self.__mana

    def get_health(self):
        return self.__health

    def get_fireballed(self):
        fireball_damage = 30
        self.__health -= fireball_damage
        if self.__health <= 0:
            print(f"{self.name} is dead")

    def drink_mana_potion(self):
        self.__mana += 40
        return f"{self.name} drank a potion and now has {self.__mana} mana"


merlin = Wizard("Merlin")
alphonse = Wizard("Alphonse Elrich")

print(
    f"{alphonse.name} vs {merlin.name} who will win",
    f"{alphonse.cast_fireball(merlin)}",
    f"{merlin.name} now has {merlin.get_health()} health",
    f"{merlin.cast_fireball(alphonse)}",
    f"{merlin.cast_fireball(alphonse)} again in rapid fire!!",
    f"{alphonse.name} now has {alphonse.get_health()} health",
    f"{alphonse.name} is backed into a corner and is getting desperate!!",
    f"{alphonse.cast_fireball(merlin)}",
    sep = '\n'
)
try:
    print(f"{alphonse.cast_fireball(merlin)} again in rapid fire!!")
except Exception as e:
    print(f"{e}!!")
print(
    f"{alphonse.drink_mana_potion()}",
    f"{alphonse.cast_fireball(merlin)} using a quick attack!",
    f"{merlin.name} has {merlin.get_health()} health left. He is dead!",
    f"{alphonse.name.upper()} is the WINNER!!",
    sep = '\n'
)
