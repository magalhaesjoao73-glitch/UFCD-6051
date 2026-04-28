def calcular_corrente(potencia, tensao):
    corrente = potencia / tensao
    return corrente

def selecionar_dijuntor(valor):
    if valor < 6:
        print("c6")
    elif valor < 6 and valor < 10:
        print("c10")
    elif valor < 10 and valor < 16:
        print("c16")    
    elif valor < 16 and valor < 20:
        print("c20")
    elif valor < 20 and valor < 25:
        print("c25") 