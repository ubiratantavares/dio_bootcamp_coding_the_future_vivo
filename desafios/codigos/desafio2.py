def get_itens(total):
    itens = []
    for _ in range(0, total):
        itens.append(input())
    return itens
# Le os itens dos equipamentositens = 
# Le os itens dos equipamentos
itens = get_itens(3)

# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    print(f"- {item}")
