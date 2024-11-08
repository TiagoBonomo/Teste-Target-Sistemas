# -*- coding: utf-8 -*-
 
"""
5) Escreva um programa que inverta os caracteres de um string.
IMPORTANTE:
   a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
   b) Evite usar funções prontas, como, por exemplo, reverse;
"""

# Solicita a entrada da string
texto = input("Digite uma string para inverter: ")

# Inverter a string manualmente
texto_invertido = ""
for i in range(len(texto) - 1, -1, -1):
    texto_invertido += texto[i]

# Exibir o resultado
print("String invertida:", texto_invertido)