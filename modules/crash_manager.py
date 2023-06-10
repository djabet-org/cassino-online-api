from __future__ import division
from .sqlite_helper import fetch_all_crash_points, deletar_velas_antigas


# Padroes:
# 1. 3 velas verdes, proxima 2x?
# 2. 2 velas verdes, proxima 2x?
# 3. 1 velas verde >= 10, proxima 2x?
# 4. 2 velas pretas < 1.5, proxima 2x?
# 5. 1 vela preta < 1.5, 2 velas verdes, 1 vela preta < 1.5, proxima 2x?

def calcular_probabilidades(velas):
    
    return {
        "Padrao (v,v,v) => G2: " : "%{0}".format(calculate_padrao1_g2(velas)*100),
        "Padrao (v,v) => G2: " : "%{0}".format(calculate_padrao2_g2(velas)*100),
        "Padrao (30v) => G2: " : "%{0}".format(_calculate_padrao_1vXx_g2(velas)*100, 30),
        "Padrao (20v) => G2: " : "%{0}".format(_calculate_padrao_1vXx_g2(velas)*100, 20),
        "Padrao (10v) => G2: " : "%{0}".format(_calculate_padrao_1vXx_g2(velas)*100, 10),
        "Padrao (9v) => G2: " : "%{0}".format(_calculate_padrao_1vXx_g2(velas)*100, 9),
        "Padrao (8v) => G2: " : "%{0}".format(_calculate_padrao_1vXx_g2(velas)*100, 8),
        "Padrao (7v) => G2: " : "%{0}".format(_calculate_padrao_1vXx_g2(velas)*100, 7),
        "Padrao (6v) => G2: " : "%{0}".format(_calculate_padrao_1vXx_g2(velas)*100, 6),
        "Padrao (5v) => G2: " : "%{0}".format(_calculate_padrao_1vXx_g2(velas)*100, 5),
        "Padrao (4v) => G2: " : "%{0}".format(_calculate_padrao_1vXx_g2(velas)*100, 4),
        "Padrao (3v) => G2: " : "%{0}".format(_calculate_padrao_1vXx_g2(velas)*100, 3),
        "Padrao (1.5p, 1.5p) => G2: " : "%{0}".format(calculate_padrao_2p_15x_g2(velas)*100),
        "Padrao (1.4p, 1.4p) => G2: " : "%{0}".format(calculate_padrao_2p_14x_g2(velas)*100),
        "Padrao (1.3p, 1.3p) => G2: " : "%{0}".format(calculate_padrao_2p_13x_g2(velas)*100),
        "Padrao (1.2p, 1.2p) => G2: " : "%{0}".format(calculate_padrao_2p_12x_g2(velas)*100),
        "Padrao (1.1p, 1.1p) => G2: " : "%{0}".format(calculate_padrao_2p_11x_g2(velas)*100),
    }

def media_velas(velas):
    velas3x = fetch_all_crash_points(200, 3)
    velas5x = fetch_all_crash_points(200, 5)
    velas10x = fetch_all_crash_points(200, 10)

    return {
        "3x" : calculate_media(velas3x, 3),
        "5x" : calculate_media(velas5x, 5),
        "10x" : calculate_media(velas10x, 10),
    }    

# def calculate_media(velas = [], forVela):
#     for i in range(len(velas)):




def fetch_contagem_cores(qtd_velas):
    velas = fetch_all_crash_points(qtd_velas)
    print(qtd_velas)
    print(velas)
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

def calculate_padrao1(velas = []):
    qtdSucesso = 0
    qtdPadraoEncontrado = 0

    for i in range(len(velas)-3):
        if all(x >= 2 for x in velas[i:i+3]):
            qtdPadraoEncontrado += 1
            if velas[i+3] >= 2:
                qtdSucesso += 1
        
        
    return float(qtdSucesso/qtdPadraoEncontrado)

def calculate_padrao1_g1(velas = []):
    qtdSucesso = 0
    qtdPadraoEncontrado = 0

    for i in range(len(velas)-4):
        if all(x >= 2 for x in velas[i:i+3]):
            qtdPadraoEncontrado += 1
            if velas[i+3] >= 2:
                qtdSucesso += 1
        
        
    return float(qtdSucesso/qtdPadraoEncontrado)

