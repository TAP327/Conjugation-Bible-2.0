'''''
Il Passato Prossimo:
    Compound tense that can use ESSERE or AVERE as the auxiliary verb
    (option obj. pronoun) AUX (present) + Past Participle

    ARE: -ato   ERE: -uto   IRE: -ito

    - All transitive verbs go with AVERE 
        *transitive verbs are verbs with direct objects
         that receive the action of the verb
    - All reflexive verbs go with ESSERE 
    - Transitive, Reflexive, and Casa di Essere verbs require 
        past participle agreement in gender and number
    
    Casa di Essere:
        Scendere (sceso)        Restare (restato)       Vivere (vissuto)
        Essere (stato)          Rimanere (rimasto)      Stare (stato)
        Uscire (uscito)         Salire (salito)         Venire (venuto)
        Andare (andato)         Cadere (caduto)         Nascere (nato)
        Divenire (divenuto)     Diventare (diventato)   Entrare (entrato)
        Rivenire (rivenuto)     Cadere (caduto)         Ritornare (ritornato)
        Arrivare (arrivato)     Morire (morto)          Partire (partito)
        chiedere (chiesto)      Chiudere (chiuso)        Dire (detto)
        Rompere (rotto)

*Combinare con i verbi ausiliari imperfetti per creare il trapassato prossimo
ESSERE: ero, eri, era, eravamo, eravate, erano
AVERE:  avevo, avevi, aveva, avevamo, avevate, avevano
'''''
import random


