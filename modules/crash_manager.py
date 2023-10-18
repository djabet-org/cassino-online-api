from __future__ import division
from datetime import datetime
from .cassino_database_manager import (
    fetch_crash_points,
    fetch_how_many_crash_points,
)


def get_estrategias(velas=[], qtd_galho=2, targetVela=2, minProbabilidade=90, padroes=[]):
    result = {
        "minutagem": {
            "minutos_fixo": probabilidade_padrao_minutos_fixo(
                velas, qtd_galho, targetVela, minProbabilidade
            ),
            "intervalos": probabilidade_padrao_minutos_intervalos(
                velas, qtd_galho, targetVela, minProbabilidade
            ),
            "intervalos_para_vela": {
                "vela": {
                    "3x": {
                        "minuto": {
                            "3": probabilidade_padrao_intervalos_para_velaX(
                                velas, 3, 5, 3, targetVela
                            ),
                            "4": probabilidade_padrao_intervalos_para_velaX(
                                velas, 3, 5, 4, targetVela
                            ),
                            "5": probabilidade_padrao_intervalos_para_velaX(
                                velas, 3, 5, 5, targetVela
                            ),
                        }
                    },
                    "5x": {
                        "minuto": {
                            "3": probabilidade_padrao_intervalos_para_velaX(
                                velas, 5, 10, 3, targetVela
                            ),
                            "4": probabilidade_padrao_intervalos_para_velaX(
                                velas, 5, 10, 4, targetVela
                            ),
                            "5": probabilidade_padrao_intervalos_para_velaX(
                                velas, 5, 10, 5, targetVela
                            ),
                        }
                    },
                    "10x": {
                        "minuto": {
                            "3": probabilidade_padrao_intervalos_para_velaX(
                                velas, 10, 50, 3, targetVela
                            ),
                            "4": probabilidade_padrao_intervalos_para_velaX(
                                velas, 10, 50, 4, targetVela
                            ),
                            "5": probabilidade_padrao_intervalos_para_velaX(
                                velas, 10, 50, 5, targetVela
                            ),
                        },
                    },
                }
            },
        },
        "padroes": _build_padroes(velas, qtd_galho, targetVela, minProbabilidade, padroes)
    }

    for minuto in ["3", "4", "5"]:
        result["minutagem"]["intervalos_para_vela"]["vela"]["3x"]["minuto"].pop(
            minuto, None
        ) if result["minutagem"]["intervalos_para_vela"]["vela"]["3x"]["minuto"][
            minuto
        ][
            "probabilidade"
        ] < minProbabilidade else 0
        result["minutagem"]["intervalos_para_vela"]["vela"]["5x"]["minuto"].pop(
            minuto, None
        ) if result["minutagem"]["intervalos_para_vela"]["vela"]["5x"]["minuto"][
            minuto
        ][
            "probabilidade"
        ] < minProbabilidade else 0
        result["minutagem"]["intervalos_para_vela"]["vela"]["10x"]["minuto"].pop(
            minuto, None
        ) if result["minutagem"]["intervalos_para_vela"]["vela"]["10x"]["minuto"][
            minuto
        ][
            "probabilidade"
        ] < minProbabilidade else 0

    return result

def _build_padroes(velas, galho, targetVela, minProbabilidade, padroes=[]):
    padroesFiltrados = {}
    for padrao in padroes:
        mappedPadrao = list(map(lambda p: int(p), padrao.split(',')))
        result = probabilidade_padrao(velas, galho, targetVela, mappedPadrao)
        if result['probabilidade'] >= minProbabilidade:
            padroesFiltrados[padrao] = result
    
    return padroesFiltrados        

def probabilidade_padrao_minutos_intervalos(
    velas=[], galho=2, targetVela=2, minProbabilidade=90
):
    result = {
        3: {
            "hit": 0,
            "tried": 0,
        },
        4: {
            "hit": 0,
            "tried": 0,
        },
        5: {
            "hit": 0,
            "tried": 0,
        },
        6: {
            "hit": 0,
            "tried": 0,
        },
        7: {
            "hit": 0,
            "tried": 0,
        },
        8: {
            "hit": 0,
            "tried": 0,
        },
        9: {
            "hit": 0,
            "tried": 0,
        },
    }

    for i in range(len(velas) - 1):
        vela = velas[i]
        dt_object = datetime.fromtimestamp(vela["created"])
        minute = dt_object.minute
        for key in result:
            if not minute % key:
                galhos = velas[i : i + galho + 1]
                if any(g["vela"] >= targetVela for g in galhos):
                    result[key]["hit"] += 1
                result[key]["tried"] += 1

    return _build_minutos_probabilidades(result, minProbabilidade)


def calculate_balance(velas=[]):
    total_money = sum(vela["total_money_bets"] for vela in velas)
    total_money_won = sum(vela["total_money_bets_won"] for vela in velas)
    return round(total_money - total_money_won, 2)


