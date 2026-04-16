#ciclo principal
while True:
    #dados de entrada
    sensor_de_humidade = 4    
    cato = 2
    planta = 1 
    tempo = 3 #dias sem regar a planta

    #processamento
    if sensor_de_humidade < 4 and tempo >=3 and planta == cato: 
        regar = True

    else:
        regar = False
