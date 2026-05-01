# Código original (mal estruturado)
def f(a):
    r = []
    for i in range(len(a)):
        if a[i] % 2 == 0:
            r.append(a[i])
    return r

# Código refatorado (gerado pela IA)
def filter_even_numbers(numbers: list[int]) -> list[int]:
    """Filtra e retorna apenas os números pares de uma lista.

    Args:
        numbers: Lista de números inteiros a ser filtrada.

    Returns:
        Lista contendo apenas os números pares.

    Exemplos:
        >>> filter_even_numbers([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
        >>> filter_even_numbers([1, 3, 5])
        []
    """
    return [number for number in numbers if number % 2 == 0]


if __name__ == '__main__':
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_result = filter_even_numbers(test_numbers)
    print(f"Números originais: {test_numbers}")
    print(f"Números pares: {even_result}")