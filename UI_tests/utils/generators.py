import random
import string


def gen_random_string(length: int, str_type: str) -> str:
    characters = []
    if str_type == 'd':
        # Строка состоит из чисел
        characters = string.digits
    elif str_type == 'l':
        # Строка состоит из букв всех регистров
        characters = string.ascii_letters
    elif str_type == 'm':
        # Строка состоит из букв всех регистров и чисел
        characters = string.ascii_letters + string.digits
    else:
        raise ValueError("Invalid str_type. Use 'n' for numbers, 'l' for letters, or 'm' for mixed.")

    return ''.join(random.choice(characters) for _ in range(length))


def gen_random_email() -> str:
    domain = f"{gen_random_string(3, 'l')}.{gen_random_string(3, 'l')}"
    local_part = gen_random_string(10, 'm')

    return f"{local_part}@{domain}"


def gen_random_number(length: int) -> int:
    if length <= 0:
        raise ValueError("Length must be a positive integer")

    first_digit = random.randint(1, 9)
    other_digits = [random.randint(0, 9) for _ in range(length - 1)]
    random_number = int(str(first_digit) + ''.join(map(str, other_digits)))

    return random_number
