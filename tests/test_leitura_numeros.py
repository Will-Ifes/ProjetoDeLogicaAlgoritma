from logica.leitura_numeros import ler_ate_zero


def executar(entradas):
    fila = iter(entradas)
    mensagens = []
    numeros = ler_ate_zero(ler=lambda _: next(fila), escrever=mensagens.append)
    return numeros, mensagens


def test_para_imediatamente_com_zero():
    assert executar(["0"]) == ([], [])


def test_acumula_numeros_ate_zero():
    numeros, mensagens = executar(["7", " -3 ", "0"])
    assert numeros == [7, -3]
    assert mensagens == ["Número digitado: 7", "Número digitado: -3"]


def test_ignora_entrada_invalida_e_continua():
    numeros, mensagens = executar(["abc", "", "4", "0"])
    assert numeros == [4]
    assert "'abc' não é um número inteiro. Tente de novo." in mensagens


def test_zero_com_espacos_tambem_encerra():
    assert executar(["5", " 0 "])[0] == [5]
