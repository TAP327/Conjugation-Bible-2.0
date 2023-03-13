"""''
Pretérito:
    -AR:  -é, -aste, -ó, -amos, -asteis, -aron
    -ER:  -í, -iste, -ió, -imos, -isteis, -ieron
    -IR:  -í, -iste, -ió, -imos, -isteis, -ieron

    Verbos Irregulares:
        SER:  fui, fuiste, fue, fuimos, fuisteis, fueron
        IR:  fui, fuiste, fue, fuimos, fuisteis, fueron
        HABER:  hube, hubiste, hubo, hubimos, hubisteis, hubieron
        PODER:  pude, pudiste, pudo, pudimos, pudisteis, pudieron
        PONER:  puse, pusiste, puso, pusimos, pusisteis, pusieron
        SABER:  supe, supiste, supo, supimos, supisteis, supieron
        HACER:  hice, hiciste, hizo, hicimos, hicisteis, hicieron
        ANDAR:  anduve, anduviste, anduvo, anduvimos, anduvisteis, anduvieron
        ESTAR:  estuve, estuviste, estuvo, estuvimos, estuvisteis, estuvieron
        TENER:  tuve, tuviste, tuvo, tuvimos, tuvisteis, tuvieron
        VENIR:  vine, viniste, vino, vinimos, vinisteis, vinieron
        QUERER:  quise, quisiste, quiso, quisimos, quisisteis, quisieron
        CABER:  cupe, cupiste, cupo, cupimos, cupisteis, cupieron
        TRAER:  traje, trajiste, trajo, trajimos, trajisteis, trajeron
        DECIR:  dije, dijiste, dijo, dijimos, dijisteis, dijeron
        
    UCIR:  TRADUCIR:  traduje, tradujiste, tradujo, tradujimos, tradujisteis, tradujeron

        *Conocer, leer, & escribir son regulares

    Accentos Irregulares
        DAR:  dí, diste, dio, dimos, disteis, dieron
        VER:  ví, viste, vio, vimos, visteis, vieron
        
        *I always felt like DAR & VER were sitting at the kids' table

    Stem Changers: 
        E-I:    REPETIR:  repetí, repetiste, repitió, repetimos, repetisteis, repitieron 
        O-U:    MORIR:  morí, moristem, murió, morimos, moristeis, murieron

            *Solo aplica a las formas 'él' y 'ellos'
    'Yo' Irregular
        C-Z  EMPEZAR:  empecé, empezaste, empezó, empezamos, empezasteis, empezaron
        G-GU PAGAR:  pagué, pagaste, pagó, pagamos, pagasteis, pagaron
        C-QU TOCAR:  toqué, tocaste, tocó, tocamos, tocasteis, tocaron
""" ""
import random


