'''''
Il Futturo:
    -ARE:  -erò, -erai, -erà, -eremo, -erete, -eranno
    -ERE:  -erò, -erai, -erà, -eremo, -erete, -eranno
    -IRE:  -irò, -irai, -irà, -iremo, -irete, -iranno

Il Condizionale:
    -ARE:  -erei, -eresti, -erebbe, -eremmo, -ereste, -erebbero
    -ERE:  -erei, -eresti, -erebbe, -eremmo, -ereste, -erebbero
    -IRE:  -irei, -iresti, -irebbe, -iremmo, -ireste, -irebbero

    Stem Changers:
        -GARE:  PAGARE: (pagheró, pagherei)    -CARE: CERCARE: (cercheró, chercherei)
        -GIARE: MANGIARE: (mangeró, mangerei)  -CIARE: COMINCIARE: (cominceró, comincerei)

    Ometti la primeira vocale:
        ANDARE (andró, andrei)  AVERE (avró, avrei)     CADERE (cadró, cadrei)  DOVERE (dovró, dovrei)
        POTERE (potró, potrei)  SAPERE (sapró, saprei)  VEDERE (vedró, vedrei)  VIVERE (vivró, vivrei)

    Irregulares:
        BERE (berró, berrei)    ESSERE (saró, sarei)    RIMANERE (rimarró, rimarrei)
        VENIRE (verró, verrei)  VOLERE (vorró, vorrei)
'''''
import random
Radici = {
            'PARLARE':'parler', 
            'LEGGERE':'legger', 
            'PARTIRE':'partir', 
            'FINIRE':'FINIR', 
            'PAGARE':'pagher', 
            'CERCARE':'cercher', 
            'MANGIARE':'manger', 
            'COMINCIARE':'comincer', 
            'ANDARE':'andr', 
            'AVERE':'avr', 
            'CADERE':'cadr', 
            'DOVERE':'dovr', 
            'POTERE':'potr', 
            'SAPERE':'sapr', 
            'VEDERE':'vedr', 
            'VIVERE':'vivr', 
            'BERE':'berr', 
            'ESSERE':'sar', 
            'RIMANERE':'rimarr', 
            'VOLERE':'vorr', 
            'VENIRE':'verr'
            }
def Italiano_Futuro():
    while 1:
        Suffissi = {'io':'ò', 'tu':'ai', 'lui':'à', 'nos':'emo', 'vos':'ete', 'loro':'anno'}
        radice = random.choice(list(Radici.items()))
        Pronomo = random.choice(list(Suffissi.items()))
        Risposta = input('(' + Pronomo[0] + ') ' + radice[0] + ' in il futuro:  ')
        if Risposta.lower == (radice[1] + Pronomo[1]):
            return ('Urrà!')
        elif Risposta.lower == 'x':
            exit()
        else:
            print(radice[0] + ': ' + radice[1] + Suffissi['io'] + ', ' + radice[1] + Suffissi['tu'] + ', ' + radice[1] + Suffissi['lui'] + ', ' + radice[1] + Suffissi['nos'] + ', ' + radice[1] + Suffissi['vos'] + ', ' + radice[1] + Suffissi['loro'])

def Italiano_Condizionale():
    while 1: 
        Suffissi = {'io':'ei', 'tu':'esti', 'lui':'ebbe', 'noi':'emmo', 'voi':'este', 'loro':'ebbero'}
        radice = random.choice(list(Radici.items()))
        Pronomo = random.choice(list(Suffissi.items()))
        Risposta = input('(' + Pronomo[0] + ') ' + radice[0] + ' in il condizionale:  ')
        if Risposta.lower == (radice[1].lower() + Pronomo[1]):
            print ('Figo!')
        elif Risposta.lower() == 'x':
            exit()
        else:
            print(radice[0] + ': ' + radice[1] + Suffissi['io'] + ', ' + radice[1] + Suffissi['tu'] + ', ' + radice[1] + Suffissi['lui'] + ', ' + radice[1] + Suffissi['noi'] + ', ' + radice[1] + Suffissi['voi'] + ', ' + radice[1] + Suffissi['loro'])
