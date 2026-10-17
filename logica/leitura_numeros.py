"""Exercício 3: repetição com while até uma condição de parada."""

from collections.abc import Callable

SAIDA = "0"


def ler_ate_zero(
    ler: Callable[[str], str] = input,
    escrever: Callable[[str], None] = print,
) -> list[int]:
    """Lê números até receber 0 e devolve os números válidos lidos.

    `ler` e `escrever` são injetáveis para permitir testes sem terminal.
    Entradas que não são números inteiros geram aviso e são ignoradas.
    """
    numeros: list[int] = []
    while True:
        entrada = ler(f"Digite um número inteiro ou {SAIDA} para sair: ").strip()
        if entrada == SAIDA:
            return numeros
        try:
            numero = int(entrada)
        except ValueError:
            escrever(f"'{entrada}' não é um número inteiro. Tente de novo.")
            continue
        numeros.append(numero)
        escrever(f"Número digitado: {numero}")


def main() -> None:
    numeros = ler_ate_zero()
    print(f"Total de números lidos: {len(numeros)}")


if __name__ == "__main__":
    main()
