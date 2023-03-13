"""''
L'Imperfetto: 
    -ARE:  -avo, -avi, -ava, -avamo, -avate, -avano
    -ERE:  -evo, -evi, -eva, -evamo, -evate, -evano
    -IRE:  -ivo, -ivi, -iva, -ivamo, -ivate, -ivano
       *Verbi 'isc' sono regulari

    Verbi Irregulari:
    ESSERE:  ero, eri, era, eravamo, eravate, erano  
        *Used for time: "erano le due del pomeriggio", "era lunedi",
    FARE:  facevo, facevi, faceva, facevamo, facevate, facevano,
    BERE:  bevevo, bevevi, bevevo, bevevamo, bevevate, bevevano,
    DIRE:  dicevo, dicevi, dicevo, dicevamo, dicevate, dicevano,
    TRADURRE:  traducevo, traducevi, traducevo, traducevamo, traducevate, traducevano
    
    Note: Dare is suspiciously regular
    
    Da:
        preposition used to mean 'had been': "aspettavo da due ore"
""" ""
import random


def Imperfetto():
    pronomi = ["io", "tu", "lei", "noi", "voi", "loro"]
    verbi = [
        "parlare",
        "vendere",
        "partire",
        "essere",
        "fare",
        "bere",
        "dire",
        "tradurre",
    ]
    pronomo = random.choice(pronomi)
    verbo = random.choice(verbi)
    risposta = input("(" + pronomo + ") " + verbo + " al L'imperfetto: ")
    if verbo == "parlare":
        if pronomo == "io" and risposta == "parlavo":
            print("Corretto!")
        elif pronomo == "tu" and risposta == "parlavi":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "parlava":
            print("Corretto!")
        elif pronomo == "noi" and risposta == "parlavamo":
            print("Corretto!")
        elif pronomo == "voi" and risposta == "parlavate":
            print("Corretto!")
        elif pronomo == "loro" and risposta == "parlavano":
            print("Corretto!")
        else:
            print("-ARE:  -avo, -avi, -ava, -avamo, -avate, -avano")
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "vendere":
        if pronomo == "io" and risposta == "vendevo":
            print("Corretto!")
        elif pronomo == "tu" and risposta == "vendevi":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "vendeva":
            print("Corretto!")
        elif pronomo == "noi" and risposta == "vendevamo":
            print("Corretto!")
        elif pronomo == "voi" and risposta == "vendevate":
            print("Corretto!")
        elif pronomo == "loro" and risposta == "vendevano":
            print("Corretto!")
        else:
            print("-ERE:  -evo, -evi, -eva, -evamo, -evate, -evano")
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "partire":
        if pronomo == "io" and risposta == "partivo":
            print("Corretto!")
        elif pronomo == "tu" and risposta == "partivi":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "partivo":
            print("Corretto!")
        elif pronomo == "noi" and risposta == "partivamo":
            print("Corretto!")
        elif pronomo == "voi" and risposta == "partivate":
            print("Corretto!")
        elif pronomo == "loro" and risposta == "partivano":
            print("Corretto!")
        else:
            print("-IRE:  -ivo, -ivi, -iva, -ivamo, -ivate, -ivano")
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "essere":
        if pronomo == "io" and risposta == "era":
            print("Corretto!")
        elif pronomo == "tu" and risposta == "eri":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "era":
            print("Corretto!")
        elif pronomo == "noi" and risposta == "eravamo":
            print("Corretto!")
        elif pronomo == "voi" and risposta == "eravate":
            print("Corretto!")
        elif pronomo == "loro" and risposta == "erano":
            print("Corretto!")
        else:
            print("ESSERE:  ero, eri, era, eravamo, eravate, erano")
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "fare":
        if pronomo == "io" and risposta == "facevo":
            print("Corretto!")
        elif pronomo == "tu" and risposta == "facevi":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "faceva":
            print("Corretto!")
        elif pronomo == "noi" and risposta == "facevamo":
            print("Corretto!")
        elif pronomo == "voi" and risposta == "facevate":
            print("Corretto!")
        elif pronomo == "loro" and risposta == "facevano":
            print("Corretto!")
        else:
            print("FARE:  facevo, facevi, faceva, facevamo, facevate, facevano,")
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "bere":
        if pronomo == "io" and risposta == "bevevo":
            print("Corretto!")
        elif pronomo == "tu" and risposta == "bevevi":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "beveva":
            print("Corretto!")
        elif pronomo == "noi" and risposta == "bevevamo":
            print("Corretto!")
        elif pronomo == "voi" and risposta == "bevevate":
            print("Corretto!")
        elif pronomo == "loro" and risposta == "bevevano":
            print("Corretto!")
        else:
            print("Mi dispiace, è sbagliato.  Riprova.")
            print("BERE:  bevevo, bevevi, bevevo, bevevamo, bevevate, bevevano,")
    elif verbo == "dire":
        if pronomo == "io" and risposta == "dicevo":
            print("Corretto!")
        elif pronomo == "tu" and risposta == "dicevi":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "diceva":
            print("Corretto!")
        elif pronomo == "noi" and risposta == "dicevamo":
            print("Corretto!")
        elif pronomo == "voi" and risposta == "dicevate":
            print("Corretto!")
        elif pronomo == "loro" and risposta == "dicevano":
            print("Corretto!")
        else:
            print("DIRE:  dicevo, dicevi, dicevo, dicevamo, dicevate, dicevano,")
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "tradurre":
        if pronomo == "io" and risposta == "traducevo":
            print("Corretto!")
        elif pronomo == "tu" and risposta == "traducevi":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "traduceva":
            print("Corretto!")
        elif pronomo == "noi" and risposta == "traducevamo":
            print("Corretto!")
        elif pronomo == "voi" and risposta == "traducevate":
            print("Corretto!")
        elif pronomo == "loro" and risposta == "traducevano":
            print("Corretto!")
        else:
            print(
                "TRADURRE:  traducevo, traducevi, traducevo, traducevamo, traducevate, traducevano"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif risposta.lower() == "x":
        print("Grazie per aver giocato!")
        exit()


