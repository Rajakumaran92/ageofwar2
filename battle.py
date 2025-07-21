from itertools import permutations


advantage = {
    "Militia": ["Spearmen", "LightCavalry"],
    "Spearmen": ["LightCavalry", "HeavyCavalry"],
    "LightCavalry": ["FootArcher", "CavalryArcher"],
    "HeavyCavalry": ["Militia", "FootArcher", "LightCavalry"],
    "CavalryArcher": ["Spearmen", "HeavyCavalry"],
    "FootArcher": ["Militia", "CavalryArcher"]
}

def read_platoons(platoon_str):
    platoons = []
    for item in platoon_str.strip().split(";"):
        unit, count = item.split("#")
        platoons.append((unit.strip(), int(count)))
    return platoons

def battle_result(my_class, my_count, enemy_class, enemy_count):
    
    if enemy_class in advantage.get(my_class, []):
        my_effective = my_count * 2
        enemy_effective = enemy_count
    elif my_class in advantage.get(enemy_class, []):
        my_effective = my_count
        enemy_effective = enemy_count * 2
    else:
        my_effective = my_count
        enemy_effective = enemy_count
    
    if my_effective > enemy_effective:
        return "win"
    elif my_effective == enemy_effective:
        return "draw"
    else:
        return "lose"

def find_winning_order(my_platoons, opponent_platoons):
    for perm in permutations(my_platoons):
        wins = 0
        for i in range(5):
            result = battle_result(perm[i][0], perm[i][1], opponent_platoons[i][0], opponent_platoons[i][1])
            if result == "win":
                wins += 1
        if wins >= 3:
            return perm
    return None


my_input = input().strip()
opponent_input = input().strip()


my_platoons = read_platoons(my_input)
opponent_platoons = read_platoons(opponent_input)

result = find_winning_order(my_platoons, opponent_platoons)

if result:
    print(";".join([f"{cls}#{count}" for cls, count in result]))
else:
    print("There is no chance of winning")
