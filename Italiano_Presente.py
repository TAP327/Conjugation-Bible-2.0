import random

"""''
Il Presente:
    -ARE:  -o, -i, -a, -iamo, -ate, -ano,
    -ERE:  -o, -i, -e, -iamo, -ete, -ono,
    -IRE:  -o, -i, -e, -iamo, -ite, -ono,
        -isco, -isci, -isce, -iamo, -ite, -iscono,

    Stem Changers:
        -CH- CERCARE:  cerco, cerchi, cerca, cerchiamo, cercate, cercano,
        -GH- PAGARE:   pago, paghi, paga, paghiamo, pagate, pagano,

    Irregulars:
        ESSERE:   sono, sei, è, siamo, siete, sono,
        AVERE:    ho, hai, ha, abbiamo, avete, hanno,
        STARE:    sto, stai, sta, stiamo, state, stanno, 
        FARE:     faccio, fai, fa, facciamo, fate, fanno,
        DARE:     do, dai, da, diamo, date, danno,
        VENIRE:   vengo, vieni, viene, veniamo, venite, vengono,
        TENERE:   tengo, tieni, tiene, teniamo, tenete, tengono,
        ANDARE:   vado, vai, va, andiamo, andate, vanno,
        DIRE:     dico, dici, dice, diciamo, dite, dicono,
        DOVERE:   devo (debbo), devi, deve, dobbiamo, dovete, devono (debbono),
        POTERE:   posso, puoi, può, possiamo, potete, possono,
        VOLERE:   voglio, vuoi, vuole, vogliamo, volete, vogliono, 
        SAPERE:   so, sai, sa, sappiamo, sapete, sanno,
        CAPIRE:   capisco, capisci, capisce, capiamo, capite, capiscono,    (You know, I'm not sure why these is included; they're regular for -isc-)
        PULIRE:   pulisco, pulisci, pulisce, puliamo, pulite, puliscono,
        BERE:     bevo, bevi, beve, beviamo, bevete, bevono,
        USCIRE:   esco, esci, esce, usciamo, uscite, escono,
        SALIRE:   salgo, sali, sale, saliamo, salite, salgono,
        PORRE:    pongo, poni, pone, poniamo, ponete, pongono, 
        MORIRE:   muoio, muori, muore, moriamo, morite, muoiono, 

        *CONOSCERE, SENTRIRE, & DORMIRE are regular  
            (Yes, dormire is the model verb I used.  No, I'm not trying to patronize you. )
""" ""


