import random
import Italiano_Presente as IP
import Italiano_Gerundi as IG
import Italiano_Imperfetto as II
import Italiano_Passato_Prossimo as IPP


def Tutti():
    Tempi_Verbali = [
        IP.Presente(),
        IG.Gerundi(),
        II.Imperfetto(),
        IPP.Passato_Prossimo(),
    ]
    random.choice(Tempi_Verbali)


def italian():
    selezione = input(
        "Which tense(s) would you like to practice?  a. Presente  b. Gerundi  c. Imperfetto  d. Passato Prossimo  e. Tutti   "
    )
    if selezione.lower() == "a":
        while 1:
            IP.Presente()
    elif selezione.lower() == "b":
        while 1:
            IG.Gerundi()
    elif selezione.lower() == "c":
        while 1:
            II.Imperfetto()
    elif selezione.lower() == "d":
        while 1:
            IPP.Passato_Prossimo()
    else:
        while 1:
            Tutti()


italian()

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
