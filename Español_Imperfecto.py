"""''
El Imperfecto:
    -AR: -aba, -abas, -aba, -ábamos, -abais, -aban
    -ER: -ía, -ías, -ía, -íamos, -íais, -ían
    -IR: -ía, -ías, -ía, -íamos, -íais, -ían

    Verbos Irregulares:
        SER: era, eras, era, éramos, erais, eran
        IR: iba, ibas, iba, íbamos, ibais, iban
    
    Desde Hace:
        La preposición que significa 'had been': "Esperaba desde hace dos horas"
""" ""
import random


def Imperfecto():
    pronombres = ["yo", "tu", "él", "nosotros", "vosotros", "ellos"]
    verbos = [
        ["hablar", "-AR: -aba, -abas, -aba, -ábamos, -abais, -aban"],
        ["comer", "-ER: -ía, -ías, -ía, -íamos, -íais, -ían"],
        ["vivir", "-IR: -ía, -ías, -ía, -íamos, -íais, -ían"],
        ["ser", "SER: era, eras, era, éramos, erais, eran"],
        ["ir", "iba, ibas, iba, íbamos, ibais, iban"],
    ]
    pronombre = random.choice(pronombres)
    verbo = random.choice(verbos)
    if "hablar" in verbo:
        raiz = "habl"
    elif "comer" in verbo:
        raiz = "com"
    elif "vivir" in verbo:
        raiz = "viv"
    else:
        raiz = "nada"
    if verbo[0] == "hablar":
        if pronombre in ["yo", "él"]:
            sufijo = "aba"
        elif pronombre == "tu":
            sufijo = "abas"
        elif pronombre == "nosotros":
            sufijo = "ábamos"
        elif pronombre == "":
            sufijo = "vosotros"
        elif pronombre == "":
            sufijo = "abais"
        else:
            sufijo = "aban"
    elif verbo[0] in ["comer", "vivir"]:
        if pronombre in ["yo", "él"]:
            sufijo = "ía"
        elif pronombre == "tu":
            sufijo = "ías"
        elif pronombre == "nosotros":
            sufijo = "íamos"
        elif pronombre == "vosotros":
            sufijo = "íais"
        else:
            sufijo = "ían"
    elif verbo[0] == "ser":
        if pronombre in ["yo", "él"]:
            sufijo = "era"
        elif pronombre == "tu":
            sufijo = "eras"
        elif pronombre == "nosotros":
            sufijo = "éramos"
        elif pronombre == "vosotros":
            sufijo = "erais"
        else:
            sufijo = "eran"
    else:
        if pronombre in ["yo", "él"]:
            sufijo = "iba"
        elif pronombre == "tu":
            sufijo = "ibas"
        elif pronombre == "nosotros":
            sufijo = "íbamos"
        elif pronombre == "vosotros":
            sufijo = "ibais"
        else:
            sufijo = "iban"
    if raiz != "nada":
        clave = raiz + sufijo
    else:
        clave = sufijo
    respuesta = input("(" + pronombre + ") " + verbo[0] + " en el imperfecto: ")
    if respuesta.lower() != "x":
        if respuesta == clave:
            print("¡Felicitaciones!")
        else:
            print(verbo[1])
    else:
        print("¡Gracias por jugar!")
        exit()
