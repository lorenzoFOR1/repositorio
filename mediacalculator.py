#coding: utf-8

import math as mt

notaa = float(input())
notab = float(input())
notac = float(input())
peso1 = 2
peso2 = 3
peso3 = 5
media_ponderada = (notaa*2+notab*3+notac*5)/(2+3+5)
saida = "MEDIA = {0:.1f}".format(media_ponderada)
print(saida)