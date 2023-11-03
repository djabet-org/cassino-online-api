from __future__ import division
from datetime import datetime
from ..cassino_database_manager import fetch_crash_points
from .helper import (
    _build_padroes,
    _probabilidade_padrao,
    _mapPadraoFromVelas,
    _mapMinutosProbabilidades,
    _fetch_crash_points_at_least,
    _media_vela_tempo,
    _vela_in_range,
    _minutesDiff,
    _anyGreen,
    _minutosProbabilidades,
    _isGreen,
)


def get_estrategias(search_filter={}):
    velas = search_filter.get("velas", [])
    result = {
        "minutagem": {
            "minutos_fixo": probabilidade_padrao_minutos_fixo(search_filter),
            "intervalos": probabilidade_padrao_minutos_intervalos(search_filter),
            "intervalos_para_vela": {"vela": intervalos_para_vela(search_filter)},
        },
        "padroes": _build_padroes(search_filter),
        "entrada_agora": {
            "probabilidade": _probabilidade_padrao(
                _mapPadraoFromVelas(velas[-4:]), search_filter
            ),
            "padrao": _mapPadraoFromVelas(velas[-4:]),
        },
        "ciclos": catalogar_ciclos(velas),
    }

    # for minuto in ["3", "4", "5"]:
    #     result["minutagem"]["intervalos_para_vela"]["vela"]["3x"]["minuto"].pop(
    #         minuto, None
    #     ) if result["minutagem"]["intervalos_para_vela"]["vela"]["3x"]["minuto"][
    #         minuto
    #     ][
    #         "probabilidade"
    #     ] < minProbabilidade else 0
    #     result["minutagem"]["intervalos_para_vela"]["vela"]["5x"]["minuto"].pop(
    #         minuto, None
    #     ) if result["minutagem"]["intervalos_para_vela"]["vela"]["5x"]["minuto"][
    #         minuto
    #     ][
    #         "probabilidade"
    #     ] < minProbabilidade else 0
    #     result["minutagem"]["intervalos_para_vela"]["vela"]["10x"]["minuto"].pop(
    #         minuto, None
    #     ) if result["minutagem"]["intervalos_para_vela"]["vela"]["10x"]["minuto"][
    #         minuto
    #     ][
    #         "probabilidade"
    #     ] < minProbabilidade else 0

    return result


def catalogar_ciclos(velas=[]):
    ciclos_count = {"continuo": 0, "alternado": 0}
    ciclos = []
    for i in range(0, len(velas) - 3, 3):
        ciclo = list(map(lambda v: v["vela"], velas[i : i + 3]))
        ciclos.append(ciclo)

    print(ciclos)
    for ciclo in ciclos[-10:]:
        if all(x < 2 for x in ciclo) or all(x >= 2 for x in ciclo):
            ciclos_count["continuo"] += 1
        else:
            ciclos_count["alternado"] += 1

    return ciclos_count


def probabilidade_padrao_minutos_intervalos(search_filter={}):
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
    velas = search_filter.get("velas", [])
    for i in range(len(velas) - 1):
        vela = velas[i]
        dt_object = datetime.fromtimestamp(vela["created"])
        minute = dt_object.minute
        for key in result:
            if not minute % key:
                galhos = velas[i : i + search_filter["qtd_galho"] + 1]
                if any(g["vela"] >= search_filter["target_vela"] for g in galhos):
                    result[key]["hit"] += 1
                result[key]["tried"] += 1

    return _mapMinutosProbabilidades(result)


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


def fetch_contagem_cores(velas=[]):
    global last_time_alert_sent

    contagem = dict()
    qtdPreta = qtd_verde = 0
    qtd_velas = len(velas)

    for vela in velas:
        if vela["vela"] >= 2:
            qtd_verde += 1
        else:
            qtdPreta += 1

    contagem["qtdPreta"] = qtdPreta
    contagem["qtdVerde"] = qtd_verde
    contagem["percentagePreta"] = "{:.0%}".format(qtdPreta / int(qtd_velas))
    contagem["percentageVerde"] = "{:.0%}".format(qtd_verde / int(qtd_velas))

    return contagem


