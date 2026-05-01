def calcular_media(numeros: list[float]) -> float:
    """Calcula a média de uma lista de números e informa aprovação.

    Args:
        numeros: Lista de valores numéricos.

    Returns:
        A média aritmética dos valores fornecidos.

    Raises:
        ValueError: Se a lista estiver vazia.
    """
    if not numeros:
        raise ValueError("A lista de números não pode estar vazia.")

    soma = sum(numeros)
    media = soma / len(numeros)

    if media > 7:
        print("Aprovado")
    else:
        print("Reprovado")

    return media


if __name__ == '__main__':
    valores = [5, 7, 8, 10]
    resultado = calcular_media(valores)
    print("Média:", resultado)
