# -*- coding: utf-8 -*-
# Cria uma variável chamada entradaIdade e inicie ela com ''
entradaIdade = ''

# Inicia um loop que continuará enquanto entradaIdade for diferente de '0'
while entradaIdade != '0':
    # Atribui à variável entradaIdade um input do usuário
    entradaIdade = input('Digite um número qualquer ou 0 para sair: ')
    
    # Se entradaIdade não for '0', imprime o número digitado
    if entradaIdade != '0':
        print('Número digitado:', entradaIdade)
