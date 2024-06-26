from __future__ import division
from datetime import datetime
from ..cassino_database_manager import fetch_double_rolls

def get_estrategias_double(rolls=[], galho=0, padroes = [], minProbabilidade = 0, maxProbabilidade = 100, targetColor = '*'):
    
    return {
        "numero_cor_probabilidades": calculate_roll_next_color_probability(
            rolls, galho, targetColor, minProbabilidade, maxProbabilidade
        ),
        "minutagem": {
            "intervalos": {
                "black": probabilidade_padrao_minutos_intervalos(rolls, galho, "black"),
                "red": probabilidade_padrao_minutos_intervalos(
                    rolls, galho, "red"
                ),
            },
            "fixos": {
                "black": probabilidade_padrao_minutos_fixo(rolls, galho, "black"),
                "red": probabilidade_padrao_minutos_fixo(rolls, galho, "red"),
            },
        },
        "padroes": probabilidade_padroes_cores(rolls, padroes, galho, targetColor, minProbabilidade, maxProbabilidade ),        
    }

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

    contagem["qtdPreta"] = qtdPreta
    contagem["qtdVermelha"] = qtdVermelha
    contagem["qtdBranca"] = qtdBranca
    contagem["percentagePreta"] = "{:.0%}".format(qtdPreta / int(qtd_rolls))
    contagem["percentageVermelha"] = "{:.0%}".format(qtdVermelha / int(qtd_rolls))
    contagem["percentageBranca"] = "{:.0%}".format(qtdBranca / int(qtd_rolls))

    return contagem


def calculate_balance_rolls(rolls=[]):
    balance = {
        "red": 0,
        "black": 0,
        "white": 0,
    }

    for roll in rolls:
        color = roll["color"]
        for key in balance:
            if key == color:
                balance[key] -= roll[f"total_{key}_money"]
            else:
                balance[key] += roll[f"total_{key}_money"]
            balance[key] = round(balance[key], 2)

    balance["total"] = round(balance["black"] + balance["red"] + balance["white"], 2)
    return balance


def probabilidade_padrao_minutos_intervalos(rolls=[], galho=0, desiredColor=""):
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

    for i in range(len(rolls) - 1):
        roll = rolls[i]
        dt_object = datetime.fromtimestamp(roll["created"])
        minute = dt_object.minute
        for key in result:
            if not minute % key:
                galhos = rolls[i : i + galho + 1]
                if any(g["color"] == desiredColor for g in galhos):
                    result[key]["hit"] += 1
                result[key]["tried"] += 1

    for key in result:
        hitTried = result[key]
        result[key]["probabilidade"] = (
            "0%"
            if hitTried["tried"] == 0
            else "{:.0%}".format(hitTried["hit"] / hitTried["tried"])
        )

    return result


def probabilidade_padrao_minutos_fixo(rolls=[], galho=0, desiredColor=""):
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

    for i in range(len(rolls) - 1):
        roll = rolls[i]
        dt_object = datetime.fromtimestamp(roll["created"])
        minute = dt_object.minute % 10
        galhos = rolls[i : i + galho + 1]
        if any(g["color"] == desiredColor for g in galhos):
            result[minute]["hit"] += 1
        result[minute]["tried"] += 1
        result[minute]["probabilidade"] = (
            "0%"
            if result[minute]["tried"] == 0
            else "{:.0%}".format(result[minute]["hit"] / result[minute]["tried"])
        )

    return result


def calculate_roll_next_color_probability(rolls=[], galho=0, targetColor='*', minProbabilidade=0, maxProbabilidade=100):
    result = _buildProbabilidadesMatrix(rolls, galho)
    result = _mapProbabilities(result)
    result = _filterByTargetColor(result, targetColor)
    result = _filterByMinAndMaxProbabilidade(result, minProbabilidade, maxProbabilidade)
    
    return result

def fetch_rolls(platform, qtd_rolls):
    rolls = fetch_double_rolls(platform, qtd_rolls)
    return list(
        map(
            lambda rowRolls: {
                "roll": rowRolls["roll"],
                "platform": rowRolls["platform"],
                "created": rowRolls["created"],
                "color": rowRolls["color"],
                "total_red_money": rowRolls["total_red_money"],
                "total_black_money": rowRolls["total_black_money"],
                "total_white_money": rowRolls["total_white_money"],
            },
            rolls,
        )
    )

def probabilidade_padroes_cores(rolls = [], padroes = [], galho = 0,  target_color='*', min_probabilidade = 50, max_probabilidade = 100):
    result = {}
    for padrao in padroes:
            result[padrao] = _probabilidade_padrao(rolls, padrao, galho, target_color, min_probabilidade, max_probabilidade)

    return result    

