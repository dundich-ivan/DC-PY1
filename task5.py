from random import sample
from string import ascii_letters, digits


def get_random_password() -> str:
    return ''.join(sample([symbol for symbol in (ascii_letters + digits)], 8))


print(get_random_password())
