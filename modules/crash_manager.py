from __future__ import division
from datetime import datetime
from .cassino_database_manager import fetch_crash_points, fetch_how_many_crash_points, fetch_double_rolls


def get_estrategias(velas=[]):

    return {
        "apos_Xx": {
            "padrao_vela_apos3x": probabilidade_aposXx(velas, 3, 4, 1),
            "padrao_vela_apos4x": probabilidade_aposXx(velas, 4, 5, 1),
            "padrao_vela_apos5x": probabilidade_aposXx(velas, 5, 10, 1),
            "padrao_vela_apos10x": probabilidade_aposXx(velas, 10, 50, 1),
            "padrao_vela_apos50x": probabilidade_aposXx(velas, 50, 100, 1),
            "padrao_vela_apos100x": probabilidade_aposXx(velas, 100, 2000, 1),
        },
        "minutagem": {
            "padrao_min_3x_3min": _probabilidade_padrao_minutagem(velas, 3, 5, 3),
            "padrao_min_3x_4min": _probabilidade_padrao_minutagem(velas, 3, 5, 4),
            "padrao_min_3x_5min": _probabilidade_padrao_minutagem(velas, 3, 5, 5),
            "padrao_min_5x_3min": _probabilidade_padrao_minutagem(velas, 5, 10, 3),
            "padrao_min_5x_4min": _probabilidade_padrao_minutagem(velas, 5, 10, 4),
            "padrao_min_5x_5min": _probabilidade_padrao_minutagem(velas, 5, 10, 5),
            "padrao_min_10x_3min": _probabilidade_padrao_minutagem(velas, 10, 50, 3),
            "padrao_min_10x_4min": _probabilidade_padrao_minutagem(velas, 10, 50, 4),
            "padrao_min_10x_5min": _probabilidade_padrao_minutagem(velas, 10, 50, 5),
        },
        "soma_digitos": {
            "padrao_soma_digitos_3x": probabilidade_soma_digitos_minutagem(velas, 3, 4),
            "padrao_soma_digitos_4x": probabilidade_soma_digitos_minutagem(velas, 4, 5),
            "padrao_soma_digitos_5x": probabilidade_soma_digitos_minutagem(velas, 5, 6),
            "padrao_soma_digitos_6x": probabilidade_soma_digitos_minutagem(velas, 6, 10)
        },
         "apos_padrao_surf": {
            "duplo": probabilidade_aposPadrao(velas, 2, 2, 3, 2),
        },
    }


def probabilidade_aposXx(velas, velaMin, velaMax, galho):
    achou = False
    tries = 0
    hit = 0
    for i in range(len(velas)-1):
        vela = velas[i]['vela']
        if not achou and vela >= velaMin and vela < velaMax:
            achou = True
            tries += 1
        if achou:
            targetVelas = velas[i+1:i+2+galho]
            anyGreen = any(_isGreen(targetVela) for targetVela in targetVelas)
            if anyGreen:
                hit += 1
            achou = False
    return {
        "assertividade": "0%" if not hit and not tries else "{:.0%}".format(hit/tries)
    }

def probabilidade_aposPadrao(velas, qtdPadrao, min, max, galho):
    hit = total = 0
    for i in range(len(velas)):
        selectedVelas = velas[i:i+qtdPadrao]
        print('selectedVelas ', selectedVelas)
        if not all(vela['vela'] >= min and vela['vela'] <= max for vela in selectedVelas):
            continue
        velas2 = velas[i+qtdPadrao:i+qtdPadrao+galho+1]
        print(velas2)
        if any(vela['vela'] >= 2 for vela in velas2):
            hit += 1
        total += 1
    return "0%" if not total else "{:.0%}".format(hit/total)


def _isGreen(velaObj):
    return velaObj['vela'] >= 2


def probabilidade_soma_digitos_minutagem(velas, minVela, maxVela):
    found_vela = None
    vela_entrada = None
    tries = 0
    hit = 0
    galhos = []
    for vela in velas:
        if not found_vela and vela['vela'] >= minVela and vela['vela'] < maxVela:
            found_vela = vela
            continue

        if found_vela:
            vela_entrada = found_vela
            velaCreatedDate = datetime.fromtimestamp(vela["created"])
            velaFoundCreatedDate = datetime.fromtimestamp(
                found_vela["created"])
            minutes_diff = (velaCreatedDate -
                            velaFoundCreatedDate).total_seconds() / 60
            if minutes_diff >= _sumDigits(found_vela['vela']):
                if len(galhos) < 2:
                    galhos.append(vela['vela'])
                    continue

                tries += 1
                if (any(v > 3 for v in galhos)):
                    hit += 1
                found_vela = None
                galhos = []

    return {
        "assertividade": "0%" if hit == tries == 0 else "{:.0%}".format(hit/tries),
        "vela_selecionada": vela_entrada['vela'] if vela_entrada else 'Nenhuma'
    }