def _buildProbabilidadesMatrix(rolls = [], galho = 0):
    result = dict(
        {
            0: [0, 0, 0, 0],
            1: [0, 0, 0, 0],
            2: [0, 0, 0, 0],
            3: [0, 0, 0, 0],
            4: [0, 0, 0, 0],
            5: [0, 0, 0, 0],
            6: [0, 0, 0, 0],
            7: [0, 0, 0, 0],
            8: [0, 0, 0, 0],
            9: [0, 0, 0, 0],
            10: [0, 0, 0, 0],
            11: [0, 0, 0, 0],
            12: [0, 0, 0, 0],
            13: [0, 0, 0, 0],
            14: [0, 0, 0, 0],
        }
    )

    for i in range(len(rolls) - 1):
        roll = rolls[i]
        if not roll["roll"] in result:
            continue
        x = result[roll["roll"]]
        next_desired_rolls = rolls[i + 1 : i + galho + 2]
        anyRed = any(r["color"] == "red" for r in next_desired_rolls)
        anyBlack = any(r["color"] == "black" for r in next_desired_rolls)
        anyWhite = any(r["color"] == "white" for r in next_desired_rolls)

        if anyRed:
            x[0] += 1
        if anyBlack:
            x[1] += 1
        if anyWhite:
            x[2] += 1

        x[3] += 1

        result[roll["roll"]] = x
    
    return result    

def _filterByTargetColor( result = {}, targetColor = ''):
    if targetColor != '*':
        filteredResult = {}
        for key in result:
                filteredResult[key] = {targetColor: result[key][targetColor]}
        return filteredResult
    return result 


def _mapProbabilities( result = {}):
    newResult = {}
    for key in result:
        value = result[key]
        newResult[key] = {
            "red": {
                'probabilidade': 0 if value[3] == 0 else int((value[0] / value[3]) * 100),
                'hit': value[0],
                'tried': value[3],
            },
            "black": {
                'probabilidade': 0 if value[3] == 0 else int((value[1] / value[3]) * 100),
                'hit': value[1],
                'tried': value[3],
            },
            "white": {
                'probabilidade': 0 if value[3] == 0 else int((value[2] / value[3]) * 100),
                'hit': value[2],
                'tried': value[3],
            }
        }
    return newResult    

def _filterByMinAndMaxProbabilidade(probabilidades = {}, minProbabilidade = 0, maxProbabilidade = 100):
    print('creu ', probabilidades)
    filteredResult = {}
    for padrao in probabilidades:
            padraoProbabilidades = {color: probabilidades[padrao][color] for color in probabilidades[padrao] 
                                    if probabilidades[padrao][color]['probabilidade'] >= minProbabilidade and
                                     probabilidades[padrao][color]['probabilidade'] <= maxProbabilidade }
            if not padraoProbabilidades:
                continue
            filteredResult[padrao] = padraoProbabilidades
    return filteredResult

def _probabilidade_padrao(rolls=[], pattern='', galho=0, targetColor='*', minProbabilidade=50, maxProbabilidade=100):
    pattern = _mapPattern(pattern)
    patternLength = len(pattern)
    total = hitRed = hitBlack = hitWhite = 0
    i = 0

    while i < len(rolls)-patternLength:
        rollsToBeChecked = rolls[i:i+patternLength]
        
        if not __is_pattern_found(rollsToBeChecked, pattern):
            i += 1
            continue

        entradas = rolls[i + patternLength : i + patternLength + galho + 1]
        if any(entrada["color"] == 'red' for entrada in entradas):
            hitRed += 1
        if any(entrada["color"] == 'black' for entrada in entradas):
            hitBlack += 1
        if any(entrada["color"] == 'white' for entrada in entradas):
            hitWhite += 1

        total += 1
        i += (patternLength + galho+1)
    
    probabilidadeBlack = int(0 if not total else (hitBlack / total) * 100)
    probabilidadeRed = int(0 if not total else (hitRed / total) * 100)
    probabilidadeWhite = int(0 if not total else (hitWhite / total) * 100)

    result = {}

    if total < 5:
        return result
    
    if (probabilidadeBlack >= minProbabilidade and probabilidadeBlack <= maxProbabilidade and (targetColor == 'black' or targetColor == '*')):
        result['black'] = {"hit": hitBlack, "tried": total, "probabilidade": probabilidadeBlack}
    if (probabilidadeWhite >= minProbabilidade and probabilidadeWhite <= maxProbabilidade and (targetColor == 'white' or targetColor == '*')):
        result['white'] = {"hit": hitWhite, "tried": total, "probabilidade": probabilidadeWhite}
    if (probabilidadeRed >= minProbabilidade and probabilidadeRed <= maxProbabilidade and (targetColor == 'red' or targetColor == '*')):
        result['red'] = {"hit": hitRed, "tried": total, "probabilidade": probabilidadeRed}       

    return result

def __is_pattern_found(rolls = [], pattern = [], ignoreNumber = True):
    rolls_colors = list(map(lambda r: r['color'], rolls))
    return all(pattern[i] == rolls_colors[i] or pattern[i] == '*' for i in range(len(pattern)))

def _mapPattern(pattern=''):
    splittedPattern = pattern.split(',')
    mappedPattern = []
    for p in splittedPattern:
        if p == 'r':
            mappedPattern.append('red')
        elif p == 'b':
            mappedPattern.append('black')
        elif p == 'w':
            mappedPattern.append('white')
        else:
            mappedPattern.append('*')

    return mappedPattern