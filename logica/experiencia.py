"""Exercício 2: faixas com if/elif/else.

A versão original usava `< 2` e `> 2 and < 5`, então exatamente 2 anos
caía em "sênior". Aqui as faixas são contínuas: [0, 2), [2, 5), [5, ∞).
"""

LIMITE_PLENO = 2
LIMITE_SENIOR = 5


def classificar_experiencia(anos: float) -> str:
    """Retorna o nível didático para os anos de experiência informados."""
    if anos < 0:
        raise ValueError("Anos de experiência não podem ser negativos.")
    if anos < LIMITE_PLENO:
        return "júnior"
    if anos < LIMITE_SENIOR:
        return "pleno"
    return "sênior"


def main() -> None:
    for anos in (0, 1.5, 2, 4, 5, 10):
        print(f"{anos} ano(s) -> nível {classificar_experiencia(anos)}")


if __name__ == "__main__":
    main()
