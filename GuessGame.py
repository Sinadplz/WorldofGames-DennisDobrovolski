from time import sleep


def gen_num(difficulty):
    import random
    secret_num = int(random.uniform(1, difficulty))
    return secret_num


def user_guess_num(difficulty):
    num = int(input(f"Please select a number between 1 to {difficulty}: "))
    return num


def result(secret_num, num):
    if secret_num == num:
        return True


def play(difficulty):
    secret_num = user_guess_num(difficulty)

    print("A number is being generated..")
    sleep(2)
    print("Your turn, choose a number!")
    sleep(1)
    number = user_guess_num(difficulty)
    if result(secret_number=secret_num, num=number):
        return True
    else:
        return False
