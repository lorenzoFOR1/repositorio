#coding: utf-8

import math as mt
'''
#true
print(5!=7)
#false
print(7!=7)
'''

def eq2grau(a,b,c):
    Delta = mt.pow(b,2)-4*a*c
    x1 = None
    x2 = None
    if (Delta>0):
        #duas reais distintas
        x1 = (-b-pow(Delta, 0.5))/(2*a)
        x2 = (-b+pow(Delta, 0.5))/(2*a)

    elif(Delta == 0):
        print("Há raiz unica, Delta = ", Delta)
        
    else:
        print("Raizes complexas, Delta = ", Delta)

    return x1,x2, Delta
        
if __name__=="__main__":
    saida = eq2grau(1,4,4)
    print(saida)
    print("qtd de termos:", len(saida))
    print("primeiro termo", saida[0])
    print("segundo termo", saida[1])
    print("terceiro termo", saida[2])