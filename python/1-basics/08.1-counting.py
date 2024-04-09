def count_enemies(enemy_names):
    kind = {}

    for enemy in enemy_names:
        # if the enemy already exists in the dict        
        if enemy in kind:
            # adds 1 to the current dict value for that key
            count = kind[enemy] + 1
        else:
            count = 1
        # update dictionary
        kind[enemy] = count

    return kind

def main(a):
    func = count_enemies(a)
    print(func)

# ------------------------------------------------

# jackal: 6, kobold: 3, soldier: 3, gremlin: 1
enemies = [
    "jackal",
    "kobold",
    "jackal",
    "kobold",
    "soldier",
    "kobold",
    "soldier",
    "soldier",
    "jackal",
    "jackal",
    "gremlin",
    "jackal",
    "jackal",
]

main(enemies)
