import pytest

from logica.experiencia import classificar_experiencia


@pytest.mark.parametrize(
    ("anos", "esperado"),
    [
        (0, "júnior"),
        (1.9, "júnior"),
        (2, "pleno"),  # caía em "sênior" na versão original
        (4.9, "pleno"),
        (5, "sênior"),
        (20, "sênior"),
    ],
)
def test_faixas_sao_continuas(anos, esperado):
    assert classificar_experiencia(anos) == esperado


def test_rejeita_valor_negativo():
    with pytest.raises(ValueError):
        classificar_experiencia(-1)
