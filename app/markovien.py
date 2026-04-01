import app.parameter as p
import random
import numpy as np

# algorithme d eprogrammation dynamique par itération de valeur

def value_iteration():
    V = np.zeros((p.n, p.m))
    
    while True:
        delta = 0
        for i in range(p.n):
            for j in range(p.m):
                v = V[i][j]

                max_value = float('-inf')
                for action in ['haut', 'gauche', 'droite']:
                    if action == 'haut':
                        next_i, next_j = max(i-1, 0), j
                        prob = p.haut
                    elif action == 'gauche':
                        next_i, next_j = i, max(j-1, 0)
                        prob = p.gauche
                    else:
                        next_i, next_j = i, min(j+1, p.m-1)
                        prob = p.droite
                    
                    reward = p.R[next_i][next_j]
                    value = prob * (reward + p.gamma * V[next_i][next_j])
                    max_value = max(max_value, value)
                
                V[i][j] = max_value
                delta = max(delta, abs(v - V[i][j]))
        
        if delta < 1e-6: # critère de convergence
            break
    
    return V