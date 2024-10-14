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
    print("vodka" not in bebidas)#vodka not in = true , vodka in bebidas = false
    print("lista de bebidas:", bebidas)
    bebida_gelada = "dolly"
    if (bebida_gelada not in bebidas):
        prompt = input("deseja adicionar uma bebida?:")
        bebidas.append(bebida_gelada)
        print(f"{bebida_gelada} adicionada ao vetor")
    else:
        print(f"{bebida_gelada} já está no vetor")
    print(bebidas)

    #if (bebida_gelada in bebidas):
        #print(f"{bebida_gelada} já está no vetor")
    

if __name__=="__main__":
    #script0()
    script1in()