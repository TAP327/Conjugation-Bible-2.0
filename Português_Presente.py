'''''
O Presente:
    AR: -o, -as, -a, -amos, -ais, -am
    ER: -o, -es, -e, -emos, -eis, -em
    IR: -o, -es, -e, -imos, -is, -em

    Verbos Irregulares:
        HAVER: hei, hás, há, havemos, haveis, hão
        SER: sou, és, é, somos, sois, são
        ESTAR: estou, estás, está, estamos, estais, estão
        IR: vou, vais, vai, vamos, ides, vão
        DAR: dou, dás, dá, damos, dais, dão
        VER: vejo, vês, vê, vemos, vedes, vêem 
        VIR: venho, vens, vem, vemos, vendes, vêm
        TER: tenho, tens, tem, temos, tendes, têm
        PÔR: ponho, pões, põe, pomos, pondes, põem   (This begs the question... what about põetry?)
        VALER: valho, vales, vale, valemos, valeis, valem
        DIZER: digo, dizes, diz, dizemos, dizeis, dizem
        TRAZER: trago, trazes, traz, trazemos, trazeis, trazem
        PODER: posso, podes, pode, podemos, podeis, podem
        QUERER: quero, queres, quer, queremos, quereis, querem
        SABER: sei, sabes, sabe, sabemos, sabeis, sabem
        CABER: caibo, cabes, cabe, cabemos, cabeis, cabem
        CAIR: caio, cais, cai, caímos, caís, caem
        

        Stem Changers:
            E-I:    VESTIR: visto, vestes, veste, vestimos, vestis, vestem
                    MENTIR: minto, mentes, mente, mentimos, mentis, mentem
                    SENTIR: sinto, sentes, sente, sentimos, sentis, sentem
            O-U:    TOSSIR: tusso, tosses, tosse, tossimos, tossis, tossem
                    DORMIR: durmo, dormes, dorme, dormimos, dormis, dormem
            C-Ç:    FAZER: faço, fazes, faze, fazemos, fazeis, fazem
                    CONHECER: conheço, conheces, conhece, conhecemos, conheceis, conhecem
            G-J:    DIRIGIR: dirijo, diriges, dirige, dirigimos, dirigis, dirigem
            UIR-IR: CONSEGUIR: consigo, consegues, consegue, conseguimos, conseguis, conseguem
        
            FUGIR: fujo, foges, foge, fugimos, fugis, fogem
            TRANSGREDIR: transgrido, transgrides, transgride, transgredimos, transgredis, transgridem

        *Morrer, volver, concluir, & distinguir são regulares!
'''''
import random