def Presente():
    pronomi = ["io", "tu", "lui", "noi", "voi", "loro"]
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
    pronomo = random.choice(pronomi)
    verbo = random.choice(verbi)
    if verbo == "parlare":
        radice = "parl"
    elif verbo == "leggere":
        radice = "legg"
    elif verbo == "dormire":
        radice = "dorm"
    elif verbo == "finire":
        if pronomo not in ["noi", "voi"]:
            radice = "finisc"
        else:
            radice = "fin"
    elif verbo == "conoscere":
        radice = "conosc"
    elif verbo == "sentire":
        radice = "sent"
    elif verbo == "cercare":
        if pronomo not in ["tu", "noi"]:
            radice = "cerc"
        else:
            radice = "cerch"
    elif verbo == "pagare":
        if pronomo not in ["tu", "noi"]:
            radice = "pag"
        else:
            radice = "pagh"
    elif verbo in [
        "essere",
        "avere",
        "venire",
        "tenire",
        "andare",
        "potere",
        "volere",
        "dovere",
        "sapere",
    ]:
        radice = "niente"
    elif verbo == "stare":
        radice = "st"
    elif verbo == "fare":
        radice = "fa"
    elif verbo == "dare":
        radice = "d"
    elif verbo == "dire":
        if verbo != "voi":
            radice = "dic"
        else:
            radice = "di"
    elif verbo == "capire":
        if pronomo not in ["noi", "voi"]:
            radice = "capisc"
        else:
            radice = "cap"
    elif verbo == "pulire":
        if pronomo not in ["noi", "voi"]:
            radice = "pulisc"
        else:
            radice = "pul"
    elif verbo == "bere":
        radice = "bev"  # Finally! Just a regular old stem changer!
    elif verbo == "uscire":
        if pronomo not in ["noi", "voi"]:
            radice = "esc"
        else:
            radice = "usc"
    elif verbo == "salire":
        if pronomo not in ["io", "loro"]:
            radice = "sal"
        else:
            radice = "salg"
    elif verbo == "porre":
        if pronomo not in ["io", "loro"]:
            radice = "pon"
        else:
            radice = "pong"
    elif verbo == "morire":
        if pronomo in ["tu", "lui"]:
            radice = "muor"
        elif pronomo in ["noi", "voi"]:
            radice = "mor"
        else:
            radice = "muoi"
    # =========================================================================================================
    # =========================================================================================================
    if pronomo == "io":
        if verbo == "essere":
            suffisso = "sono"
        elif verbo == "fare":
            suffisso = "ccio"
        elif verbo == "avere":
            suffisso = "ho"
        elif verbo == "venire":
            suffisso = "vengo"
        elif verbo == "tenire":
            suffisso = "tengo"
        elif verbo == "andare":
            suffisso = "vado"
        elif verbo == "potere":
            suffisso = "posso"
        elif verbo == "volere":
            suffisso = "voglio"
        elif verbo == "dovere":
            suffisso = "devo" or "debbo"
        elif verbo == "sapere":
            suffisso = "so"
        else:
            suffisso = "o"
    elif pronomo == "tu":
        if verbo == "essere":
            suffisso = "sei"
        elif verbo == "stare":
            suffisso = "ai"
        elif verbo == "fare":
            suffisso = "i"
        elif verbo == "avere":
            suffisso = "hai"
        elif verbo == "dare":
            suffisso = "ai"
        elif verbo == "venire":
            suffisso = "vieni"
        elif verbo == "tenire":
            suffisso = "tieni"
        elif verbo == "andare":
            suffisso = "vai"
        elif verbo == "potere":
            suffisso = "puoi"
        elif verbo == "volere":
            suffisso = "vuoi"
        elif verbo == "dovere":
            suffisso = "devi"
        elif verbo == "sapere":
            suffisso = "sai"
        else:
            suffisso = "i"
    elif pronomo == "lui":
        if verbo == "essere":
            suffisso = "è"
        elif verbo == "fare":
            suffisso = ""
        elif verbo == "avere":
            suffisso = "ha"
        elif verbo == "dare":
            suffisso = "à"
        elif verbo == "venire":
            suffisso = "viene"
        elif verbo == "tenire":
            suffisso = "tiene"
        elif verbo == "andare":
            suffisso = "va"
        elif verbo == "potere":
            suffisso = "può"
        elif verbo == "volere":
            suffisso = "vuole"
        elif verbo == "dovere":
            suffisso = "deve"
        elif verbo == "sapere":
            suffisso = "sa"
        elif verbo == ("parlare", "cercare", "pagare", "stare"):
            suffisso = "a"
        else:
            suffisso = "e"
    elif pronomo == "noi":
        if verbo == "essere":
            suffisso = "siamo"
        elif verbo == "fare":
            suffisso = "cciamo"
        elif verbo == "avere":
            suffisso = "abbiamo"
        elif verbo == "venire":
            suffisso = "veniamo"
        elif verbo == "tenire":
            suffisso = "teniamo"
        elif verbo == "andare":
            suffisso = "andiamo"
        elif verbo == "potere":
            suffisso = "possiamo"
        elif verbo == "volere":
            suffisso = "vogliamo"
        elif verbo == "dovere":
            suffisso = "dobbiamo"
        elif verbo == "sapere":
            suffisso = "sappiamo"
        else:
            suffisso = "iamo"
    elif pronomo == "voi":
        if verbo == "essere":
            suffisso = "siete"
        elif verbo == "fare":
            suffisso = "te"
        elif verbo == "avere":
            suffisso = "avete"
        elif verbo == "venire":
            suffisso = "venete"
        elif verbo == "tenire":
            suffisso = "tenete"
        elif verbo == "andare":
            suffisso = "andate"
        elif verbo == "potere":
            suffisso = "potete"
        elif verbo == "volere":
            suffisso = "volete"
        elif verbo == "dovere":
            suffisso = "dovete"
        elif verbo == "sapere":
            suffisso = "sapete"
        elif verbo in ["parlare", "cercare", "pagare", "stare", "dare"]:
            suffisso = "ate"
        elif verbo in ["leggere", "bevere", "ponere", "conoscere"]:
            suffisso = "ete"
        else:
            suffisso = "ite"
    else:
        if verbo == "essere":
            suffisso = "sono"
        elif verbo in ["stare", "danno"]:
            suffisso = "anno"
        elif verbo == "fare":
            suffisso = "nno"
        elif verbo == "avere":
            suffisso = "hanno"
        elif verbo == "venire":
            suffisso = "vengono"
        elif verbo == "tenire":
            suffisso = "tengono"
        elif verbo == "andare":
            suffisso = "vanno"
        elif verbo == "potere":
            suffisso = "possono"
        elif verbo == "volere":
            suffisso = "vogliono"
        elif verbo == "dovere":
            suffisso = "devono" or "debbono"
        elif verbo == "sapere":
            suffisso = "sanno"
        elif verbo in ["parlare", "cercare", "pagare"]:
            suffisso = "ano"
        else:
            suffisso = "ono"
    if radice == "niente":
        chiave = suffisso
    else:
        chiave = radice + suffisso
    risposta = input("(" + pronomo + ") " + verbo + " al presente: ")
    if risposta == chiave:
        print("Evviva!")
    elif risposta.lower() == "x":
        print("Grazie per aver giocato!")
        exit()
    else:
        print("Mi dispiace, è sbagliato.  Riprova.")
        if verbo == "parlare":
            print("-ARE:  -o, -i, -a, -iamo, -ate, -ano,")
        elif verbo == ("leggere" or "conoscere"):
            print("-ERE:  -o, -i, -e, -iamo, -ete, -ono,")
        elif verbo == ("dormire" or "sentire"):
            print("-IRE:  -o, -i, -e, -iamo, -ite, -ono,")
        elif verbo == ("finire" or "capire" or "pulire"):
            print("-isco, -isci, -isce, -iamo, -ite, -iscono,")
        elif verbo == "cercare":
            print("-CH- CERCARE:  cerco, cerchi, cerca, cerchiamo, cercate, cercano,")
        elif verbo == "pulire":
            print("-GH- PAGARE:   pago, paghi, paga, paghiamo, pagate, pagano,")
        elif verbo == "essere":
            print("ESSERE:   sono, sei, è, siamo, siete, sono,")
        elif verbo == "avere":
            print("AVERE:    ho, hai, ha, abbiamo, avete, hanno,")
        elif verbo == "stare":
            print("STARE:    sto, stai, sta, stiamo, state, stanno,")
        elif verbo == "fare":
            print("FARE:     faccio, fai, fa, facciamo, fate, fanno,")
        elif verbo == "dare":
            print("DARE:     do, dai, da, diamo, date, danno,")
        elif verbo == "venire":
            print("VENIRE:   vengo, vieni, viene, veniamo, venite, vengono,")
        elif verbo == "tenire":
            print("TENERE:   tengo, tieni, tiene, teniamo, tenete, tengono,")
        elif verbo == "amdare":
            print("ANDARE:   vado, vai, va, andiamo, andate, vanno,")
        elif verbo == "dire":
            print("DIRE:     dico, dici, dice, diciamo, dite, dicono,")
        elif verbo == "dovere":
            print(
                "DOVERE:   devo (debbo), devi, deve, dobbiamo, dovete, devono (debbono),"
            )
        elif verbo == "potere":
            print("POTERE:   posso, puoi, può, possiamo, potete, possono,")
        elif verbo == "volere":
            print("VOLERE:   voglio, vuoi, vuole, vogliamo, volete, vogliono, ")
        elif verbo == "sapere":
            print("SAPERE:   so, sai, sa, sappiamo, sapete, sanno,")
        elif verbo == "bere":
            print("BERE:     bevo, bevi, beve, beviamo, bevete, bevono,")
        elif verbo == "uscire":
            print("USCIRE:   esco, esci, esce, usciamo, uscite, escono,")
        elif verbo == "salire":
            print("SALIRE:   salgo, sali, sale, saliamo, salite, salgono,")
        elif verbo == "porre":
            print("PORRE:    pongo, poni, pone, poniamo, ponete, pongono,")
        else:
            print("MORIRE:   muoio, muori, muore, moriamo, morite, muoiono,")


# return verbs.get("porre") OR return verbs["porre"]  SECONDO LUI