def media_intervalo_tempo(velas=[]):
    if not velas or len(velas) == 1:
        return "Nenhuma."

    qtd_intervals = 0
    seconds_total = 0
    for i in range(len(velas)-1):
        velaCreated1 = datetime.fromtimestamp(velas[i]["created"])
        velaCreated2 = datetime.fromtimestamp(velas[i+1]["created"])
        seconds_diff = (velaCreated2 - velaCreated1).total_seconds()
        seconds_total += seconds_diff
        qtd_intervals += 1

    return '{0:.2f}min'.format((seconds_total/qtd_intervals) / 60)


def media_velas(velas=[]):
    intervalos = dict()
    velas3x = _fetch_crash_points_at_least(velas, 3, 5)
    velas5x = _fetch_crash_points_at_least(velas, 5, 10)
    velas10x = _fetch_crash_points_at_least(velas, 10, 100)
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
            velaCreated1 = datetime.fromtimestamp(vela["created"])
            velaCreated2 = datetime.fromtimestamp(found_vela["created"])

            minutes_diff = (velaCreated1 - velaCreated2).total_seconds() / 60
            if minutes_diff >= minutos:
                if len(galhos) < 2:
                    galhos.append(vela['vela'])
                    continue

                tries += 1
                if (any(v > 2 for v in galhos)):
                    hit += 1
                found_vela = None
                galhos = []

    return {
        "assertividade": "0%" if hit == tries == 0 else "{:.0%}".format(hit/tries),
        "vela_selecionada": vela_entrada['vela'] if vela_entrada else 'Nenhuma'
    }


def fetch_contagem_cores(velas=[]):
    contagem = dict()
    qtdPreta = qtdVerde = 0
    qtd_velas = len(velas)

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

def calculate_rolls_distribution(rolls=[]):
    contagem = dict()
    qtdPreta = qtdVermelha = qtdBranca = 0
    qtd_rolls = len(rolls)

    for roll in rolls:
        if roll["color"] == "red":
            qtdVermelha += 1
        elif roll["color"] == "black":
            qtdPreta += 1
        else:
            qtdBranca += 1    

    contagem['qtdPreta'] = qtdPreta
    contagem['qtdVermelha'] = qtdVermelha
    contagem['qtdBranca'] = qtdBranca
    contagem['percentagePreta'] = "{:.0%}".format(qtdPreta/int(qtd_rolls))
    contagem['percentageVermelha'] = "{:.0%}".format(qtdVermelha/int(qtd_rolls))
    contagem['percentageBranca'] = "{:.0%}".format(qtdBranca/int(qtd_rolls))

    return contagem

def calculate_roll_next_color_probability(rolls = []):
    result = dict({
        0: [0,0,0,0],
        1: [0,0,0,0],
        2: [0,0,0,0],
        3: [0,0,0,0],
        4: [0,0,0,0],
        5: [0,0,0,0],
        6: [0,0,0,0],
        7: [0,0,0,0],
        8: [0,0,0,0],
        9: [0,0,0,0],
        10: [0,0,0,0],
        11: [0,0,0,0],
        12: [0,0,0,0],
        13: [0,0,0,0],
        14: [0,0,0,0],
      }
    )

    for i in range(len(rolls)-1):
        roll = rolls[i]
        print(roll)
        x = result[roll["roll"]]
        next_desired_rolls = rolls[i+1:i+4]
        anyRed = any( r["color"] == "red" for r in next_desired_rolls )
        anyBlack = any( r["color"] == "black" for r in next_desired_rolls )
        anyWhite = any( r["color"] == "white" for r in next_desired_rolls )

        if anyRed:
            x[0] += 1
        if anyBlack:    
            x[1] += 1
        if anyWhite:    
            x[2] += 1    

        x[3] += 1    

        result[roll["roll"]] = x

    for key in result:
        value = result[key]
        result[key] = {
            'red': 0 if value[3] == 0 else int((value[0]/value[3])*100),
            'black': 0 if value[3] == 0 else int((value[1]/value[3])*100),
            'white': 0 if value[3] == 0 else int((value[2]/value[3])*100)
        }    
    
    return result    


def fetch_velas(platform, qtd_velas):
    velas = fetch_crash_points(platform, qtd_velas)
    return list(map(lambda velaObg: {"vela": velaObg["vela"], "platform": velaObg["platform"], "created": velaObg["created"]},
                    velas))


def fetch_rolls(platform, qtd_rolls):
    rolls = fetch_double_rolls(platform, qtd_rolls)
    return list(map(lambda rowRolls: {
        "roll": rowRolls["roll"],
        "platform": rowRolls["platform"],
        "created": rowRolls["created"],
        "color": rowRolls["color"]},
        rolls))

def fetch_how_many_velas():
    return fetch_how_many_crash_points()["total"]


def _fetch_crash_points_at_least(velas, atLeast, atMost):
    return list(filter(lambda vela: vela["vela"] >= atLeast and vela["vela"] < atMost, velas))


def _sumDigits(n):
    strr = str(n)
    list_of_number = list(
        map(lambda n: int(n) if n.isnumeric() else 0, strr.strip()))
    return sum(list_of_number)
