from __future__ import division
from datetime import datetime
from .cassino_database_manager import fetch_double_rolls

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

def fetch_rolls(platform, qtd_rolls):
    rolls = fetch_double_rolls(platform, qtd_rolls)
    return list(map(lambda rowRolls: {
        "roll": rowRolls["roll"],
        "platform": rowRolls["platform"],
        "created": rowRolls["created"],
        "color": rowRolls["color"]},
        rolls))

