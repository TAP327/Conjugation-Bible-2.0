"""''
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
        Andare (andato)         Arrivare (arrivato)     Cadere (caduto)
        Divenire (divenuto)     Diventare (diventato)   Entrare (entrato)       
        Essere (stato)          Esistere (esistito)     Morire (morto)          
        Nascere (nato)          Occorrere (occorso)     Partire (partito)       
        Restare (restato)       Rimanere (rimasto)      Ritornare (ritornato)   
        Rivenire (rivenuto)     Scappare (scappato)     Scendere (sceso)        
        Stare (stato)           Svanire (svanito)       Tornare (tornato)       
        Uscire (uscito)         Venire (venito)         

    Altri Weirdi
        Chiedere (chiesto)      Chiudere (chiuso)       Dire (detto)            
        Rompere (rotto)         Vivere (vissuto)

*Combinare con i verbi ausiliari imperfetti per creare il trapassato prossimo
ESSERE: ero, eri, era, eravamo, eravate, erano
AVERE:  avevo, avevi, aveva, avevamo, avevate, avevano
""" ""
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
        "tornare",
        "ritornare",
        "arrivare",
        "morire",
        "partire",
        "esistere",
        "occorrere",
        "scappare",
        "svanire"
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
            print("Mi dispiace, è sbagliato.  Riprova.")
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
            print("Mi dispiace, è sbagliato.  Riprova.")
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
            print("Mi dispiace, è sbagliato.  Riprova.")
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
            print("Mi dispiace, è sbagliato.  Riprova.")
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
            print("Mi dispiace, è sbagliato.  Riprova.")
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
            print("Mi dispiace, è sbagliato.  Riprova.")
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
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "alzarsi":
        if pronomo == "lui" and risposta == "si è alzato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "si è alzata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "si sono alzati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "si sono alzate":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "scendere":
        if pronomo == "lui" and risposta == "è sceso":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è scesa":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono scesi":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono scese":
            print("Corretto!")
        else:
            print(
                "Casa di Essere: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "restare":
        if pronomo == "lui" and risposta == "è restato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è restata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono restati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono restate":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "vivere":
        if pronomo == "lui" and risposta == "è vissuto":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è vissuta":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono vissuti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono vissute":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "essere" or verbo == "stare":
        if pronomo == "lui" and risposta == "è stato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è stata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono stati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono state":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "rimanere":
        if pronomo == "lui" and risposta == "è rimasto":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è rimasta":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono rimasti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono rimaste":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "uscire":
        if pronomo == "lui" and risposta == "è uscito":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è uscita":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono usciti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono uscite":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "salire":
        if pronomo == "lui" and risposta == "ha salito":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "ha salito":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "hanno salito":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "hanno salito":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "venire":
        if pronomo == "lui" and risposta == "è venuto":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è venuta":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono venuti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono venute":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "andare":
        if pronomo == "lui" and risposta == "è andato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è andata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono andati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono andate":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "cadere":
        if pronomo == "lui" and risposta == "è caduto":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è caduta":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono caduti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono cadute":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "nascere":
        if pronomo == "lui" and risposta == "è nato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è nata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono nati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono nate":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "vivere":
        if pronomo == "lui" and risposta == "è divenuto":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è divenuta":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono divenuti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono divenute":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "diventare":
        if pronomo == "lui" and risposta == "è diventato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è diventata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono diventati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono diventato":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "entrare":
        if pronomo == "lui" and risposta == "è entrato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è entrata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono entrati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono entrate":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "rivenire":
        if pronomo == "lui" and risposta == "è rivenuto":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è rivenuta":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono rivenuti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono rivenute":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "ritornare":
        if pronomo == "lui" and risposta == "è ritornato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è ritornata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono ritornati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono ritornate":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "arrivare":
        if pronomo == "lui" and risposta == "è arrivato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è arrivata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono arrivati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono arrivate":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "morire":
        if pronomo == "lui" and risposta == "è morto":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è morta":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono morti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono morte":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
    elif verbo == "partire":
        if pronomo == "lui" and risposta == "è partito":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è partita":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono parti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono partite":
            print("Corretto!")
    elif verbo == "esistere":
        if pronomo == "lui" and risposta == "è esistito":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è esistita":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono esistiti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono esistite":
            print("Corretto!")
    elif verbo == "occurrere":
        if pronomo == "lui" and risposta == "è occurso":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è occursa":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono occursi":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono occurse":
            print("Corretto!")
    elif verbo == "tornare":
        if pronomo == "lui" and risposta == "è tornato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è tornata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono tornati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono tornate":
            print("Corretto!")
    elif verbo == "scappare":
        if pronomo == "lui" and risposta == "è scappato":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è scappata":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono scappati":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono scappate":
            print("Corretto!")
    elif verbo == "svanire":
        if pronomo == "lui" and risposta == "è svanito":
            print("Corretto!")
        elif pronomo == "lei" and risposta == "è svanita":
            print("Corretto!")
        elif pronomo == "loro (m.)" and risposta == "sono svaniti":
            print("Corretto!")
        elif pronomo == "loro (f.)" and risposta == "sono svanite":
            print("Corretto!")
        else:
            print(
                "Verbi Riflessivi: pronomo riflessivo + essere (presente) + participio passato"
            )
            print("Mi dispiace, è sbagliato.  Riprova.")
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
        elif verbo == "partire":
            print("Partire (partito)")
        elif verbo == "dire":
            print("Dire (detto)")
        elif verbo == "chiedere":
            print("Chiedere (chiesto)")
        elif verbo == "chiudere":
            print ("Chiudere (chiuso)")
        elif verbo == "esistere":
            print ("Esistere: esistito")
        elif verbo == "occorrere":
            print("Occorrere (occurso)")
        elif verbo == "rompere":
            print("Rompere (rotto)")
        elif verbo == "scappare":
            print("Scappare (scappato)")
        elif verbo == "svanire":
            print("Svanire (svanito)")
        else:
            print("Tornare (tornato)")
