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
    if (Delta>0):
        #duas reais distintas
        x1 = (-b-pow(Delta, 0.5))/(2*a)
        x2 = (-b+pow(Delta, 0.5))/(2*a)
        return x1,x2
    elif(Delta == 0):
        print("Há raiz unica, Delta = ", Delta)
        return Delta
    else:
        print("Raizes complexas, Delta = ", Delta)
        return Delta

if __name__=="__main__":
    x1,x2 = eq2grau(1,4,3)
    print(f"as raizes sao {x1} e {x2}")