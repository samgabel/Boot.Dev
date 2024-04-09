def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    current_lead = None

    for enemy in enemies_dict:
        if enemies_dict[enemy] > max_so_far:
            max_so_far = enemies_dict[enemy]
            current_lead = enemy

    return current_lead



def main(a):
    func = get_most_common_enemy(a)
    print(func)

#--------------------------------------------------------------------------------

enemies = {
    "jackal": 5,
    "kobold": 3,
    "soldier": 10,
    "gremlin": 5,
    "dragon": 20
}

main(enemies)
