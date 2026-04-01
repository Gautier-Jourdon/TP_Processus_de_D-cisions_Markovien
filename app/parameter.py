import numpy as np

# =================== [Grille] ===================
n = 3
m = 4
Grille = np.zeros((n,m))

# =================== [ Position initiale ] ===================
X0 = 1
Y0 = 1

# =================== [ Paramètre d'escompte ] ===================
gamma = 0.9 # 0 < gamma < 1

# =================== [ Déplacement ] ===================
# Par défaut
haut = 0.8
gauche = 0.1
droite = 0.1

# =================== [ Récompenses ] ===================
R = [
    [0,0,0,+1],
    [0,0,0,-1],
    [0,0,0,0]
    ]