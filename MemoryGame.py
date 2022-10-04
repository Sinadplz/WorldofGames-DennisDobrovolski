import time
import os


def generate_num(difficulty):
    import random
    random_num = []
    for num in range(difficulty):
        random_num.append(int(random.uniform(1, 101)))
    print(random_num)
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    return random_num


def user_nums(difficulty):
    user_num = []
    print(f"Select {difficulty} numbers please")
    for num in range(difficulty):
        num = user_num.append(int(input("Import a Number: ")))
    return user_num


def equal_list(random_num, user_num):
    random_num.sort()
    user_num.sort()
    os.system('cls' if os.name == 'nt' else 'clear')
    if random_num == user_num:
        return True
    else:
        return False


def play(difficulty):
    random_num = generate_num(difficulty)
    user_num = user_nums(difficulty)
    if equal_list(user_num=user_num, random_num=random_num):
        return True
    else:
        return False
