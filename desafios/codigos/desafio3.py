import re

def validar_numero_telefone(numero):
    # Expressão regular para validar o formato (XX) 9XXXX-XXXX
    padrao = r'^\(\d{2}\) 9\d{4}-\d{4}$'
    
    # Verificar se o número corresponde ao padrão
    if re.match(padrao, numero):
        return True
    else:
        return False
    
def imprimir_mensagem(numero):
    if validar_numero_telefone(numero):
        return "Número de telefone válido."
    return "Número de telefone inválido."
    
numero = input()
print(imprimir_mensagem(numero))
