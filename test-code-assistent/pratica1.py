def is_prime(number: int) -> bool:
    """Verifica se um número inteiro positivo é primo.

    Args:
        number: Valor inteiro a ser testado.

    Returns:
        True se o número for primo, False caso contrário.
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2

    return True


if __name__ == '__main__':
    test_values = [0, 1, 2, 3, 4, 17, 18, 19, 20, 23, 24, 25]
    for value in test_values:
        status = 'primo' if is_prime(value) else 'não primo'
        print(f'{value}: {status}')
