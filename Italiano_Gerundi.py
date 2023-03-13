'''''
I Participi Presenti & Gerundi:
    -ARE: -ando 
    -ERE: -endo
    -IRE: -endo

    Irregulari:
        BERE: bevendo
        DIRE: dicendo
        FARE: facendo
        TRADURRE: traducendo
        PORRE: ponendo

    Irregularmente Regulari:
        essendo, avendo, stando, dando, venendo, tenendo, andando, dovendo, 
        potendo, volendo, sapendo, capendo, pulendo, uscendo, salendo, morendo, 

'''''
import random


def Gerundi():
    verbi = [
        "parlare",
        "leggere",
        "dormire",
        "finire",
        "cercare",
        "pagare",
        "essere",
        "avere",
        "stare",
        "fare",
        "dare",
        "venire",
        "tenire",
        "andare",
        "dire",
        "dovere",
        "potere",
        "volere",
        "sapere",
        "capire",
        "pulire",
        "bere",
        "uscire",
        "salire",
        "porre",
        "morire",
        "conoscere",
        "sentire",
    ]
    verbo = random.choice(verbi)
    if verbo == "parlare":
        gerundio = "parlando"
    elif verbo == "leggere":
        gerundio = "leggendo"
    elif verbo == "dormire":
        gerundio = "dormendo"
    elif verbo == "finire":
        gerundio = "finendo"
    elif verbo == "cercare":
        gerundio = "cercando"
    elif verbo == "pagare":
        gerundio = "pagando"
    elif verbo == "essere":
        gerundio = "essendo"
    elif verbo == "avere":
        gerundio = "avendo"
    elif verbo == "fare":
        gerundio = "facendo"
    elif verbo == "stare":
        gerundio = "stando"
    elif verbo == "dare":
        gerundio = "dando"
    elif verbo == "venire":
        gerundio = "venendo"
    elif verbo == "tenere":
        gerundio = "tenendo"
    elif verbo == "andare":
        gerundio = "andando"
    elif verbo == "dire":
        gerundio = "dicendo"
    elif verbo == "volere":
        gerundio = "volendo"
    elif verbo == "potere":
        gerundio = "potendo"
    elif verbo == "dovere":
        gerundio = "dovendo"
    elif verbo == "sapere":
        gerundio = "sapendo"
    elif verbo == "capire":
        gerundio = "capendo"
    elif verbo == "pulire":
        gerundio = "pulendo"
    elif verbo == "bere":
        gerundio = "bevendo"
    elif verbo == "uscire":
        gerundio = "uscendo"
    elif verbo == "salire":
        gerundio = "salendo"
    elif verbo == "porre":
        gerundio = "ponendo"
    elif verbo == "morire":
        gerundio = "morendo"
    elif verbo == "conoscere":
        gerundio = "conoscendo"
    elif verbo == "tradurre":
        gerundio = "traducendo"
    else:
        gerundio = "sentendo"
    risposta = input("Qual è il gerundio di " + verbo + "? ")
    if risposta == gerundio:
        print("Giusto!")
    elif risposta.lower() == "x":
        print("Grazie per aver giocato!")
        exit()
    else:
        print("Mi dispiace, è sbagliato.  Riprova.")
        if verbo == "bere":
            print("BERE: bevendo")
        elif verbo == "dire":
            print("DIRE: dicendo")
        elif verbo == "fare":
            print("FARE: facendo")
        elif verbo == "tradurre":
            print("TRADURRE: traducendo")
        elif verbo == "porre":
            print("ponendo")
        else:
            print("Dude, this verb isn't even irregular!")
