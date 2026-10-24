def add(a, b):
    """Вернуть сумму двух чисел."""
    return a + b


def is_even(number):
    """Проверить, является ли число чётным."""
    return number % 2 == 0


if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("4 чётное:", is_even(4))
