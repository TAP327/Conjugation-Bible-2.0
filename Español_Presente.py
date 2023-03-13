'''''
El Presente:
    Los Verbos Regulares:
        -AR:  -o, -as, -a, -amos, -áis, -an
        -ER:  -o, -es, -e, -emos, -éis, -en
        -IR:  -o, -es, -e, -imos, -ís, -en

    Los Verbos Irregulares:
        HABER:  he, has, ha, hemos, habéis, han
        SER:  soy, eres, es, somos, sois, son
        ESTAR: estoy, estás, está, estamos, estáis, están
        IR:  voy, vas, va, vamos, vais, van
        
    Stem Changers:  
        E - IE  PENSAR:  pienso, piensas, piensa, pensamos, pensáis, piensan
        O - UE  VOLVER:  vuelvo, vuelves, vuelve, volvemos, volvéis, vuelven
        E - I   REPETIR:  repito, repites, repite, repetimos, repetís, repiten
        I - IE  ADQUIRIR:  adquiero, adquieres, adquiere, adquirimos, adquirís, adquieren
        U - UE  JUGAR:  juego, juegas, juega, jugamos, jugáis, juegan
        O - HUE OLER:  huelo, hueles, huele, olemos, oléis, huelen

        G - J   ESCOGER:  escojo, escoges, escoge, escogemos, escogéis, escogen
        C - Z   FRUNCIR:  frunzo, frunces, frunce, fruncimos, fruncís, fruncen
        C - ZC  CONOCER: conozco, conoces, conoce, conocemos, conocéis, conocen,
        C - G   DECIR:  digo, dices, dice, decimos, decís, dicen
                HACER:  hago, haces, hace, hacemos, hacéis, hacen
                TENER:  tengo, tienes, tiene, tenemos, tenéis, tienen
                VENIR:  vengo, vienes, viene, venemos, venéis, vienen
                SALIR:  salgo, sales, sale, salimos, salís, salen,
                PONER:  pongo, pones, pone, ponemos, ponéis, ponen
        -GUIR:  DISTINGUIR: distingo, distingues, distingue, distinguimos, distinguís, distinguen
        -UIR:   CONCLUIR:  concluyo, concluyes, concluye, concluimos, concluís, concluyen

    Irregular 'Yo':
        CABER: quepo, cabes, cabe, cabemos, cabéis, caben
        CAER:  caigo, caes, cae, caemos, caéis, caen
        DAR:  doy, das, da, damos, dais, dan
        SABER:  sé, sabes, sabe, sabemos, sabéis, saben
        TRAER:  traigo, traes, trae, traemos, traéis, traen
        VALER:  valgo, vales vale, valemos, valéis, valen
        VER:  veo, ves, ve, vemos, véis, ven
'''''
import random


