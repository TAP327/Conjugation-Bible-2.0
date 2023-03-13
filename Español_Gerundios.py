'''''
Gerundios:
    -AR:  -ando
    -ER:  -iendo
    -IR:  -iendo

    Vocal & Fin:
        -AER, -UIR, -EER, -OIR:  -yendo
        TRAER: trayendo     HUIR: huyendo   
        LEER: leyendo       OIR: oyendo

            *No aplica a verbos -GUIR por alguna razón. 

        -EIR: -iendo   
        REIR: riendo        FREIR: friendo

    Stem Changers:
        E-IE: MENTIR: mintiendo     PREFERIR: prefiriendo
        E-I: VESTIR: vistiendo      SEGUIR: siguiendo
        O-UE: MORIR: muriendo       DORMIR: durmiendo

        *No hay verbos -AR irregulares:  
        CONTAR: contando    EMPEZAR: empezando

    
    Verbos Irregulares:
        IR: yendo

'''''
import random

def Gerundios():
    verbos = [
        ['hablar', 'hablando'], 
        ['comer', 'comiendo'], 
        ['vivir', 'viviendo'], 
        ['traer', 'trayendo'],
        ['caer', 'cayendo'],
        ['huir', 'huyendo'],
        ['construir', 'construyendo'],
        ['concluir', 'concluyendo'],
        ['leer', 'leyendo'],
        ['creer', 'creyendo'],
        ['oir', 'oyendo'],
        ['distinguir', 'distinguiendo'],
        ['extinguir', 'extingo'],
        ['reir', 'riendo'],
        ['freir', 'friendo'],
        ['mentir', 'mintiendo'],
        ['preferir', 'prefiriendo'],
        ['vestir', 'vistiendo'],
        ['seguir', 'siguiendo'],
        ['morir', 'muriendo'],
        ['dormir', 'durmiendo'],
        ['contar', 'contando'],
        ['empezar', 'empezando'],
        ['ir', 'yendo']
        ]
    verbo = random.choice(verbos)
    respuesta = input('¿Qué es el gerundio del verbo ' + verbo[0] + ' en español?  ')
    if respuesta == verbo[1]:
        print("¡Perfecto!")
    elif respuesta.lower() == 'x':
        print('¡Gracias por jugar!')
        exit()
    else:
        print("Lo siento, pero no tienes razón. La respuesta indicada es '" + verbo[1] + "'.")