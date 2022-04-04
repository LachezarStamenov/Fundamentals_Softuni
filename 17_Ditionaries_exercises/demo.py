import random

random_dict = {}

for i in range (1, 21):
    for num in range(1, 11):
        n = random.randint(-90, 99)

        if i not in random_dict:
            random_dict[i] = []
        random_dict[i].append(n)
        if sum((random_dict[i])) > 0:
            continue
        else:
            del random_dict[i]
            n = random.randint(-90, 99)

            if i not in random_dict:
                random_dict[i] = []
            random_dict[i].append(n)
            if sum(random_dict[i]) > 0:
                continue
            del random_dict[i]
print(random_dict)