def Presente():
    pronombres = ["yo", "tu", "él", "nosotros", "vosotros", "ellos"]
    verbos = {
        "hablar": "-AR:  -o, -as, -a, -amos, -áis, -an",
        "comer": "-ER:  -o, -es, -e, -emos, -éis, -en",
        "vivir": "-IR:  -o, -es, -e, -imos, -s, -en",
        "haber": "HABER:  he, has, ha, hemos, habéis, han",
        "ser": "SER:  soy, eres, es, somos, sois, son",
        "estar": "ESTAR: estoy, estás, está, estamos, estáis, están",
        "ir": "IR:  voy, vas, va, vamos, vais, van",
        "pensar": "PENSAR:  pienso, piensas, piensa, pensamos, pensáis, piensan",
        "volver": "VOLVER:  vuelvo, vuelves, vuelve, volvemos, volvéis, vuelven",
        "repetir": "REPETIR:  repito, repites, repite, repetimos, repetís, repiten",
        "adquirir": "ADQUIRIR:  adquiero, adquieres, adquiere, adquirimos, adquirís, adquieren",
        "jugar": "JUGAR:  juego, juegas, juega, jugamos, jugáis, juegan",
        "oler": "OLER:  huelo, hueles, huele, olemos, oléis, huelen",
        "escoger": "ESCOGER:  escojo, escoges, escoge, escogemos, escogéis, escogen",
        "fruncir": "FRUNCIR:  frunzo, frunces, frunce, fruncimos, fruncís, fruncen",
        "conocer": "CONOCER: conozco, conoces, conoce, conocemos, conocéis, conocen",
        "decir": "DECIR:  digo, dices, dice, decimos, decís, dicen",
        "hacer": "HACER:  hago, haces, hace, hacemos, hacéis, hacen",
        "tener": "TENER:  tengo, tienes, tiene, tenemos, tenéis, tienen",
        "venir": "VENIR:  vengo, vienes, viene, venemos, venéis, vienen",
        "salir": "SALIR:  salgo, sales, sale, salimos, salís, salen",
        "poner": "PONER:  pongo, pones, pone, ponemos, ponéis, ponen",
        "distinguir": "DISTINGUIR: distingo, distingues, distingue, distinguimos, distinguís, distinguen",
        "concluir": "CONCLUIR:  concluyo, concluyes, concluye, concluimos, concluís, concluyen",
        "caber": "CABER: quepo, cabes, cabe, cabemos, cabéis, caben",
        "caer": "CAER:  caigo, caes, cae, caemos, caéis, caen",
        "dar": "DAR:  doy, das, da, damos, dais, dan",
        "saber": "SABER:  sé, sabes, sabe, sabemos, sabéis, saben",
        "traer": "TRAER:  traigo, traes, trae, traemos, traéis, traen",
        "valer": "VALER:  valgo, vales vale, valemos, valéis, valen,",
        "ver": "VER:  veo, ves, ve, vemos, véis, ven",
    }
    pronombre = random.choice(pronombres)
    verbo = random.choice(list(verbos.keys()))
    if verbo == "hablar":
        raiz = "habl"
    elif verbo == "comer":
        raiz = "com"
    elif verbo == "vivir":
        raiz = "viv"
    elif verbo in [
        "haber",
        "ser"
    ]:
        raiz = "nada"
    elif verbo == "estar":
        raiz = "est"
    elif verbo == "ir":
        raiz = "v"
    elif verbo == "pensar":
        if pronombre not in ["nosotros", "vosotros"]:
            raiz = "piens"
        else:
            raiz = "pens"
    elif verbo == "volver":
        if pronombre not in ["nosotros", "vosotros"]:
            raiz = "vuelv"
        else:
            raiz = "volv"
    elif verbo == "repetir":
        if pronombre not in ["nosotros", "vosotros"]:
            raiz = "repit"
        else:
            raiz = "repet"
    elif verbo == "adquirir":
        if pronombre not in ["nosotros", "vosotros"]:
            raiz = "adquier"
        else:
            raiz = "adquir"
    elif verbo == "jugar":
        if pronombre not in ["nosotros", "vosotros"]:
            raiz = "jueg"
        else:
            raiz = "jug"
    elif verbo == "oler":
        if pronombre not in ["nosotros", "vosotros"]:
            raiz = "huel"
        else:
            raiz = "ol"
    elif verbo == "escoger":
        if pronombre == "yo":
            raiz = "escoj"
        else:
            raiz = "escog"
    elif verbo == "fruncir":
        if pronombre == "yo":
            raiz = "frunz"
        else:
            raiz = "frunc"
    elif verbo == "conocer":
        if pronombre == "yo":
            raiz = "conozc"
        else:
            raiz = "conoc"
    elif verbo == "decir":
        if pronombre == "yo":
            raiz = "dig"
        elif pronombre in ["nosotros", "vosotros"]:
            raiz = "dec"
        else:
            raiz = "dic"
    elif verbo == "hacer":
        if pronombre == "yo":
            raiz = "hag"
        else:
            raiz = "hac"
    elif verbo == "tener":
        if pronombre == "yo":
            raiz = "teng"
        elif pronombre in ["nosotros", "vosotros"]:
            raiz = "ten"
        else:
            raiz = "tien"
    elif verbo == "venir":
        if pronombre == "yo":
            raiz = "veng"
        elif pronombre in ["nosotros", "vosotros"]:
            raiz = "ven"
        else:
            raiz = "vien"
    elif verbo == "salir":
        if pronombre == "yo":
            raiz = "salg"
        else:
            raiz = "sal"
    elif verbo == "poner":
        if pronombre == "yo":
            raiz = "pong"
        else:
            raiz = "pon"
    elif verbo == "distinguir":
        if pronombre == "yo":
            raiz = "disting"
        else:
            raiz = "distingu"
    elif verbo == "concluir":
        if pronombre in ["nosotros", "vosotros"]:
            raiz = "conclu"
        else:
            raiz = "concluy"
    elif verbo == "caber":
        if pronombre == "yo":
            raiz = "quep"
        else:
            raiz = "cab"
    elif verbo == "caer":
        if pronombre == "yo":
            raiz = "caig"
        else:
            raiz = "ca"
    elif verbo == "dar":
        raiz = "d"
    elif verbo == "saber":
        if pronombre == "yo":
            raiz = "nada"
        else:
            raiz = "sab"
    elif verbo == "traer":
        if pronombre == "yo":
            raiz = "traig"
        else:
            raiz = "tra"
    elif verbo == "valer":
        if pronombre == "yo":
            raiz = "valg"
        else:
            raiz = "val"
    else:
        if pronombre == "yo":
            raiz = "ve"
        else:
            raiz = "v"
    # ==================================================================================================
    # ==================================================================================================
    if pronombre == "yo":
        if verbo in [
            "hablar",
            "comer",
            "vivir",
            "pensar",
            "volver",
            "repetir",
            "adquirir",
            "jugar",
            "oler",
            "escoger",
            "fruncir",
            "conocer",
            "decir",
            "hacer",
            "tener",
            "venir",
            "salir",
            "poner",
            "distinguir",
            "concluir",
            "caber",
            "caer",
            "traer",
            "valer",
            "ver",
        ]:
            sufijo = "o"
        elif verbo == "haber":
            sufijo = "he"
        elif verbo == "ser":
            sufijo = "soy"
        elif verbo in ["estar", "dar", "ir"]:
            sufijo = "oy"
        else:
            sufijo = "sé"
    elif pronombre == "tu":
        if verbo in ["hablar", "pensar", "jugar", "dar"]:
            sufijo = "as"
        elif verbo in [
            "comer",
            "vivir",
            "volver",
            "repetir",
            "adquirir",
            "oler",
            "escoger",
            "fruncir",
            "conocer",
            "decir",
            "hacer",
            "tener",
            "venir",
            "salir",
            "poner",
            "distinguir",
            "concluir",
            "caber",
            "caer",
            "saber",
            "traer",
            "valer",
            "ver",
        ]:
            sufijo = "es"
        elif verbo == "haber":
            sufijo = "has"
        elif verbo == "ser":
            sufijo = "eres"
        elif verbo == "estar":
            sufijo = "ás"
        elif verbo == "ir":
            sufijo = "vas"
    elif pronombre == "él":
        if verbo in ["hablar", "pensar", "jugar", "dar"]:
            sufijo = "a"
        elif verbo in [
            "comer",
            "vivir",
            "ir",
            "volver",
            "repetir",
            "adquirir",
            "oler",
            "escoger",
            "fruncir",
            "conocer",
            "decir",
            "hacer",
            "tener",
            "venir",
            "salir",
            "poner",
            "distinguir",
            "concluir",
            "caber",
            "caer",
            "saber",
            "traer",
            "valer",
            "ver",
        ]:
            sufijo = "e"
        elif verbo == "haber":
            sufijo = "ha"
        elif verbo == "ser":
            sufijo = "es"
        elif verbo == "estar":
            sufijo = "á"
        elif verbo == "ir":
            sufijo = "va"
    elif pronombre == "nosotros":
        if verbo in ["hablar", "pensar", "jugar", "dar", "estar"]:
            sufijo = "amos"
        elif verbo in [
            "comer",
            "volver",
            "oler",
            "escoger",
            "conocer",
            "hacer",
            "tener",
            "poner",
            "caber",
            "caer",
            "saber",
            "traer",
            "valer",
            "ver",
        ]:
            sufijo = "emos"
        elif verbo in [
            "vivir",
            "repetir",
            "adquirir",
            "fruncir",
            "decir",
            "venir",
            "salir",
            "poner",
            "distinguir",
            "concluir",
        ]:
            sufijo = "imos"
        elif verbo == "haber":
            sufijo = "hemos"
        elif verbo == "ser":
            sufijo = "somos"
        elif verbo == "ir":
            sufijo = "vamos"
    elif pronombre == "vosotros":
        if verbo in ["hablar", "pensar", "jugar", "dar", "estar"]:
            sufijo = "áis"
        elif verbo in [
            "comer",
            "volver",
            "oler",
            "escoger",
            "conocer",
            "hacer",
            "tener",
            "poner",
            "caber",
            "caer",
            "saber",
            "traer",
            "valer",
            "ver",
        ]:
            sufijo = "éis"
        elif verbo in [
            "vivir",
            "repetir",
            "adquirir",
            "fruncir",
            "decir",
            "venir",
            "salir",
            "distinguir",
            "concluir",
        ]:
            sufijo = "ís"
        elif verbo == "haber":
            sufijo = "habéis"
        elif verbo == "ser":
            sufijo = "sois"
        elif verbo == "ir":
            sufijo = "vais"
    else:
        if verbo in ["hablar", "pensar", "jugar", "dar"]:
            sufijo = "an"
        elif verbo in [
            "comer",
            "vivir",
            "volver",
            "repetir",
            "adquirir",
            "oler",
            "escoger",
            "fruncir",
            "conocer",
            "decir",
            "hacer",
            "tener",
            "venir",
            "salir",
            "poner",
            "distinguir",
            "concluir",
            "caber",
            "caer",
            "saber",
            "traer",
            "valer",
            "ver",
        ]:
            sufijo = "en"
        elif verbo == "haber":
            sufijo = "han"
        elif verbo == "ser":
            sufijo = "son"
        elif verbo == "estar":
            sufijo = "án"
        elif verbo == "ir":
            sufijo = "van"
    if raiz == "nada":
        clave = sufijo
    else:
        clave = raiz + sufijo
    respuesta = input("(" + pronombre + ") " + verbo + " en el presente: ")
    if respuesta == clave:
        print("¡Eso!")
    elif respuesta.lower() == "x":
        print("¡Gracias por juagr!")
        exit()
    else:
        print(verbos[verbo])



def Presente1():
    terminado = None
    while terminado != "x":
        terminado = Presente()
        if terminado == "x":
            print("¡Gracias por juagr!")
            exit()
        print(terminado)
