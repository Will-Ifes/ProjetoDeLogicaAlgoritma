# -*- coding: utf-8 -*-
# Cria uma variável chamada tempoExperiencia e inicie ela com o valor 5
tempoExperiencia = 5

# Validar se o valor da variável tempoExperiencia é menor que 2
if tempoExperiencia < 2:
    print('Nível de conhecimento júnior.')
# Validar se o valor da variável tempoExperiencia é maior que 2 e menor que 5
elif tempoExperiencia > 2 and tempoExperiencia < 5:
    print('Nível de conhecimento pleno.')
# Caso contrário, se não for nenhuma das opções anteriores
else:
    print('Nível de conhecimento sênior.')
