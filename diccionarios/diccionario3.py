d1 = {"leon": "lion", 
      "elefante": "elephant", 
      "sapo": "toad",
      "tortuga": "tortoise"}

def tuplaAnima1(d1):
    listaEspañol=[]
    listaIngles=[]
    for clave,valor in d1.items():
        listaEspañol.append(clave)
        listaIngles.append(valor)
        tuplaEspañol = tuple(listaEspañol)
        tuplaIngles = tuple(listaIngles)
    return (tuplaEspañol, tuplaIngles)
  
tupla1, tupla2= tuplaAnima1 (d1)
print ("La tupla en español son: ", tupla1)
print ("La tupla en ingles son: ", tupla2)