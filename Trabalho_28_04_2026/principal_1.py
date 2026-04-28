#cria uma estrurtura de dados com os componentes de um quadro eletrico 
###mencionar as especificaçoes 

quadro={
    "corte_geral":{
        "in" : 32,
    },
    "dijuntor1":{
        "in" : 10,

    },
    "dijuntor2":{
        "in" : 16,
    },

    "diferencial":{
        "deltai" : 0.03,
        "in" : 40,  
    },

    "interruptor":{
        "in" : 40,  
    },

    "barramento_terra":{
        "in" : 100,
    },
    "barramento_neutro":{
        "in" : 100,
    },
}

lampadas={
    "potencia" : 40,
    "tensao": 230,
    "quantidade" : 3
}

import minhas_funçoes

corrente_de_cada_lampada = minhas_funçoes.calcular_corrente(lampadas["potencia"], lampadas["tensao"])
print("corrente de cada lampada: ")
corrente_de_todas_lampadas = minhas_funçoes
print("corrente de todas as lampadas: ")

corrente_de_todas_lampadas = corrente_de_cada_lampada * lampadas
corrente_de_todas_lampadas

minhas_funçoes.selecionar_dijuntor(corrente_de_todas_lampadas)