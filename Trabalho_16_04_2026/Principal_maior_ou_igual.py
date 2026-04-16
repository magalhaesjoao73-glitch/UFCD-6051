#ciclo principal

while True:
    
    #dados de entrada

    sensor_de_pressao = 35

    #pocessamento

    if sensor_de_pressao >= 40:
        ativar_eletrovalvula = True         
    else:           
        ativar_eletrovalvula = False