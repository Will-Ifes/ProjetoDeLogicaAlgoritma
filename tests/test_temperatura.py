import pytest

from logica.temperatura import classificar_temperatura


@pytest.mark.parametrize(
    ("graus", "esperado"),
    [
        (-5, "A temperatura hoje está amena."),
        (29.9, "A temperatura hoje está amena."),
        (30, "Hoje está fazendo calor."),
        (40, "Hoje está fazendo calor."),
    ],
)
def test_classificar_temperatura(graus, esperado):
    assert classificar_temperatura(graus) == esperado
