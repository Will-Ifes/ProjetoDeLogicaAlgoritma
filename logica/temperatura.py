"""Exercício 1: decisão simples com if/else."""

LIMITE_CALOR = 30


def classificar_temperatura(graus: float) -> str:
    """Retorna a descrição do dia para a temperatura informada, em °C."""
    if graus < LIMITE_CALOR:
        return "A temperatura hoje está amena."
    return "Hoje está fazendo calor."


def main() -> None:
    for graus in (29, 30, 35):
        print(f"{graus} °C -> {classificar_temperatura(graus)}")


if __name__ == "__main__":
    main()
