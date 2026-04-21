# calculo de medias

dia1 = 100
dia2 = 500
dia3 = 1000
dia4 = 1500

media = (dia1 + dia2 + dia3 + dia4) / 4
print(media) 

# calculo de dias maus um de cada vez  
testar_numero_de_vendas= dia1 - media


if testar_numero_de_vendas >0:
    print("dia bom")
else:
    print("dia mau")


testar_numero_de_vendas = dia2 - media

if testar_numero_de_vendas >0:
    print("dia bom")
else:
    print("dia mau")


testar_numero_de_vendas= dia3 - media

if testar_numero_de_vendas >0:
    print("dia bom")
else:
    print("dia mau")


testar_numero_de_vendas = dia4 - media

if testar_numero_de_vendas >0:
    print("dia bom")
else:
    print("dia mau")

