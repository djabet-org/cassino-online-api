from __future__ import division
import datetime
from .cassino_database_manager import fetch_crash_points

def get_estrategias(qtd_velas):
    # Padrao a => 5x3min
    # Padrao b => 10x3min
    # Padrao c => 5x5min
    # Padrao d => 10x5min
    # Padrao e => 3x + soma digitos + add no tempo

    return {
        "a": _probabilidade_padrao_minutagem(qtd_velas, 5, 10, 3),
        "b": _probabilidade_padrao_minutagem(qtd_velas, 10, 50, 3),
        "c": _probabilidade_padrao_minutagem(qtd_velas, 5, 10, 5),
        "d": _probabilidade_padrao_minutagem(qtd_velas, 10, 50, 5),
        "e": probabilidade_soma_digitos_minutagem(qtd_velas, 3, 4)
    }

def probabilidade_soma_digitos_minutagem(qtd_velas, minVela, maxVela):
    velas = list(reversed(fetch_crash_points(qtd_velas)))
    found_vela = None
    tries = 0
    hit = 0
    galhos = []

    for vela in velas:
        if not found_vela and vela[0] >= minVela and vela[0] < maxVela:
            found_vela = vela
            continue
        
        if found_vela:
            vela_entrada = found_vela
            minutes_diff = (vela[1] - found_vela[1]).total_seconds() / 60
            if minutes_diff >= _sumDigits(found_vela[0]):
                if len(galhos) < 2:
                    galhos.append(vela[0])
                    continue

                tries += 1
                if (any( v > 3 for v in galhos)):                
                    hit += 1
                found_vela = None
                galhos = []
   
    return {
        "assertividade": "0%" if hit == tries == 0 else "{:.0%}".format(hit/tries),
        "vela_selecionada": vela_entrada[0]
    }

def media_intervalo_tempo(velas = []):
    if not velas or len(velas) == 1:
        return "Nenhuma."
    
    qtd_intervals = 0
    seconds_total = 0
    for i in range(len(velas)-1):
        velaCreated1 = datetime.datetime.strptime(velas[i]["created"], "%a, %d %b %Y %H:%M:%S GMT")
        velaCreated2 = datetime.datetime.strptime(velas[i+1]["created"], "%a, %d %b %Y %H:%M:%S GMT")
        seconds_diff = (velaCreated1 - velaCreated2).total_seconds()
        seconds_total += seconds_diff
        qtd_intervals += 1
    
    return '{0:.2f}min'.format((seconds_total/qtd_intervals) / 60)

def media_velas(qtd_velas):
    intervalos = dict()
    velas3x = _fetch_crash_points_at_least(qtd_velas, 3, 5)
    velas5x = _fetch_crash_points_at_least(qtd_velas, 5, 10)
    velas10x = _fetch_crash_points_at_least(qtd_velas, 10,100)
    velas100x = _fetch_crash_points_at_least(qtd_velas, 100, 1000)

    intervalos['3x'] = media_intervalo_tempo(velas3x)
    intervalos['5x'] = media_intervalo_tempo(velas5x)
    intervalos['10x'] = media_intervalo_tempo(velas10x)
    intervalos['100x'] = media_intervalo_tempo(velas100x)

    return intervalos 

def fetch_contagem_cores(qtd_velas):
    velas = fetch_crash_points(qtd_velas)
    contagem = dict()
    qtdPreta = qtdVerde = 0

    for vela in velas:
        if vela >= 2:
            qtdVerde += 1
        else:
            qtdPreta += 1

    contagem['qtdPreta'] = qtdPreta
    contagem['qtdVerde'] = qtdVerde
    contagem['percentagePreta'] = "{:.0%}".format(qtdPreta/int(qtd_velas))
    contagem['percentageVerde'] = "{:.0%}".format(qtdVerde/int(qtd_velas))

    return contagem

def fetch_velas(qtd_velas):
    return list(map( lambda velaObg: { "vela": velaObg[0], "created": velaObg[1]}, fetch_crash_object(qtd_velas)))

def _probabilidade_padrao_minutagem(qtd_velas, minVela, maxVela, minutos):
    velas = list(reversed(fetch_crash_points(qtd_velas)))
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

def fetch_contagem_cores(qtd_velas):
    velas = fetch_crash_points(qtd_velas)
    contagem = dict()
    qtdPreta = qtdVerde = 0

    for vela in velas:
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
    return list(map( lambda velaObg: { "vela": velaObg["vela"], "platform": velaObg["platform"], "created": velaObg["created"]}, fetch_crash_points(qtd_velas)))

def _fetch_crash_points_at_least( howMany, atLeast, atMost):
    return list(filter( lambda vela: vela["vela"] >= atLeast and vela["vela"] < atMost, fetch_crash_points(howMany)))
def _sumDigits(n):
    strr = str(n)
    list_of_number = list(map( lambda n: int(n) if n.isnumeric() else 0, strr.strip()))
    return sum(list_of_number)
