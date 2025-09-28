import random


def generate_random_product_code() -> int:
    random_code = random.randint(1000, 9999)
    return random_code
