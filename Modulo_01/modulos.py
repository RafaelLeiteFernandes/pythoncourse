print("Exemplo de importação de um módulo padrão:")
# import math
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"A raiz de 25 é {raiz_quadrada}")
###################################################################################
print("\nExemplo de criação e utilização de um módulo personalizado")
# import meu_modulo
from meu_modulo import saudacao, dobro


mensagem = saudacao("Rafael")
resultado_dobro = dobro(10)

print(mensagem)
print(resultado_dobro)