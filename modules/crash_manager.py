from __future__ import division

# Padroes:
# 1. 3 velas verdes, proxima 2x?
# 2. 2 velas verdes, proxima 2x?
# 3. 1 velas verde >= 10, proxima 2x?

def calcular_probabilidades(velas):
    
    return {
        "Padrao (v,v,v,V) => G2: " : "%{0}".format(calculate_padrao1_g2(velas)*100),
        "Padrao (v,v,V) => G2: " : "%{0}".format(calculate_padrao2_g2(velas)*100),
        "Padrao (10v, V) => G2: " : "%{0}".format(calculate_padrao3_g2(velas)*100),
    }

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

def calculate_padrao3(velas = []):
    qtdSucesso = 0
    qtdPadraoEncontrado = 0

    for i in range(len(velas)-1):
        if velas[i] >= 10:
            qtdPadraoEncontrado += 1
            if velas[i+1] >= 2:
                qtdSucesso += 1
    return float(qtdSucesso/qtdPadraoEncontrado)
            

def calculate_padrao3_g1(velas = []):
    qtdSucesso = 0
    qtdPadraoEncontrado = 0

    for i in range(len(velas)-2):
        if velas[i] >= 10:
            qtdPadraoEncontrado += 1
            if velas[i+1] >= 2 or velas[i+2] >= 2:
                qtdSucesso += 1                
    return float(qtdSucesso/qtdPadraoEncontrado)

def calculate_padrao3_g2(velas = []):
    qtdSucesso = 0
    qtdPadraoEncontrado = 0

    for i in range(len(velas)-3):
        if velas[i] >= 10:
            qtdPadraoEncontrado += 1
            if velas[i+1] >= 2 or velas[i+2] >= 2 or velas[i+3] >= 2:
                qtdSucesso += 1                   
    return float(qtdSucesso/qtdPadraoEncontrado)