def probabilidade_aposXx(velas=[], afterQtdVelas=2, targetVela=2, galho=2):
    tries = 0
    hit = 0
    for i in range(len(velas) - 1):
        vela = velas[i]["vela"]
        if vela < 10:
            continue

        entradas = velas[i + afterQtdVelas : i + afterQtdVelas + galho]
        print("vela ", vela)
        print("entradas ", entradas)
        if any(entrada["vela"] >= targetVela for entrada in entradas):
            hit += 1
        tries += 1
    return {
        "assertividade": "0%" if not hit and not tries else "{:.0%}".format(hit / tries)
    }


def probabilidade_padrao(velas, galho, targetVela, padrao=[]):
    padraoSize = len(padrao)
    hit = total = 0
    i = 0
    while i < (len(velas) - padraoSize):
        selectedVelas = list(map(lambda vela: vela['vela'], velas[i : i + padraoSize]))
        if not all( selectedVelas[i] >= padrao[i] or (padrao[i] < 2 and selectedVelas[i] < 2) for i in range(padraoSize)):
            i += 1
            continue
        # print('padrao ', padrao)
        # print('selectedVelas ', selectedVelas)
        entradas = velas[i + padraoSize : i + padraoSize + galho + 1]
        if any(entrada["vela"] >= targetVela for entrada in entradas):
            hit += 1
        total += 1
        i += (padraoSize + galho)
    probabilidade = int(0 if not total else (hit / total) * 100)
    return {"hit": hit, "tried": total, "probabilidade": probabilidade}


def probabilidade_padrao_surf(velas, galho, targetVela, minProbabilidade):
    result = {}
    for qtdSurf in [2, 3, 4]:
        padrao = [2,2]*qtdSurf
        surfProbabilidade = probabilidade_padrao(velas, galho, targetVela, padrao)
        probabilidade = surfProbabilidade['probabilidade']
        if probabilidade >= minProbabilidade:
            result[qtdSurf] = surfProbabilidade

    return result


def probabilidade_padrao_xadrez(velas, galho, targetVela, minProbabilidade):
    result = {}
    for qtdXadrez in [2, 3, 4]:
        padrao = [2,1]*qtdXadrez
        xadrezProbabilidade = probabilidade_padrao(velas, galho, targetVela, padrao)
        probabilidade = xadrezProbabilidade['probabilidade']
        if probabilidade >= minProbabilidade:
            result[qtdXadrez] = xadrezProbabilidade

    return result

def media_vela_tempo(velas=[]):
    if not velas or len(velas) == 1:
        return "Nenhuma."

    qtd_intervals = 0
    seconds_total = 0
    for i in range(len(velas) - 1):
        velaCreated1 = datetime.fromtimestamp(velas[i]["created"])
        velaCreated2 = datetime.fromtimestamp(velas[i + 1]["created"])
        seconds_diff = (velaCreated2 - velaCreated1).total_seconds()
        seconds_total += seconds_diff
        qtd_intervals += 1

    return "{0:.2f}min".format((seconds_total / qtd_intervals) / 60)


def media_velas(velas=[]):
    intervalos = dict()
    velas3x = _fetch_crash_points_at_least(velas, 3, 5)
    velas5x = _fetch_crash_points_at_least(velas, 5, 10)
    velas10x = _fetch_crash_points_at_least(velas, 10, 100)
    velas100x = _fetch_crash_points_at_least(velas, 100, 1000)

    intervalos["3x"] = media_vela_tempo(velas3x)
    intervalos["5x"] = media_vela_tempo(velas5x)
    intervalos["10x"] = media_vela_tempo(velas10x)
    intervalos["100x"] = media_vela_tempo(velas100x)

    return intervalos


def probabilidade_padrao_minutos_soma_digitos(
    velas=[], minVela=2, maxVela=2, minutos=3, galho=2, targetVela=2
):
    tries = 0
    hit = 0

    for i in range(len(velas) - 1):
        vela = velas[i]
        if vela["vela"] < minVela or vela["vela"] >= maxVela:
            continue

        auxIndex = i + 1
        while True:
            velaAux = velas[auxIndex]
            d1 = datetime.fromtimestamp(vela["created"])
            d2 = datetime.fromtimestamp(velaAux["created"])

            minutes_diff = (d2 - d1).total_seconds() / 60
            if minutes_diff >= minutos:
                break
            else:
                auxIndex += 1

        entrada = velas[auxIndex]
        galhos = [entrada] + (
            [] if galho == 0 else velas[auxIndex + 1 : auxIndex + galho + 1]
        )

        if any(g["vela"] >= targetVela for g in galhos):
            hit += 1
        tries += 1
    return {
        "assertividade": "0%" if hit == tries == 0 else "{:.0%}".format(hit / tries),
        # "vela_selecionada": vela_entrada["vela"] if vela_entrada else "Nenhuma",
    }


