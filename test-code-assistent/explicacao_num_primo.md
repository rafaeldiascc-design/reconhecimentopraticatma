# Verificação de número primo em Python

Este documento apresenta a implementação da função `is_prime` e uma explicação clara e organizada de cada parte do código.

## Código Python

```python
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
```

## Explicação detalhada

### Definição da função

- `def is_prime(number: int) -> bool:`
  - Declara a função `is_prime` que recebe um parâmetro `number` do tipo inteiro e retorna `True` ou `False`.

### Documentação da função

- `"""Verifica se um número inteiro positivo é primo.`
  - Início da docstring com a descrição do objetivo da função.

- `Args:`
  - Início da seção que descreve os parâmetros.

- `    number: Valor inteiro a ser testado.`
  - Explica qual valor deve ser passado para o parâmetro `number`.

- `Returns:`
  - Início da seção que descreve o valor de retorno.

- `    True se o número for primo, False caso contrário.`
  - Indica o resultado esperado da função.

- `"""`
  - Final da docstring.

### Verificações iniciais

- `if number <= 1:`
  - Verifica se o número é menor ou igual a 1.

- `    return False`
  - Números menores ou iguais a 1 não são primos.

- `if number <= 3:`
  - Verifica se o número é 2 ou 3.

- `    return True`
  - 2 e 3 são primos.

- `if number % 2 == 0:`
  - Verifica se o número é par.

- `    return False`
  - Números pares maiores que 2 não são primos.

### Teste de divisores

- `divisor = 3`
  - Define o primeiro divisor ímpar a ser testado.

- `while divisor * divisor <= number:`
  - Continua testando divisores enquanto o quadrado do divisor for menor ou igual ao número.
  - Isso é suficiente porque, se um número tem um divisor maior que sua raiz quadrada, ele também terá um divisor menor que a raiz.

- `    if number % divisor == 0:`
  - Verifica se o número é divisível pelo divisor atual.

- `        return False`
  - Se encontrar um divisor exato, o número não é primo.

- `    divisor += 2`
  - Avança para o próximo divisor ímpar (3, 5, 7 etc.).
  - Números pares já foram eliminados, então só são testados divisores ímpares.

### Conclusão da função

- `return True`
  - Se nenhum divisor for encontrado até a raiz quadrada, o número é primo.

### Bloco principal

- `if __name__ == '__main__':`
  - Garante que os testes sejam executados apenas quando o arquivo for executado diretamente.

- `test_values = [0, 1, 2, 3, 4, 17, 18, 19, 20, 23, 24, 25]`
  - Lista de valores usados para demonstrar o funcionamento da função.

- `for value in test_values:`
  - Itera sobre cada valor da lista.

- `    status = 'primo' if is_prime(value) else 'não primo'`
  - Usa a função `is_prime` para determinar o status de cada número.

- `    print(f'{value}: {status}')`
  - Exibe o resultado final no console.

## Por que essa versão é otimizada?

- Realiza verificações rápidas para casos especiais (`<= 1`, `<= 3` e números pares).
- Evita testar divisores pares desnecessários.
- Para quando o divisor atinge a raiz quadrada do número, reduzindo o número de testes.
