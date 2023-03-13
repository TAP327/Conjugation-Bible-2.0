import random
import Español_Presente as EP
import Español_Gerundios as EG
import Español_Imperfecto as EI
import Español_Pretérito as EPret
import Italiano_Presente as IP
import Italiano_Gerundi as IG
import Italiano_Imperfetto as II
import Italiano_Passato_Prossimo as IPP


def Omnia():
    Verbum_Temporis = [
        EP.Presente(),
        EG.Gerundios(),
        EI.Imperfecto(),
        EPret.Pretérito(),
        IP.Presente(),
        IG.Gerundi(),
        II.Imperfetto(),
        IPP.Passato_Prossimo(),
    ]
    random.choice(Verbum_Temporis)


def Todos():
    Tiempos_Verbales = [
        EP.Presente(),
        EG.Gerundios(),
        EI.Imperfecto(),
        EPret.Pretérito(),
    ]
    random.choice(Tiempos_Verbales)


def Tutti():
    Tempi_Verbali = [
        IP.Presente(),
        IG.Gerundi(),
        II.Imperfetto(),
        IPP.Passato_Prossimo(),
    ]
    random.choice(Tempi_Verbali)


def Omnes_Praesentes():
    Praesentia_tempora = [EP.Presente(), IP.Presente()]
    random.choice(Praesentia_tempora)


def Omnia_Gernudia():
    Gerundia = [EG.Gerundios(), IG.Gerundi()]
    random.choice(Gerundia)


def Omnia_Imperfecta():
    Tempora_Imperfecta = [EI.Imperfecto(), II.Imperfetto()]
    random.choice(Tempora_Imperfecta)


def Omnes_Praeteriti():
    Praeteritis_Temporibus = [EPret.Pretérito(), IPP.Passato_Prossimo()]
    random.choice(Praeteritis_Temporibus)


def Romance_Dominus():
    electio = input(
        "Would you like to sort by... a. language  b. tense  c. let's practice everything!  "
    )
    if electio.lower() == "a":
        print(
            "Note: The Conjugation Bible is still under construction.  \
            Tenses in Spanish and Italian are limited, and Portuguese and French haven't been constructed yet."
        )
        elige_linguam = input(
            "Would you like to study... a. Español  b. Português  c. Italiano  d. Français  "
        )
        tempus_de_linguam = input(
            "Within your selected language, would you like to study... \
            a. Present Simple  b. Present Progressive  c. Imperfect  d. Preterite & Composite Past  e. All!  "
        )
        if elige_linguam.lower() == "a":
            if tempus_de_linguam.lower() == "a":
                while 1:
                    EP.Presente()
            elif tempus_de_linguam.lower() == "b":
                while 1:
                    EG.Gerundios()
            elif tempus_de_linguam.lower() == "c":
                while 1:
                    EI.Imperfecto()
            elif tempus_de_linguam.lower() == "d":
                while 1:
                    EPret.Pretérito()
            elif tempus_de_linguam.lower() == "e":
                while 1:
                    Todos()
            else:
                print(
                    "Lo siento, pero ese tiempo todavía no existe en la Biblia de Conjugación :("
                )
        elif elige_linguam.lower() == "b":
            print("Eu sento, mas português ainda não existe na Biblia de Conjugação :(")
        elif elige_linguam.lower() == "c":
            if tempus_de_linguam.lower() == "a":
                while 1:
                    IP.Presente()
            elif tempus_de_linguam.lower() == "b":
                while 1:
                    IG.Gerundi()
            elif tempus_de_linguam.lower() == "c":
                while 1:
                    II.Imperfetto()
            elif tempus_de_linguam.lower() == "d":
                while 1:
                    IPP.Passato_Prossimo()
            else:
                while 1:
                    Tutti()
        else:
            print(
                "Je suis désolée, mais français n'existe toujours dans la Bible de Conjugaisons :("
            )
        print("Finem programmatis. Gratias tibi!")
    elif electio == "b":
        elige_tempus = input(
            "Would you like to study... a. Present Simple  b. Present Progressive  c. Imperfect  d. Preterite & Composite Past  "
        )
        if elige_tempus.lower() == "a":
            Omnes_Praesentes()
        elif elige_tempus.lower() == "b":
            Omnia_Gernudia()
        elif elige_tempus.lower() == "c":
            Omnia_Imperfecta()
        else:
            Omnes_Praeteriti()
    else:
        print("De primo!")
        while 1:
            Omnia()


Romance_Dominus()

"""''
Next up is... 
    -Double checking the current code 
        -Adding present progressive corrections
        -Getting Spanish Present to work outside of Run & Debug
    -Starting on Spanish Imperfect :)
    -Understand Dictionaries better (working on it)

Long Term Goals:
    - Code all tenses across Spanish, Portuguese, Italian, & French
    - Have programs for each language that mix tenses, each tense that mix languages, and all tenses/languages
    - Create an executable (preferably with a UI that doesn't look like it was built in 2000)
    - Add a "See Notes" function for desperate times

return verbs.get("porre") OR return verbs["porre"]  SECONDO LUI

Stats:
    Italiano_Principale: 39 (5*1=5, 7.8)
        Italiano_Presente: 374 (28*6=168, 2.226)            Most efficient
        Italiano_Gerundi: 131 (28*1=28, 4.679)              Shortest, Least efficient
        Italiano_Imperfetto: 171 (8*6=48, 3.563)     
        Italiano_Passato_Prossimo: 484 (27*4=108, 4.48)
    Español_Principal: r/n
        Español_Presente: 494 (29*6=174, 2.839)             Longest
        Español_Gerundos: r/n
        Español_Imperfecto: r/n
        Español_Preterito: r/n
""" ""
