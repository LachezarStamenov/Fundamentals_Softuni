num_of_heroes = int(input())

heroes = dict()
max_hp = 100
max_mp = 200

for i in range(0, num_of_heroes):
    hero_name, hit_points, mana_points = input().split()
    heroes[hero_name] = {'hit_points': int(hit_points), 'mana_points': int(mana_points)}

data = input()

while not data == 'End':
    current_data = data.split(' - ')
    action = current_data[0]
    hero_name = current_data[1]

    if action == 'CastSpell':
        mp_needed = int(current_data[2])
        spell_name = current_data[3]
        if heroes[hero_name]['mana_points'] >= mp_needed:
            heroes[hero_name]['mana_points'] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mana_points']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif action == 'TakeDamage':
        damage = int(current_data[2])
        attacker = current_data[3]
        heroes[hero_name]['hit_points'] -= damage
        if heroes[hero_name]['hit_points'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hit_points']} "
                  f"HP left!")
        else:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif action == 'Recharge':
        amount = int(current_data[2])
        heroes[hero_name]['mana_points'] += amount
        if heroes[hero_name]['mana_points'] > 200:
            recovered_amount = amount - abs(200 - heroes[hero_name]['mana_points'])
            heroes[hero_name]['mana_points'] = 200
            print(f"{hero_name} recharged for {recovered_amount} MP!")
        else:
            print(f"{hero_name} recharged for {amount} MP!")
    elif action == 'Heal':
        amount = int(current_data[2])
        heroes[hero_name]['hit_points'] += amount
        if heroes[hero_name]['hit_points'] > 100:
            recovered_amount = amount - abs(100-heroes[hero_name]['hit_points'])
            heroes[hero_name]['hit_points'] = 100
            print(f"{hero_name} healed for {recovered_amount} HP!")
        else:
            print(f"{hero_name} healed for {amount} HP!")

    data = input()

for hero_name in heroes:
    print(hero_name)
    print(f"HP: {heroes[hero_name]['hit_points']}")
    print(f"MP: {heroes[hero_name]['mana_points']}")
# for hero_name, stats in heroes.items():
#     current_hp = stats['hit_points']
#     current_mp = stats['mana_points']
#     print(f'{hero_name}\n HP: {current_hp}\n MP: {current_mp}')