def Pretérito():
    Pronombres = ["yo", "tu", "él", "nosotros", "vosotros", "ellos"]
    Verbos = [
        ["hablar", "-AR:  -é, -aste, -ó, -amos, -asteis, -aron"],
        ["comer", "-ER:  -í, -iste, -ió, -imos, -isteis, -ieron"],
        ["vivir", "-IR:  -í, -iste, -ió, -imos, -isteis, -ieron"],
        ["leer", "-ER:  -í, -iste, -ió, -imos, -isteis, -ieron"],
        ["conocer", "-ER:  -í, -iste, -ió, -imos, -isteis, -ieron"],
        ["escribir", "-IR:  -í, -iste, -ió, -imos, -isteis, -ieron"],
        ["ser", "SER:  fui, fuiste, fue, fuimos, fuisteis, fueron"],
        ["ir", "IR:  fui, fuiste, fue, fuimos, fuisteis, fueron"],
        ["haber", "HABER:  hube, hubiste, hubo, hubimos, hubisteis, hubieron"],
        ["poder", "PODER:  pude, pudiste, pudo, pudimos, pudisteis, pudieron"],
        ["poner", "PONER:  puse, pusiste, puso, pusimos, pusisteis, pusieron"],
        ["saber", "SABER:  supe, supiste, supo, supimos, supisteis, supieron"],
        ["hacer", "HACER:  hice, hiciste, hizo, hicimos, hicisteis, hicieron"],
        [
            "andar",
            "ANDAR:  anduve, anduviste, anduvo, anduvimos, anduvisteis, anduvieron",
        ],
        [
            "estar",
            "ESTAR:  estuve, estuviste, estuvo, estuvimos, estuvisteis, estuvieron",
        ],
        ["tener", "TENER:  tuve, tuviste, tuvo, tuvimos, tuvisteis, tuvieron"],
        ["venir", "VENIR:  vine, viniste, vino, vinimos, vinisteis, vinieron"],
        ["querer", "QUERER:  quise, quisiste, quiso, quisimos, quisisteis, quisieron"],
        ["caber", "CABER:  cupe, cupiste, cupo, cupimos, cupisteis, cupieron"],
        ["traer", "TRAER:  traje, trajiste, trajo, trajimos, trajisteis, trajeron"],
        ["decir", "DECIR:  dije, dijiste, dijo, dijimos, dijisteis, dijeron"],
        [
            "traducir",
            "TRADUCIR:  traduje, tradujiste, tradujo, tradujimos, tradujisteis, tradujeron",
        ],
        [
            "conducir",
            "CONDUCIR:  conduje, condujiste, condujo, condujimos, condujisteis, condujeron",
        ],
        ["dar", "DAR:  dí, diste, dio, dimos, disteis, dieron"],
        ["ver", "VER:  ví, viste, vio, vimos, visteis, vieron  "],
        [
            "repetir",
            "REPETIR:  repetí, repetiste, repitió, repetimos, repetisteis, repitieron",
        ],
        ["pedir", "PEDIR:  pedí, pediste, pidió, pedimos, pedisteis, pidieron"],
        ["morir", "MORIR:  morí, moriste, murió, morimos, moristeis, murieron  "],
        ["dormir", "DORMIR: dormí, dormiste, durmió, dormimos, dormisteis, durmieron"],
        [
            "empezar",
            "EMPEZAR:  empecé, empezaste, empezó, empezamos, empezasteis, empezaron",
        ],
        ["pagar", "PAGAR:  pagué, pagaste, pagó, pagamos, pagasteis, pagaron"],
        ["tocar", "TOCAR:  toqué, tocaste, tocó, tocamos, tocasteis, tocaron"],
    ]
    pronombre = random.choice(Pronombres)
    verbo = random.choice(Verbos)
    if verbo == "hablar":
        raiz = "habl"
    elif verbo == "comer":
        raiz = "com"
    elif verbo == "vivir":
        raiz = "viv"
    elif verbo == "leer":
        raiz = "le"
    elif verbo == "conocer":
        raiz = "conoc"
    elif verbo == "escribir":
        raiz = "escrib"
    elif verbo in ["ser", "ir"]:
        raiz = "fu"
    elif verbo == "haber":
        raiz = "hub"
    elif verbo == "poder":
        raiz = "pud"
    elif verbo == "poner":
        raiz = "pus"
    elif verbo == "saber":
        raiz = "sup"
    elif verbo == "hacer":
        if pronombre != "él":
            raiz = "hic"
        else:
            raiz = "hiz"
    elif verbo == "andar":
        raiz = "anduv"
    elif verbo == "estar":
        raiz = "estuv"
    elif verbo == "tener":
        raiz = "tuv"
    elif verbo == "venir":
        raiz = "vin"
    elif verbo == "querer":
        raiz = "quis"
    elif verbo == "caber":
        raiz = "cup"
    elif verbo == "traer":
        raiz = "traj"
    elif verbo == "decir":
        raiz = "dij"
    elif verbo == "traducir":
        raiz = "traduj"
    elif verbo == "conducir":
        raiz = "conduj"
    elif verbo == "dar":
        raiz = "d"
    elif verbo == "ver":
        raiz = "v"
    elif verbo == "repetir":
        if pronombre not in ["él", "ellos"]:
            raiz = "repet"
        else:
            raiz = "repit"
    elif verbo == "pedir":
        if pronombre not in ["él", "ellos"]:
            raiz = "ped"
        else:
            raiz = "pid"
    elif verbo == "morir":
        if pronombre not in ["él", "ellos"]:
            raiz = "mor"
        else:
            raiz = "mur"
    elif verbo == "dormir":
        if pronombre not in ["él", "ellos"]:
            raiz = "dorm"
        else:
            raiz = "durm"
    elif verbo == "empezar":
        if pronombre == "yo":
            raiz = "empec"
        else:
            raiz = "empez"
    elif verbo == "pagar":
        if pronombre == "yo":
            raiz = "pagu"
        else:
            raiz = "pag"
    else:
        if pronombre == "yo":
            raiz = "toqu"
        else:
            raiz = "toc"
    if pronombre == "yo":
        if verbo[0] in ["hablar", "empezar", "pagar", "tocar"]:
            sufijo = "é"
        elif verbo[0] in [
            "comer",
            "vivir",
            "leer",
            "conocer",
            "escribir",
            "dar",
            "ver",
            "repetir",
            "pedir",
            "morir",
            "dormir",
        ]:
            sufijo = "í"
        elif verbo[0] in [
            "haber",
            "poder",
            "poner",
            "saber",
            "hacer",
            "andar",
            "estar",
            "tener",
            "venir",
            "querer",
            "caber",
            "traer",
            "decir",
            "traducir",
            "conducir",
        ]:
            sufijo = "e"
        else:
            sufijo = "i"
    elif pronombre == "tu":
        if verbo[0] in ["hablar", "empezar", "pagar", "tocar"]:
            sufijo = "aste"
        else:
            sufijo = "iste"
    elif pronombre == "él":
        if verbo[0] in ["hablar", "empezar", "pagar", "tocar"]:
            sufijo = "ó"
        elif verbo[0] in [
            "comer",
            "vivir",
            "leer",
            "conocer",
            "escribir",
            "repetir",
            "pedir",
            "morir",
            "dormir",
        ]:
            sufijo = "ió"
        elif verbo[0] in ["ser", "ir"]:
            sufijo = "e"
        elif verbo[0] in ["dar", "ver"]:
            sufijo = "io"
        else:
            sufijo = "o"
    elif pronombre == "nosotros":
        if verbo[0] in ["hablar", "empezar", "pagar", "tocar"]:
            sufijo = "amos"
        else:
            sufijo = "imos"
    elif pronombre == "vosotros":
        if verbo[0] in ["hablar", "empezar", "pagar", "tocar"]:
            sufijo = "asteis"
        else:
            sufijo = "isteis"
    else:
        if verbo[0] in ["hablar", "empezar", "pagar", "tocar"]:
            sufijo = "aron"
        elif verbo[0] in ["ser", "ir", "traer", "decir", "traducir", "conducir"]:
            sufijo = "eron"
        else:
            sufijo = "ieron"
    respuesta = input("(" + pronombre + ") " + verbo[0] + " en el préterito:  ")
    clave = raiz + sufijo
    if clave == respuesta:
        print("¡Sí!")
    elif respuesta.lower() == "x":
        print("¡Gracias por jugar!")
        exit()
    else:
        print("Lo siento, pero eso no es la respuesta indicada.")
        print(verbo[1])
