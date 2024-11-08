# -*- coding: utf-8 -*-
"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, 
informado um número, ele calcule a sequência de Fibonacci e 
retorne uma mensagem avisando se o número informado pertence ou não a sequência.
"""

def pertence_a_fibonacci(num):
    # Inicializando a sequência de Fibonacci
    fb1, fb2 = 0, 1
    while fb1 < num:
        fb1, fb2 = fb2, fb1 + fb2

    # Verificando se o número pertence à sequência
    return fb1 == num

def main():
    # Recebe o número informado pelo usuário
    try:
        numero = int(input("Informe um número: "))

        # Verifica se o número pertence à sequência de Fibonacci
        if pertence_a_fibonacci(numero):
            print(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {numero} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Por favor, insira um número válido.")
# Só, permite a execução caso o script seja executado diretamente.
if __name__ == "__main__":
    main()