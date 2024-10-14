#coding: utf-8

def script0():
    vA = [] #vazio
    vB = [ None ] * 5 #vazio de tamanho 5 
    vC = [1, 3.4 , "A", "batman", 3.4, "batman", "batman"] #tamanho 4 com tipos diff

    print(vA)
    print(vB)
    print(vC)
    print("batman aparece", vC.count("batman"),"vez(es)")

def script1in():
    bebidas = ["coco-cola", "pespi", "guarana", "leite"]
    print("coco-cola" in bebidas)
    print("vodka" not in bebidas)#vodka not in = true se vodka in bebidas = false
    

if __name__=="__main__":
    #script0()
    script1in()