def probabilidade_padrao_intervalos_para_velaX(
    velas=[], minVela=2, maxVela=3, minutos=3, galho=2, targetVela=2
):
    tries = 0
    hit = 0

    for i in range(len(velas) - 1):
        vela = velas[i]
        if vela["vela"] < minVela or vela["vela"] >= maxVela:
            continue

        auxIndex = i + 1
        while auxIndex < len(velas):
            velaAux = velas[auxIndex]
            d1 = datetime.fromtimestamp(vela["created"])
            d2 = datetime.fromtimestamp(velaAux["created"])

            minutes_diff = (d2 - d1).total_seconds() / 60
            if minutes_diff >= minutos:
                break
            else:
                auxIndex += 1

        entradas = (
            [velas[auxIndex]] if galho == 0 else velas[auxIndex : auxIndex + galho + 1]
        )

        if any(entrada["vela"] >= targetVela for entrada in entradas):
            hit += 1
        tries += 1
    
    probabilidade = int(0 if tries == 0 else (hit / tries) * 100)
    return {"hit": hit, "tried": tries, "probabilidade": probabilidade}


def probabilidade_padrao_minutos_fixo(
    velas=[], galho=2, targetVela=2, minProbabilidade=90
):
    keys = {
        0: {
            "hit": 0,
            "tried": 0,
        },
        1: {
            "hit": 0,
            "tried": 0,
        },
        2: {
            "hit": 0,
            "tried": 0,
        },
        3: {
            "hit": 0,
            "tried": 0,
        },
        4: {
            "hit": 0,
            "tried": 0,
        },
        5: {
            "hit": 0,
            "tried": 0,
        },
        6: {
            "hit": 0,
            "tried": 0,
        },
        7: {
            "hit": 0,
            "tried": 0,
        },
        8: {
            "hit": 0,
            "tried": 0,
        },
        9: {
            "hit": 0,
            "tried": 0,
        },
    }
    for key in keys:
        i=0
        lastMinute = None
        while i < (len(velas) - 1):
            vela = velas[i]
            dt_object = datetime.fromtimestamp(vela["created"])
            minute = dt_object.minute % 10

            # print(f'minute != key {minute != key}! lastMinute == key {lastMinute == key}')
            if minute != key:
                lastMinute = None
                i += 1
                continue
            
            if lastMinute == minute:
                i += 1
                continue

            lastMinute = minute
            # print(dt_object)
            keys[key]["tried"] += 1
            entradas = velas[i : i + galho + 1]
            if any(entrada["vela"] >= targetVela for entrada in entradas):
                keys[key]["hit"] += 1
            i += (galho)

    return _build_minutos_probabilidades(keys, minProbabilidade)


def _build_minutos_probabilidades(result, minProbabilidade):
    keys = list(result.keys())
    probabilidades = {}
    for key in keys:
        hitTried = result[key]
        probabilidade = int(
            0 if hitTried["tried"] == 0 else (hitTried["hit"] / hitTried["tried"]) * 100
        )
        if probabilidade >= minProbabilidade:
            probabilidades[key] = hitTried
            probabilidades[key]["probabilidade"] = probabilidade

    return probabilidades


def fetch_contagem_cores(velas=[]):
    contagem = dict()
    qtdPreta = qtdVerde = 0
    qtd_velas = len(velas)

    for vela in velas:
        if vela["vela"] >= 2:
            qtdVerde += 1
        else:
            qtdPreta += 1

    contagem["qtdPreta"] = qtdPreta
    contagem["qtdVerde"] = qtdVerde
    contagem["percentagePreta"] = "{:.0%}".format(qtdPreta / int(qtd_velas))
    contagem["percentageVerde"] = "{:.0%}".format(qtdVerde / int(qtd_velas))

    return contagem


def fetch_velas(platform, qtd_velas):
    velas = fetch_crash_points(platform, qtd_velas)
    return list(
        map(
            lambda velaObg: {
                "vela": velaObg["vela"],
                "platform": velaObg["platform"],
                "created": velaObg["created"],
                "total_money_bets": velaObg["total_money_bets"],
                "total_money_bets_won": velaObg["total_money_bets_won"],
                "total_bets_placed": velaObg["total_bets_placed"],
            },
            velas,
        )
    )


def fetch_how_many_velas():
    return fetch_how_many_crash_points()["total"]


def _fetch_crash_points_at_least(velas, atLeast, atMost):
    return list(
        filter(lambda vela: vela["vela"] >= atLeast and vela["vela"] < atMost, velas)
    )


def _sumDigits(n):
    strr = str(n)
    list_of_number = list(map(lambda n: int(n) if n.isnumeric() else 0, strr.strip()))
    return sum(list_of_number)
