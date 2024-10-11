#coding: utf-8

import math as mt

def comissao():
    nome = input("Entre com o nome do vendedor:")
    salariofixo = float(input("Entre com o salário do vendedor:"))
    vendasvalor = float(input("Informe o total de vendas:"))
    comissaovalor = 0.15*vendasvalor
    totalareceber = salariofixo+comissaovalor
    return nome, comissaovalor, totalareceber
    print()


if __name__=="__main__":
    nome,comissaovalor,totalareceber = comissao()
    strg = "{0} obteve R$ {1:.2f} de comissão e vai receber {2:.2f}".format(nome, comissaovalor, totalareceber)
    print(strg)