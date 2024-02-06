# Declarações 

nome_completo = "Rafael Leite"
nome_com_aspas_pular_linha = """ Rafael
Leite """
nome_completo_quebra = " Rafael \
Leite"

nome = "Rafael"
sobrenome = "Leite"

# Formatação
print ("Nome  (1a forma)", nome)
print ("Nome (2a forma)"+ nome)
print ("Nome (3a forma)"+ "Rafael" + "Leite")
print ("Nome (4a forma)", "Rafael" , "Leite")
print ("Nome (5a forma)", nome_com_aspas_pular_linha)
print ("Nome (6a forma)", nome_completo_quebra)
print ("Nome (7a forma) %s" % nome)
print ("Nome (8a forma) %s %s" % (nome, sobrenome))
print(f"Nome (9a forma){nome} {sobrenome}")
print("Nome {} {}". format(nome, sobrenome))
