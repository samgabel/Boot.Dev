def merge(dict1, dict2):
    game = {}
    for quarter in dict1:
        game[quarter] = dict1[quarter]
    for quarter in dict2:
        game[quarter] = dict2[quarter]
    return game

def total_score(score_dict):
    total = 0
    for score in score_dict:
        total += score_dict[score]
    return total

def main(a, b):
    func1 = merge(a, b)
    func2 = total_score(func1)
    print(func2)

#------------------------------------------------

game_1 = {"first_quarter": 25, "second_quarter": 2}
game_2 = {"third_quarter": 31, "fourth_quarter": 0}

main(game_1, game_2)
