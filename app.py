# Simone Araujo - Técnico em Desenvolvimento de Sistemas
 # Trabalho: Classificação de Consumo de Água
print("="*50)
print("        SISTEMA DE CLASSIFICAÇÃO DE CONSUMO")
print("="*50)
 # Entrada de dados
nome = input("Digite o nome do morador: ")
consumo = float(input("Digite o consumo mensal de água em m³: "))
 # Classificação do consumo
if consumo <= 5:
     categoria = "Baixo Consumo"
     mensagem = "Parabéns! Você está consumindo de forma consciente."
elif consumo <= 10:
     categoria = "Consumo Moderado"
     mensagem = "Atenção! Tente reduzir o consumo para economizar recursos."
elif consumo <= 20:
     categoria = "Alto Consumo"
     mensagem = "Alerta! O consumo está elevado. Revise o uso da água."
else:
     categoria = "Consumo Excessivo"
     mensagem = "URGENTE! Consumo muito alto. Economize água imediatamente!"
 # Exibição dos resultados
print("\n" + "-" * 50)
print(f"Morador: {nome}")
print(f"Consumo registrado: {consumo} m³")
print(f"Classificação: {categoria}")
print(f"Observação: {mensagem}")
print("-" * 50)
print("\n💧 Água é vida. Preserve e economize! 💧")