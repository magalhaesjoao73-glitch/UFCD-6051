#ciclo principal
while True:

    #dados de entrada
    sensor_de_luz1 = 100
    sensor_de_luz2 = 100
    sensor_de_luz3 = 100
    sensor_de_luz4 = 100
    
    #processamento

    if sensor_de_luz1 < 100 or sensor_de_luz2 < 100 or sensor_de_luz3 < 100 or sensor_de_luz4 < 40:
        aumentar_intensidade_luz = True

    else:
        aumentar_intensidade_luz = False