def Passato_Prossimo():
    pronomi = ["lui", "lei", "loro (m.)", "loro (f.)"]
    verbi = [
        "parlare",
        "vendere",
        "finire",
        "rompere",
        "chiedere",
        "dire",
        "alzarsi",
        "scendere",
        "restare",
        "vivere",
        "essere",
        "rimanere",
        "stare",
        "uscire",
        "salire",
        "venire",
        "andare",
        "cadere",
        "nascere",
        "divenire",
        "diventare",
        "entrare",
        "rivenire",
        "ritornare",
        "arrivare",
        "morire",
        "partire",
    ]
    pronomo = random.choice(pronomi)
    verbo = random.choice(verbi)
    risposta = input("(" + pronomo + ") " + verbo + " al Passato Prossimo: ")
    if risposta.lower() == "x":
        print("Grazie per aver giocato!")
        exit()
    elif verbo == "parlare":
        if pronomo == "lui" and risposta == "ha parlato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "ha parlato":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "hanno parlato":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "hanno parlato":
            print("Corretto!")
        else:
            print("-ARE: Avere + -ato")
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "vendere":
        if pronomo == "lui" and risposta == "ha venduto":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "ha venduto":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "hanno venduto":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "hanno venduto":
            print("Corretto!")
        else:
            print("-ERE: Avere + -uto")
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "finire":
        if pronomo == "lui" and risposta == "ha finito":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "ha finito":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "hanno finito":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "hanno finito":
            print("Corretto!")
        else:
            print("-IRE: Avere + -ito")
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "rompere":
        if pronomo == "lui" and risposta == "ha rotto":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "ha rotto":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "hanno rotto":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "hanno rotto":
            print("Corretto!")
        else:
            print("ROMPERE: rotto")
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "chiedere":
        if pronomo == "lui" and risposta == "ha chiesto":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "ha chiesto":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "hanno chiesto":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "hanno chiesto":
            print("Corretto!")
        else:
            print("CHIEDERE: chiesto")
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "chiudere":
        if pronomo == "lui" and risposta == "ha chiuso":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "ha chiuso":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "hanno chiuso":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "hanno chiuso":
            print("Corretto!")
        else:
            print("CHIUDERE: chiuso")
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "dire":
        if pronomo == "lui" and risposta == "ha detto":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "ha detto":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "hanno detto":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "hanno detto":
            print("Corretto!")
        else:
            print("DIRE: detto")
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "alzarsi":
        if pronomo == "lui" and risposta == "si ?? alzato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "si ?? alzata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "si sono alzati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "si sono alzate":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "scendere":
        if pronomo == "lui" and risposta == "?? sceso":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "?? scesa":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono scesi":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono scese":
            print("Corretto!")
        else:
            print(
                "Casa di Essere: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "restare":
        if pronomo == "lui" and risposta == "?? restato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "?? restata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono restati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono restate":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "vivere":
        if pronomo == "lui" and risposta == "?? vissuto":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "?? vissuta":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono vissuti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono vissute":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "essere" or verbo == "stare":
        if pronomo == "lui" and risposta == "?? stato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "?? stata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono stati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono state":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "rimanere":
        if pronomo == "lui" and risposta == "?? rimasto":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "?? rimasta":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono rimasti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono rimaste":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "uscire":
        if pronomo == "lui" and risposta == "?? uscito":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "?? uscita":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono usciti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono uscite":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "salire":
        if pronomo == "lui" and risposta == "?? salito":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "?? salita":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono saliti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono salite":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "venire":
        if pronomo == "lui" and risposta == "?? venuto":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "?? venuta":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono venuti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono venute":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "andare":
        if pronomo == "lui" and risposta == "?? andato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "?? andata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono andati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono andate":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "cadere":
        if pronomo == "lui" and risposta == "?? caduto":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "?? caduta":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono caduti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono cadute":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "nascere":
        if pronomo == "lui" and risposta == "?? nato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "?? nata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono nati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono nate":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "vivere":
        if pronomo == "lui" and risposta == "?? divenuto":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "?? divenuta":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono divenuti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono divenute":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "diventare":
        if pronomo == "lui" and risposta == "?? diventato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "?? diventata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono diventati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono diventato":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "entrare":
        if pronomo == "lui" and risposta == "?? entrato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "?? entrata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono entrati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono entrate":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "rivenire":
        if pronomo == "lui" and risposta == "?? rivenuto":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "?? rivenuta":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono rivenuti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono rivenute":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "ritornare":
        if pronomo == "lui" and risposta == "?? ritornato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "?? ritornata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono ritornati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono ritornate":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "arrivare":
        if pronomo == "lui" and risposta == "?? arrivato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "?? arrivata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono arrivati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono arrivate":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "morire":
        if pronomo == "lui" and risposta == "?? morto":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "?? morta":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono morti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono morte":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
    elif verbo == "partire":
        if pronomo == "lui" and risposta == "?? partito":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "?? partita":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono parti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono partite":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, ?? sbagliato.  Riprova.")
        if verbo == "parlare":
            print("-ato")
        elif verbo == "vendere":
            print("-uto")
        elif verbo == "finire":
            print("-ito")
        elif verbo == "alzarsi":
            print(
                "All reflexive verbs go with ESSERE.  Transitive, Reflexive, and Casa di Essere \
                  verbs require past participle agreement in gender and number"
            )
        elif verbo == "scendere":
            print("Scendere (sceso)")
        elif verbo == "restare":
            print("Restare (restato)")
        elif verbo == "vivere":
            print("Vivere (vissuto)")
        elif verbo == "essere":
            print("Essere (stato)")
        elif verbo == "rimanere":
            print("Rimanere (rimasto)")
        elif verbo == "stare":
            print("Stare (stato)")
        elif verbo == "uscire":
            print("Uscire (uscito)")
        elif verbo == "salire":
            print("Salire (salito)")
        elif verbo == "venire":
            print("Venire (venuto)")
        elif verbo == "andare":
            print("Andare (andato)")
        elif verbo == "cadere":
            print("Cadere (caduto)")
        elif verbo == "nascere":
            print("Nascere (nato)")
        elif verbo == "divenire":
            print("Divenire (divenuto)")
        elif verbo == "diventare":
            print("Diventare (diventato)")
        elif verbo == "entrare":
            print("Entrare (entrato)")
        elif verbo == "rivenire":
            print("Rivenire (rivenuto)")
        elif verbo == "ritornare":
            print("Ritornare (ritornato)")
        elif verbo == "arrivare":
            print("Arrivare (arrivato)")
        elif verbo == "morire":
            print("Morire (morto)")
        else:
            print("Partire (partito)")