def media_velas(velas=[]):
    intervalos = dict()
    velas2x = _fetch_crash_points_at_least(velas, 2, 3)
    velas3x = _fetch_crash_points_at_least(velas, 3, 5)
    velas5x = _fetch_crash_points_at_least(velas, 5, 10)
    velas10x = _fetch_crash_points_at_least(velas, 10, 100)
    velas100x = _fetch_crash_points_at_least(velas, 100, 1000)

    intervalos["2x"] = {
        "qtd": len(velas2x),
        "media": int(len(velas2x) / len(velas) * 100),
        "media_tempo": _media_vela_tempo(velas2x),
    }

    intervalos["3x"] = {
        "qtd": len(velas3x),
        "media": int(len(velas3x) / len(velas) * 100),
        "media_tempo": _media_vela_tempo(velas3x),
    }

    intervalos["5x"] = {
        "qtd": len(velas5x),
        "media": int(len(velas5x) / len(velas) * 100),
        "media_tempo": _media_vela_tempo(velas5x),
    }
    intervalos["10x"] = {
        "qtd": len(velas10x),
        "media": int(len(velas10x) / len(velas) * 100),
        "media_tempo": _media_vela_tempo(velas10x),
    }
    intervalos["100x"] = {
        "qtd": len(velas100x),
        "media": int(len(velas100x) / len(velas) * 100),
        "media_tempo": _media_vela_tempo(velas100x),
    }

    return intervalos


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
    }


def probabilidade_padrao_intervalos_para_velaX(
    rangeTarget, afterQtdMinutes, search_filters
):
    tries = 0
    hit = 0
    velas = search_filters["velas"]
    qtd_galho = search_filters["qtd_galho"]
    target_vela = search_filters["target_vela"]
    min_probabilidade = search_filters["min_probabilidade"]

    nextCheckIndex = 0
    for i in range(len(velas)):
        if i < nextCheckIndex:
            continue
        vela = velas[i]
        if not _vela_in_range(vela, rangeTarget):
            continue
        tries += 1
        for i2 in range(i + 1, len(velas)):
            vela2 = velas[i2]
            if _minutesDiff(vela, vela2) < afterQtdMinutes:
                continue
            velas_to_be_verified = velas[i2 : i2 + qtd_galho + 1]
            if _anyGreen(velas_to_be_verified, target_vela):
                hit += 1
            nextCheckIndex = i2 + qtd_galho + 1
            break

    probabilidade = int(0 if tries == 0 else (hit / tries) * 100)
    return {"hit": hit, "tried": tries, "probabilidade": probabilidade}


def probabilidade_padrao_minutos_fixo(search_filter={}):
    velas = search_filter.get("velas", [])
    qtd_galho = search_filter.get("qtd_galho", 0)
    target_vela = search_filter.get("target_vela", 0)
    last_minute = None

    minutosProbabilidades = _minutosProbabilidades()
    for i in range(0, len(velas), qtd_galho + 1):
        vela = velas[i]
        velaMinute = datetime.fromtimestamp(vela["created"]).minute % 10
        if last_minute == velaMinute:
            continue
        velasToVerify = velas[i : qtd_galho + 1]
        minutosProbabilidades[velaMinute]["hit"] += (
            1 if any(_isGreen(vela, target_vela) for vela in velasToVerify) else 0
        )
        minutosProbabilidades[velaMinute]["tried"] += 1
        last_minute = velaMinute

    return _mapMinutosProbabilidades(minutosProbabilidades)


def intervalos_para_vela(search_filter):
    velasMinutos = {
        "3x": {
            "minuto": {
                "3": probabilidade_padrao_intervalos_para_velaX(
                    [3, 5], 3, search_filter
                ),
                "4": probabilidade_padrao_intervalos_para_velaX(
                    [3, 5], 4, search_filter
                ),
                "5": probabilidade_padrao_intervalos_para_velaX(
                    [3, 5], 5, search_filter
                ),
            }
        },
        "5x": {
            "minuto": {
                "3": probabilidade_padrao_intervalos_para_velaX(
                    [5, 10], 3, search_filter
                ),
                "4": probabilidade_padrao_intervalos_para_velaX(
                    [5, 10], 4, search_filter
                ),
                "5": probabilidade_padrao_intervalos_para_velaX(
                    [5, 10], 5, search_filter
                ),
            }
        },
        "10x": {
            "minuto": {
                "3": probabilidade_padrao_intervalos_para_velaX(
                    [10, 50], 3, search_filter
                ),
                "4": probabilidade_padrao_intervalos_para_velaX(
                    [10, 50], 4, search_filter
                ),
                "5": probabilidade_padrao_intervalos_para_velaX(
                    [10, 50], 5, search_filter
                ),
            }
        },
    }

    # filteredVelasMinutes = {vela: velasMinutos[] for vela, minuto in velasMinutos.items() if velasMinutos[vela][minuto]}
    return velasMinutos