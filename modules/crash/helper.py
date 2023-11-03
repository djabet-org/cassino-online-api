from datetime import datetime

def _probabilidade_padrao(padrao, search_filters):
    padraoSize = len(padrao)
    hit = total = i = 0
    velas = search_filters['velas']
    qtd_galho = search_filters['qtd_galho']

    while i < (len(velas) - padraoSize):
        selectedVelas = list(map(lambda vela: vela['vela'], velas[i : i + padraoSize]))
        if not all( padrao[i] >= 2 and selectedVelas[i] >= 2 or (padrao[i] < 2 and selectedVelas[i] < 2) for i in range(padraoSize)):
            i += 1
            continue
        entradas = velas[i + padraoSize : i + padraoSize + qtd_galho + 1]
        if any(entrada["vela"] >= search_filters['target_vela'] for entrada in entradas):
            hit += 1
        total += 1
        i += (padraoSize + qtd_galho)
    probabilidade = int(0 if not total else (hit / total) * 100)
    return {"hit": hit, "tried": total, "probabilidade": probabilidade}

def _media_vela_tempo(velas=[]):
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


def _mapPadraoFromVelas(velas = []):
    return list(map(lambda v: v['vela'], velas))

def _build_padroes(search_filters):
    padroesFiltrados = {}
    for padrao in search_filters['padroes']:
        mappedPadrao = list(map(lambda p: int(p), padrao.split(',')))
        result = _probabilidade_padrao(mappedPadrao, search_filters)
        if result['probabilidade'] >= search_filters['min_probabilidade']:
            padroesFiltrados[padrao] = result
    
    return padroesFiltrados   

def _mapMinutosProbabilidades(result):
    keys = list(result.keys())
    probabilidades = {}
    for key in keys:
        hitTried = result[key]
        probabilidade = int(
            0 if hitTried["tried"] == 0 else (hitTried["hit"] / hitTried["tried"]) * 100
        )
        probabilidades[key] = hitTried
        probabilidades[key]["probabilidade"] = probabilidade

    return probabilidades

def _fetch_crash_points_at_least(velas, atLeast, atMost):
    return list(
        filter(lambda vela: vela["vela"] >= atLeast and vela["vela"] < atMost, velas)
    )


def _sumDigits(n):
    strr = str(n)
    list_of_number = list(map(lambda n: int(n) if n.isnumeric() else 0, strr.strip()))
    return sum(list_of_number)

def _isGreen(vela, target_vela):
    return vela['vela'] >= target_vela

def _anyGreen(velas, target_vela):
    return any( _isGreen(vela, target_vela) for vela in velas)

def _achouPadrao( velas_verificar, padrao):
    return padrao == velas_verificar

def _vela_in_range( vela, range):
    return range[0] <= vela['vela'] <= range[1]

def _vela_in_minute(vela, minute):
    velaMinute = datetime.fromisoformat(vela['created']).minute
    return velaMinute == minute

def _minutosProbabilidades():
    return {
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
    
def _minutesDiff(vela1, vela2):
    d1 = datetime.fromtimestamp(vela1["created"])
    d2 = datetime.fromtimestamp(vela2["created"])
    return (d2 - d1).total_seconds() / 60