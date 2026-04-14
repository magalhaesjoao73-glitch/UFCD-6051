#ciclo principal
while True:

#dados de entrada
    interroptor1= False
    interroptor2= True

# processamento
    if ( not interroptor1 and  interroptor2) or ( interroptor1 and not interroptor2):

        ligar_luz= True

    else:
        ligar_luz = False   

        # forma simplificada
    if  interroptor1 ^ interroptor2:
        validar = True
    else:
        validar = False

