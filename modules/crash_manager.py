from __future__ import division
import datetime
from .cassino_database_manager import fetch_crash_points

def get_estrategias(velas = []):

    reversedVelas = list(reversed(velas))

    return {
        "padrao_vela_apos3x": probabilidade_aposXx(reversedVelas, 3, 4, 2),
        "padrao_vela_apos4x": probabilidade_aposXx(reversedVelas, 4, 5, 2),
        "padrao_vela_apos5x": probabilidade_aposXx(reversedVelas, 5, 10, 2),
        "padrao_vela_apos10x": probabilidade_aposXx(reversedVelas, 10, 50, 2),
        "padrao_vela_apos50x": probabilidade_aposXx(reversedVelas, 50, 100, 2),
        "padrao_min_3x_3min": _probabilidade_padrao_minutagem(velas, 3, 5, 3),
        "padrao_min_3x_4min": _probabilidade_padrao_minutagem(velas, 3, 5, 4),
        "padrao_min_3x_5min": _probabilidade_padrao_minutagem(velas, 3, 5, 5),
        "padrao_min_5x_3min": _probabilidade_padrao_minutagem(velas, 5, 10, 3),
        "padrao_min_5x_4min": _probabilidade_padrao_minutagem(velas, 5, 10, 4),
        "padrao_min_5x_5min": _probabilidade_padrao_minutagem(velas, 5, 10, 5),
        "padrao_min_10x_3min": _probabilidade_padrao_minutagem(velas, 10, 50, 3),
        "padrao_min_10x_4min": _probabilidade_padrao_minutagem(velas, 10, 50, 4),
        "padrao_min_10x_5min": _probabilidade_padrao_minutagem(velas, 10, 50, 5),
        "padrao_soma_digitos_3x": probabilidade_soma_digitos_minutagem(velas, 3, 4),
        "padrao_soma_digitos_4x": probabilidade_soma_digitos_minutagem(velas, 4, 5),
        "padrao_soma_digitos_5x": probabilidade_soma_digitos_minutagem(velas, 5, 6),
        "padrao_soma_digitos_6x": probabilidade_soma_digitos_minutagem(velas, 6, 10)
    }

def probabilidade_aposXx(velas, velaMin, velaMax, galho):
    achou = False
    g = galho
    tries = 0
    hit = 0
    print(velas)
    for i in range(len(velas)):
        vela = velas[i]['vela']
        if not achou and vela >= velaMin and vela < velaMax:
            achou = True
            tries += 1
            continue
        if achou:
            if not g:
                achou = False
                continue 
            if vela >= 2:
                hit += 1
                achou = False
                continue
            g -= 1

    print(hit)
    print(tries)
    
    return {
        "assertividade": "0%" if hit == tries == 0 else "{:.0%}".format(hit/tries)
    }

def probabilidade_soma_digitos_minutagem(velas, minVela, maxVela):
    found_vela = None
    tries = 0
    hit = 0
    galhos = []

    for vela in velas:
        if not found_vela and vela['vela'] >= minVela and vela['vela'] < maxVela:
            found_vela = vela
            continue
        
        if found_vela:
            vela_entrada = found_vela
            velaCreatedDate = datetime.datetime.strptime(vela["created"], "%a, %d %b %Y %H:%M:%S GMT")
            velaFoundCreatedDate = datetime.datetime.strptime(found_vela["created"], "%a, %d %b %Y %H:%M:%S GMT")
            minutes_diff = (velaCreatedDate - velaFoundCreatedDate).total_seconds() / 60
            if minutes_diff >= _sumDigits(found_vela['vela']):
                if len(galhos) < 2:
                    galhos.append(vela['vela'])
                    continue

                tries += 1
                if (any( v > 3 for v in galhos)):                
                    hit += 1
                found_vela = None
                galhos = []
   
    return {
        "assertividade": "0%" if hit == tries == 0 else "{:.0%}".format(hit/tries),
        "vela_selecionada": vela_entrada['vela'] if vela_entrada else 'Nenhuma'
    }

