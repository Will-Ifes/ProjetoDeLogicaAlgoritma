"""Menu para executar os exercícios: python -m logica"""

from logica import experiencia, leitura_numeros, temperatura

EXERCICIOS = {
    "1": ("Temperatura (if/else)", temperatura.main),
    "2": ("Nível de experiência (if/elif/else)", experiencia.main),
    "3": ("Leitura até zero (while)", leitura_numeros.main),
}


def main() -> None:
    while True:
        print("\nLógica de programação · Python")
        for chave, (titulo, _) in EXERCICIOS.items():
            print(f"  {chave}. {titulo}")
        print("  0. Sair")
        escolha = input("Escolha um exercício: ").strip()
        if escolha == "0":
            return
        if escolha not in EXERCICIOS:
            print("Opção inválida.")
            continue
        print()
        EXERCICIOS[escolha][1]()


if __name__ == "__main__":
    main()
