# Exemplo
def saudacao(nome):
    print(f"Olá, {nome}!")

print("\n Chamando a função saudacao:")
saudacao("Rafael")
saudacao("Bob")

# Função com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\nChamando função quadrado:")
resultado_quadrado = quadrado(5)
print("Resultado da funcao:", resultado_quadrado)

# Função com multiplos parametros
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\nChamando a funcao soma:")
numero1 = 20
numero2 = 20
reusltado_soma = soma(numero1, numero2)
print("A soma do numero %s e do numero %s é %s" % (numero1,numero2, reusltado_soma))