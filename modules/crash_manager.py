from __future__ import division
from datetime import datetime
from .cassino_database_manager import (
    fetch_crash_points,
    fetch_how_many_crash_points,
)


def get_estrategias(velas=[], qtd_galho=2, targetVela=2):
    return {
        "minutagem": {
            "minutos_fixo": probabilidade_padrao_minutos_fixo(
                velas, qtd_galho, targetVela
            ),
            "intervalos": probabilidade_padrao_minutos_intervalos(
                velas, qtd_galho, targetVela
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
        "padroes": {
            "xadrez": {
                "simples": probabilidade_padrao_xadrez(velas, 1, qtd_galho, targetVela),
                "duplo": probabilidade_padrao_xadrez(velas, 2, qtd_galho, targetVela),
                "triplo": probabilidade_padrao_xadrez(velas, 3, qtd_galho, targetVela),
            },
            "surf": {
                "verde": {
                    "duplo": probabilidade_padrao_surf(velas, 2, qtd_galho, targetVela),
                    "triplo": probabilidade_padrao_surf(
                        velas, 3, qtd_galho, targetVela
                    ),
                    "quadruplo": probabilidade_padrao_surf(
                        velas, 4, qtd_galho, targetVela
                    ),
                },
                "preto": {
                    "duplo": probabilidade_padrao_surf(velas, 2, qtd_galho, targetVela),
                    "triplo": probabilidade_padrao_surf(
                        velas, 3, qtd_galho, targetVela
                    ),
                    "quadruplo": probabilidade_padrao_surf(
                        velas, 4, qtd_galho, targetVela
                    ),
                },
            },
        },
    }


def probabilidade_padrao_minutos_intervalos(velas=[], galho=2, targetVela=2):
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

    for key in result:
        hitTried = result[key]
        result[key] = (
            "0%"
            if hitTried["tried"] == 0
            else "{:.0%}".format(hitTried["hit"] / hitTried["tried"])
        )

    return result


def calculate_balance(velas=[]):
    total_money = sum(vela["total_money_bets"] for vela in velas)
    total_money_won = sum(vela["total_money_bets_won"] for vela in velas)
    return round(total_money - total_money_won, 2)


def probabilidade_aposXx(velas, velaMin, velaMax, galho):
    achou = False
    tries = 0
    hit = 0
    for i in range(len(velas) - 1):
        vela = velas[i]["vela"]
        if not achou and vela >= velaMin and vela < velaMax:
            achou = True
            tries += 1
        if achou:
            targetVelas = velas[i + 1 : i + 2 + galho]
            anyGreen = any(_isGreen(targetVela) for targetVela in targetVelas)
            if anyGreen:
                hit += 1
            achou = False
    return {
        "assertividade": "0%" if not hit and not tries else "{:.0%}".format(hit / tries)
    }


def probabilidade_padrao_surf(velas = [], qtdPadrao = 4, galho = 2, targetVela = 2):
    hit = total = 0
    for i in range(len(velas)):
        selectedVelas = velas[i : i + qtdPadrao]
        if not all(vela["vela"] >= 2 for vela in selectedVelas):
            continue
        velas2 = velas[i + qtdPadrao : i + qtdPadrao + galho + 1]
        if any(vela["vela"] >= targetVela for vela in velas2):
            hit += 1
        total += 1
    return "0%" if not total else "{:.0%}".format(hit / total)


def probabilidade_padrao_xadrez(velas = [], length = 2, galho = 2, targetVela = 2):
    hit = total = 0
    for i in range(len(velas)):
        indexEnd = i + length * 2
        selectedVelas = velas[i:indexEnd]
        mappedVelas = list(map(lambda vela: vela["vela"] >= 2, selectedVelas))
        if mappedVelas != [True, False] * length:
            continue
        galhos = velas[indexEnd : indexEnd + galho + 1]
        if any(vela["vela"] >= targetVela for vela in galhos):
            hit += 1
        total += 1
    return "0%" if not total else "{:.0%}".format(hit / total)


def _isGreen(velaObj):
    return velaObj["vela"] >= 2


def media_intervalo_tempo(velas=[]):
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

    intervalos["3x"] = media_intervalo_tempo(velas3x)
    intervalos["5x"] = media_intervalo_tempo(velas5x)
    intervalos["10x"] = media_intervalo_tempo(velas10x)
    intervalos["100x"] = media_intervalo_tempo(velas100x)

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
    return {
        "assertividade": "0%" if hit == tries == 0 else "{:.0%}".format(hit / tries),
        # "vela_selecionada": vela_entrada["vela"] if vela_entrada else "Nenhuma",
    }


def probabilidade_padrao_minutos_fixo(velas=[], galho=2, targetVela=2):
    result = {
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

    for i in range(len(velas) - 1):
        vela = velas[i]
        dt_object = datetime.fromtimestamp(vela["created"])
        minute = dt_object.minute % 10
        entradas = velas[i : i + galho + 1]
        if any(entrada["vela"] >= targetVela for entrada in entradas):
            result[minute]["hit"] += 1
        result[minute]["tried"] += 1
    for key in result:
        hitTried = result[key]
        result[key] = (
            "0%"
            if hitTried["tried"] == 0
            else "{:.0%}".format(hitTried["hit"] / hitTried["tried"])
        )

    return result


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