def media_intervalo_tempo(velas = []):
    if not velas or len(velas) == 1:
        return "Nenhuma."
    
    qtd_intervals = 0
    seconds_total = 0
    for i in range(len(velas)-1):
        velaCreated1 = datetime.datetime.strptime(velas[i]["created"], "%a, %d %b %Y %H:%M:%S GMT")
        velaCreated2 = datetime.datetime.strptime(velas[i+1]["created"], "%a, %d %b %Y %H:%M:%S GMT")
        seconds_diff = (velaCreated2 - velaCreated1 ).total_seconds()
        seconds_total += seconds_diff
        qtd_intervals += 1
    
    return '{0:.2f}min'.format((seconds_total/qtd_intervals) / 60)

def media_velas(velas = []):
    intervalos = dict()
    velas3x = _fetch_crash_points_at_least(velas, 3, 5)
    velas5x = _fetch_crash_points_at_least(velas, 5, 10)
    velas10x = _fetch_crash_points_at_least(velas, 10,100)
    velas100x = _fetch_crash_points_at_least(velas, 100, 1000)

    intervalos['3x'] = media_intervalo_tempo(velas3x)
    intervalos['5x'] = media_intervalo_tempo(velas5x)
    intervalos['10x'] = media_intervalo_tempo(velas10x)
    intervalos['100x'] = media_intervalo_tempo(velas100x)

    return intervalos 

def _probabilidade_padrao_minutagem(velas, minVela, maxVela, minutos):
    found_vela = None
    tries = 0
    hit = 0
    galhos = []
    vela_entrada = None

    for vela in velas:
        if not found_vela and vela['vela'] >= minVela and vela['vela'] < maxVela:
            found_vela = vela
            continue
        
        if found_vela:
            vela_entrada = found_vela
            velaCreated1 = datetime.datetime.strptime(vela["created"], "%a, %d %b %Y %H:%M:%S GMT")
            velaCreated2 = datetime.datetime.strptime(found_vela["created"], "%a, %d %b %Y %H:%M:%S GMT")

            minutes_diff = (velaCreated1 - velaCreated2).total_seconds() / 60
            if minutes_diff >= minutos:
                if len(galhos) < 2:
                    galhos.append(vela['vela'])
                    continue

                tries += 1
                if (any( v > 2 for v in galhos)):                
                    hit += 1
                found_vela = None
                galhos = []
   
    return {
        "assertividade": "0%" if hit == tries == 0 else "{:.0%}".format(hit/tries),
        "vela_selecionada": vela_entrada['vela'] if vela_entrada else 'Nenhuma'
    }

def fetch_contagem_cores(velas = []):
    contagem = dict()
    qtdPreta = qtdVerde = 0
    qtd_velas = len(velas)
    reversedVelas = list(reversed(velas))

    for vela in reversedVelas:
        if vela["vela"] >= 2:
            qtdVerde += 1
        else:
            qtdPreta += 1

    contagem['qtdPreta'] = qtdPreta
    contagem['qtdVerde'] = qtdVerde
    contagem['percentagePreta'] = "{:.0%}".format(qtdPreta/int(qtd_velas))
    contagem['percentageVerde'] = "{:.0%}".format(qtdVerde/int(qtd_velas))

    return contagem

def fetch_velas(qtd_velas):
    velas = fetch_crash_points(qtd_velas)
    return list(map( lambda velaObg: { "vela": velaObg["vela"], "platform": velaObg["platform"], "created": velaObg["created"]},
                     velas))

def _fetch_crash_points_at_least( velas, atLeast, atMost):
    return list(filter( lambda vela: vela["vela"] >= atLeast and vela["vela"] < atMost, velas))

def _sumDigits(n):
    strr = str(n)
    list_of_number = list(map( lambda n: int(n) if n.isnumeric() else 0, strr.strip()))
    return sum(list_of_number)