def Presente():
    pronomes = ['eu', 'tu', 'ele', 'nós', 'vós', 'eles']
    verbos = [
        ['falar', 'AR: -o, -as, -a, -amos, -ais, -am'],
        ['vender', 'ER: -o, -es, -e, -emos, -eis, -em'],
        ['partir', 'IR: -o, -es, -e, -imos, -is, -em'],
        ['haver', 'HAVER: hei, hás, há, havemos, haveis, hão'],
        ['ser', 'SER: sou, és, é, somos, sois, são'],
        ['estar', 'ESTAR: estou, estás, está, estamos, estais, estão'],
        ['ir', 'IR: vou, vais, vai, vamos, ides, vão'],
        ['dar', 'DAR: dou, dás, dá, damos, dais, dão'],
        ['ver', 'VER: vejo, vês, vê, vemos, vedes, vêem '],
        ['vir', 'VIR: venho, vens, vem, vemos, vendes, vêm'],
        ['ter', 'TER: tenho, tens, tem, temos, tendes, têm'],
        ['pôr', 'PÔR: ponho, pões, põe, pomos, pondes, põem'],
        ['valer', 'VALER: valho, vales, vale, valemos, valeis, valem'],
        ['dizer', 'DIZER: digo, dizes, diz, dizemos, dizeis, dizem'],
        ['trazer', 'TRAZER: trago, trazes, traz, trazemos, trazeis, trazem'],
        ['poder', 'PODER: posso, podes, pode, podemos, podeis, podem'],
        ['querer', 'QUERER: quero, queres, quer, queremos, quereis, querem'],
        ['saber', 'SABER: sei, sabes, sabe, sabemos, sabeis, sabem'],
        ['caber', 'CABER: caibo, cabes, cabe, cabemos, cabeis, cabem'],
        ['cair', 'CAIR: caio, cais, cai, caímos, caís, caem'],
        ['vestir', 'VESTIR: visto, vestes, veste, vestimos, vestis, vestem'],
        ['mentir', 'MENTIR: minto, mentes, mente, mentimos, mentis, mentem'],
        ['sentir', 'SENTIR: sinto, sentes, sente, sentimos, sentis, sentem'],
        ['tossir', 'TOSSIR: tusso, tosses, tosse, tossimos, tossis, tossem'],
        ['dormir', 'DORMIR: durmo, dormes, dorme, dormimos, dormis, dormem'],
        ['fazer', 'FAZER: faço, fazes, faze, fazemos, fazeis, fazem'],
        ['conhecer', 'CONHECER: conheço, conheces, conhece, conhecemos, conheceis, conhecem'],
        ['dirigir', 'DIRIGIR: dirijo, diriges, dirige, dirigimos, dirigis, dirigem'],
        ['conseguir', 'CONSEGUIR: consigo, consegues, consegue, conseguimos, conseguis, conseguem'],
        ['fugir', 'FUGIR: fujo, foges, foge, fugimos, fugis, fogem'],
        ['transgredir', 'TRANSGREDIR: transgrido, transgrides, transgride, transgredimos, transgredis, transgridem'],
        ['morrer', 'MORRER: morro, morres, morre, morremos, morreis, morrem'],
        ['volver', 'VOLVER: volvo, volves, volve, volvemos, volveis, volvem'],
        ['distinguir', 'DISTINGUIR: distingo, distingues, distingue, distinguimos, distinguis, distinguem'],
        ['concluir', 'concluio, conclues, conclue, concluimos, concluis, concluem']
    ]
    pronome = random.choice(pronomes)
    verbo = random.choice(verbos)
    if verbo [0] == 'falar':
        raiz = 'fal'
    elif verbo[0] == 'vender':    
        raiz = 'vend'
    elif verbo[0] == 'partir':
        raiz = 'part'
    elif verbo[0] == 'haver':
        if pronome not in ['nós', 'vós']:
            raiz = 'h'
        else: 
            raiz = 'hav'
    elif verbo[0] == 'ser':
        raiz = ''
    elif verbo[0] == 'estar':
        raiz = 'est'
    elif verbo[0] == 'ir':
        if pronome != 'vós':
            raiz = 'v'
        else:
            raiz = ''
    elif verbo[0] == 'dar':
        raiz = 'd'
    elif verbo[0] == 'ver':
        raiz = 'v'
    elif verbo[0] == 'vir':
        raiz = 'v'
    elif verbo[0] == 'ter':
        raiz = 't'
    elif verbo[0] == 'pôr':
        raiz = 'p'
    elif verbo[0] == 'valer':
        raiz = 'val'
    elif verbo[0] == 'dizer':
        if pronome == 'eu':
            raiz = 'dig'
        else:
            raiz = 'diz'
    elif verbo[0] == 'trazer':
        if pronome == 'eu':
            raiz = 'trag'
        else:
            raiz = 'traz'
    elif verbo[0] == 'poder':
        if pronome == 'eu':
            raiz = 'poss'
        else:
            raiz = 'pod'
    elif verbo[0] == 'querer':
        raiz = 'quer'
    elif verbo[0] == 'saber':
        if pronome == 'eu':
            raiz = 's'
        else:
            raiz = 'sab'
    elif verbo[0] == 'caber':
        if pronome == 'eu':
            raiz = 'caib'
        else: 
            raiz = 'cab'
    elif verbo[0] == 'cair':
        if pronome == 'eu':
            raiz = 'cai' 
        else:
            raiz = 'ca'
    elif verbo[0] == 'vestir':
        if pronome == 'eu':
            raiz = 'vist'
        else:
            raiz = 'vest'
    elif verbo[0] == 'mentir':
        if pronome == 'eu':
            raiz = 'mint'
        else:
            raiz = 'ment'
    elif verbo[0] == 'sentir':
        if pronome == 'eu':
            raiz = 'sint'
        else:
            raiz = 'sent'
    elif verbo[0] == 'tossir':
        if pronome == 'eu':
            raiz = 'tuss'
        else:
            raiz = 'toss'
    elif verbo[0] == 'dormir':
        if pronome == 'eu':
            raiz = 'durm'
        else:
            raiz = 'dorm'
    elif verbo[0] == 'fazer':
        if pronome == 'eu':
            raiz = 'faç'
        else:
            raiz = 'faz'
    elif verbo[0] == 'conhecer':
        if pronome == 'eu':
            raiz = 'conheç'
        else:
            raiz = 'conhec'
    elif verbo[0] == 'dirigir':
        if pronome == 'eu':
            raiz = 'dirij'
        else: 
            raiz = 'dirig'
    elif verbo[0] == 'conseguir':
        if pronome == 'eu':
            raiz = 'consig' 
        else:
            raiz = 'consegu'
    elif verbo[0] == 'fugir':
        if pronome == 'eu':
            raiz = 'fuj'
        elif pronome in ['nós', 'vós']:
            raiz = 'fug'
        else:
            raiz = 'fog'
    elif verbo[0] == 'transgredir':
        if pronome not in ['nós', 'vós']:
            raiz = 'transgrid'
        else: 
            'transgred'
    elif verbo[0] == 'morrer':
        raiz = 'morr'
    elif verbo[0] == 'volver':
        raiz = 'volv'
    elif verbo[0] == 'distinguir':
        if pronome == 'eu':
            raiz = 'disting'
        else:
            raiz = 'distingu'
    else:
        raiz = 'conclu'
    if pronome == 'eu':
        if verbo[0] in ['saber', 'haver']:
            sufixo = 'ei'
        elif verbo[0] == 'ser':
            sufixo = 'sou'
        elif verbo[0] in ['estar', 'ir', 'dar']:
            sufixo = 'ou'
        elif verbo[0] == 'ver':
            sufixo = 'ejo'
        elif verbo[0] in ['vir', 'ter']:
            sufixo = 'enho'
        elif verbo[0] == 'pôr':
            sufixo = 'onho'
        elif verbo[0] == 'valer':
            sufixo = 'ho'
        elif verbo[0] == 'conluir':
            sufixo = 'io'
        else:
            sufixo = 'o'
    elif pronome == 'tu':
        if verbo[0] == 'falar':
            sufixo = 'as'
        elif verbo[0] in ['haver', 'estar', 'dar']:
            sufixo = 'ás'
        elif verbo[0] == 'ser':
            sufixo = 'és'
        elif verbo[0] == 'ir':
            sufixo = 'ais'
        elif verbo[0] == 'ver':
            sufixo = 'ês'
        elif verbo[0] in ['vir', 'ter']:
            sufixo = 'ens'
        elif verbo[0] == 'pôr':
            sufixo = 'ões'
        elif verbo[0] == 'cair':
            sufixo = 'is'
        else:
            sufixo = 'es'
    elif pronome == 'ele':
        if verbo[0] == 'falar':
            sufixo = 'a'
        elif verbo[0] in ['haver', 'estar', 'dar']:
            sufixo = 'á'
        elif verbo[0] == 'ser':
            sufixo = 'é'
        elif verbo[0] == 'ir':
            sufixo = 'ai'
        elif verbo[0] == 'ver':
            sufixo = 'ê'
        elif verbo[0] in ['vir', 'ter']:
            sufixo = 'em'
        elif verbo[0] == 'pôr':
            sufixo = 'õe'
        else:
            sufixo = 'e'
    elif pronome == 'nós':
        if verbo[0] in ['falar', 'estar', 'ir', 'dar']:
            sufixo = 'amos'
        elif verbo[0] in ['vender', 'haver', 'ver', 'vir', 'ter', 'valer', 'dizer', 'trazer', 'poder', 'querer', 'saber', 'caber', 'fazer', 'conhecer', 'morrer', 'volver']:
            sufixo = 'emos'
        elif verbo[0] == 'ser':
            sufixo = 'somos'
        elif verbo [0] == 'pôr':
            sufixo = 'omos'
        elif verbo [0] == 'cair':
            sufixo = 'ímos'
        else:
            sufixo = 'imos'
    elif pronome == 'vós':
        if verbo[0] in ['falar', 'estar' 'dar']:
            sufixo = 'ais'
        elif verbo[0] in ['vender', 'haver', 'valer', 'dizer', 'trazer', 'poder', 'querer', 'saber', 'caber', 'fazer', 'conhecer', 'morrer', 'volver']:
            sufixo = 'eis'
        elif verbo[0] == 'ser':
            sufixo = 'sois'
        elif verbo[0] == 'ir':
            sufixo = 'ides'
        elif verbo[0] == 'ver':
            sufixo = 'edes'
        elif verbo [0] in ['vir', 'ter']:
            sufixo = 'endes'
        elif verbo [0] == 'pôr':
            sufixo = 'ondes'
        elif verbo [0] == 'cair':
            sufixo = 'ís'
        else:
            sufixo = 'is'
    else:
        if verbo[0] == 'falar':
            sufixo = 'am'
        elif verbo[0] in ['haver', 'estar', 'dar', 'ir']:
            sufixo = 'ão'
        elif verbo[0] == 'ser':
            sufixo = 'são'
        elif verbo[0] == 'ir':
            sufixo = 'ão'
        elif verbo[0] == 'ver':
            sufixo = 'êem'
        elif verbo[0] in ['vir', 'ter']:
            sufixo = 'êm'
        elif verbo[0] == 'pôr':
            sufixo = 'õem'
        else:
            sufixo = 'em'
    chave = raiz + sufixo
    resposta = input('(' + pronome + ') ' + verbo + ' no presente:  ')
    if chave == resposta:
        print('Otimo!')
    elif resposta.lower() == 'x':
        print('Obrigada por jogar!')
        exit()
    else: 
        print('Eu sento, mas não está certo.')
        print(verbo[1])