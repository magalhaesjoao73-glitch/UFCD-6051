#ciclo principal

while True:

#dados de entrada

    sensor_porta= False
    sensor_de_comando= True      
# processamento

    if not ((not sensor_porta and not sensor_de_comando) or (sensor_porta and sensor_de_comando)):

        validar= True
    else:
        validar = False   


# forma simplificada
    if  not (sensor_porta ^ sensor_de_comando):
        validar = True
    else:
        validar = False