import string
import random


def get_project_name():
    symbols = string.ascii_letters + string.digits + " " * 10
    return "Проект_" + "".join(
        random.choice(symbols)
        for _ in range(random.randint(1, 20))
    )


def get_project_description():
    symbols = string.ascii_letters + string.digits + " " * 10
    return "Описание_" + "".join(
        random.choice(symbols)
        for _ in range(random.randint(1, 100))
    )