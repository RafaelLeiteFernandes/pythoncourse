# Coleção não ordenada de pares chave e valor

# Criando um de exemplo
pessoa = {"nome": "João", "idade":30, "cidade": "São Paulo"}

# Exibindo o exemplo
print("Meu dicionário:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])

# Inserir item ao dicionário
pessoa ["sobrenome"] = "Silva"
print("sobrenome:", pessoa["sobrenome"])

# Atualizar dado do dicionário
pessoa["idade"] = 31
print("idade atualizada:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["sobrenome"]
# print("sobrenome:", pessoa["sobrenome"])

# Método: keys()
chaves = list(pessoa.keys()) # Transforma o dicionário em lista para buscar por index
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])

# Método: values()
valores = list(pessoa.values()) # Transforma o dicionário em lista para buscar por index
print("Valores do dicionário:", valores)
print("Primeiro valor:", valores[0])

# Método: items()
itens =  list(pessoa.items()) # Transforma o dicionário em lista para buscar por index
print("Items do dicionário:", itens)
print("Primeiro iten:", itens[0][1])