#Padrao (v,v,v)"
def calculate_padrao1_g2(velas = []):
    qtdSucesso = 0
    qtdPadraoEncontrado = 0

    for i in range(len(velas)-5):
        if all(x >= 2 for x in velas[i:i+3]):
            qtdPadraoEncontrado += 1
            if velas[i+3] >= 2 or velas[i+4] >= 2 or velas[i+5] >= 2:
                qtdSucesso += 1
        
        
    return float(qtdSucesso/qtdPadraoEncontrado)    

def calculate_padrao2(velas = []):
    qtdSucesso = 0
    qtdPadraoEncontrado = 0

    for i in range(len(velas)-2):
        if velas[i] >= 2 and velas[i+1] >= 2:
            qtdPadraoEncontrado += 1
            if velas[i+2] >= 2:
                qtdSucesso += 1
        
        
    return float(qtdSucesso/qtdPadraoEncontrado)

def calculate_padrao2_g1(velas = []):
    qtdSucesso = 0
    qtdPadraoEncontrado = 0

    for i in range(len(velas)-3):
        if velas[i] >= 2 and velas[i+1] >= 2:
            qtdPadraoEncontrado += 1
            if velas[i+2] >= 2 or velas[i+3] >= 2:
                qtdSucesso += 1
        
        
    return float(qtdSucesso/qtdPadraoEncontrado) 

def calculate_padrao2_g2(velas = []):
    qtdSucesso = 0
    qtdPadraoEncontrado = 0

    for i in range(len(velas)-4):
        if velas[i] >= 2 and velas[i+1] >= 2:
            qtdPadraoEncontrado += 1
            if velas[i+2] >= 2 or velas[i+3] >= 2 or velas[i+4] >= 2:
                qtdSucesso += 1
        
        
    return float(qtdSucesso/qtdPadraoEncontrado)        

def calculate_padrao_1v10x_g2(velas = []):
    return _calculate_padrao_1vXx_g2(velas, 10)

def _calculate_padrao_1vXx_g2(velas = [], vela = 10):
    qtdSucesso = 0
    qtdPadraoEncontrado = 0

    for i in range(len(velas)-1):
        if velas[i] >= vela:
            qtdPadraoEncontrado += 1
            if any(v >= 2 for v in velas[i+1:i+4]):
                qtdSucesso += 1
    return float(qtdSucesso/qtdPadraoEncontrado) if qtdPadraoEncontrado > 0 else 0             

# Padrao (1.1p, 1.1p)
def calculate_padrao_2p_11x_g2(velas = []):
    return _calculate_padrao_2p_g2(velas, 1.1)

# Padrao (1.2p, 1.2p)
def calculate_padrao_2p_12x_g2(velas = []):
    return _calculate_padrao_2p_g2(velas, 1.2)     

# Padrao (1.3p, 1.3p)
def calculate_padrao_2p_13x_g2(velas = []):
    return _calculate_padrao_2p_g2(velas, 1.3)

# Padrao (1.4p, 1.4p)
def calculate_padrao_2p_14x_g2(velas = []):
    return _calculate_padrao_2p_g2(velas, 1.4)

# Padrao (1.5p, 1.5p)
def calculate_padrao_2p_15x_g2(velas = []):
    return _calculate_padrao_2p_g2(velas, 1.5)     

def _calculate_padrao_2p_g2(velas = [], vela = 1.99):
    qtdSucesso = 0
    qtdPadraoEncontrado = 0
    for i in range(len(velas)-2):
        # print(velas[i:i+2])
        if all( v < vela for v in velas[i:i+2]):
            print(velas[i:i+2])
            qtdPadraoEncontrado += 1
            if any( v >= 2 for v in velas[i+2:i+5]):
                qtdSucesso += 1

    return float(qtdSucesso/qtdPadraoEncontrado) if qtdPadraoEncontrado > 0 else 0 