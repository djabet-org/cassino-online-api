from __future__ import division
from datetime import datetime
from .cassino_database_manager import (
    fetch_crash_points,
    fetch_how_many_crash_points,
    fetch_double_rolls,
)


def get_estrategias(velas=[], qtd_galho=2):
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
            "padrao_soma_digitos_6x": probabilidade_soma_digitos_minutagem(
                velas, 6, 10
            ),
        },
        "padroes": {
            "xadrez": {
                "simples": probabilidade_padrao_xadrez(velas, 1, qtd_galho),
                "duplo": probabilidade_padrao_xadrez(velas, 2, qtd_galho),
                "triplo": probabilidade_padrao_xadrez(velas, 3, qtd_galho),
            },
            "surf": {
                "duplo": probabilidade_padrao_surf(velas, 2, qtd_galho),
                "triplo": probabilidade_padrao_surf(velas, 3, qtd_galho),
                "quadruplo": probabilidade_padrao_surf(velas, 4, qtd_galho),
            },
        },
    }


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


def probabilidade_padrao_surf(velas, qtdPadrao, galho):
    hit = total = 0
    for i in range(len(velas)):
        selectedVelas = velas[i : i + qtdPadrao]
        if not all(
            vela["vela"] >= 2 for vela in selectedVelas
        ):
            continue
        velas2 = velas[i + qtdPadrao : i + qtdPadrao + galho + 1]
        if any(vela["vela"] >= 2 for vela in velas2):
            hit += 1
        total += 1
    return "0%" if not total else "{:.0%}".format(hit / total)


def probabilidade_padrao_xadrez(velas, length, galho):
    hit = total = 0
    for i in range(len(velas)):
        indexEnd = i + length * 2
        selectedVelas = velas[i:indexEnd]
        mappedVelas = list(map(lambda vela: vela["vela"] >= 2, selectedVelas))
        if mappedVelas != [True, False] * length:
            continue
        galhos = velas[indexEnd : indexEnd + galho + 1]
        if any(vela["vela"] >= 2 for vela in galhos):
            hit += 1
        total += 1
    return "0%" if not total else "{:.0%}".format(hit / total)


def _isGreen(velaObj):
    return velaObj["vela"] >= 2


def probabilidade_soma_digitos_minutagem(velas, minVela, maxVela):
    found_vela = None
    vela_entrada = None
    tries = 0
    hit = 0
    galhos = []
    for vela in velas:
        if not found_vela and vela["vela"] >= minVela and vela["vela"] < maxVela:
            found_vela = vela
            continue

        if found_vela:
            vela_entrada = found_vela
            velaCreatedDate = datetime.fromtimestamp(vela["created"])
            velaFoundCreatedDate = datetime.fromtimestamp(found_vela["created"])
            minutes_diff = (velaCreatedDate - velaFoundCreatedDate).total_seconds() / 60
            if minutes_diff >= _sumDigits(found_vela["vela"]):
                if len(galhos) < 2:
                    galhos.append(vela["vela"])
                    continue

                tries += 1
                if any(v > 3 for v in galhos):
                    hit += 1
                found_vela = None
                galhos = []

    return {
        "assertividade": "0%" if hit == tries == 0 else "{:.0%}".format(hit / tries),
        "vela_selecionada": vela_entrada["vela"] if vela_entrada else "Nenhuma",
    }


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


def _probabilidade_padrao_minutagem(velas, minVela, maxVela, minutos):
    found_vela = None
    tries = 0
    hit = 0
    galhos = []
    vela_entrada = None

    for vela in velas:
        if not found_vela and vela["vela"] >= minVela and vela["vela"] < maxVela:
            found_vela = vela
            continue

        if found_vela:
            vela_entrada = found_vela
            velaCreated1 = datetime.fromtimestamp(vela["created"])
            velaCreated2 = datetime.fromtimestamp(found_vela["created"])

            minutes_diff = (velaCreated1 - velaCreated2).total_seconds() / 60
            if minutes_diff >= minutos:
                if len(galhos) < 2:
                    galhos.append(vela["vela"])
                    continue

                tries += 1
                if any(v > 2 for v in galhos):
                    hit += 1
                found_vela = None
                galhos = []

    return {
        "assertividade": "0%" if hit == tries == 0 else "{:.0%}".format(hit / tries),
        "vela_selecionada": vela_entrada["vela"] if vela_entrada else "Nenhuma",
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
