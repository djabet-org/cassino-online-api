from __future__ import division

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
        "Padrao (10v) => G2: " : "%{0}".format(calculate_padrao3_g2(velas)*100),
        "Padrao (1.5p, 1.5p) => G2: " : "%{0}".format(calculate_padrao4_g2(velas)*100),
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

# Padrao (1.5p, 1.5p)
def calculate_padrao4_g2(velas = []):
    qtdSucesso = 0
    qtdPadraoEncontrado = 0
    for i in range(len(velas)-3):
        if all(vela < 1.5 for vela in velas[i:i+2]):
            print(velas[i:i+2])
            qtdPadraoEncontrado += 1
            if any( vela >= 2 for vela in velas[i+2:i+5]):
                qtdSucesso += 1

    return float(qtdSucesso/qtdPadraoEncontrado) if qtdPadraoEncontrado > 0 else 0

 # Padrao (1.5p, 1.5p)
def calculate_padrao5_g2(velas = []):
    qtdSucesso = 0
    qtdPadraoEncontrado = 0
    for i in range(len(velas)-4):
        if velas[i] < 1.5 and velas[i+1] >= 2 and velas[i+2] >= 2 and velas[i+3] < 1.5:
            # print(velas[i:i+2])
            qtdPadraoEncontrado += 1
            if any( vela >= 2 for vela in velas[i+4:i+7]):
                qtdSucesso += 1

    return float(qtdSucesso/qtdPadraoEncontrado) if qtdPadraoEncontrado > 0 else 0 

# Padrao (1.3p, 1.3p)
def calculate_padrao_2p_13x_g2(velas = []):
    return _calculate_padrao_2p_g2(velas, 1.3) 

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