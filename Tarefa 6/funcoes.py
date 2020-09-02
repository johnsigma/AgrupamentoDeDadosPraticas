import pandas as pd
import numpy as np
import random

def distancia(obj1, obj2, dist=2):
  
  lista = []

  for (valor1, valor2) in zip(obj1, obj2):
    resultado = abs(valor1 - valor2) ** int(dist)
    lista.append(resultado)

  resultado = sum(lista)
  resultado = resultado ** (1/int(dist))

  return round(resultado, 2)

def distancia_todos(df, dist=1):
  if dist != 1 and dist != 2:
    return 'Somente as distâncias 1 (euclediana) e 2 (manhattan) estão disponíveis!'
    
  listas = []
  for i, (nome_col, dados_row) in enumerate(df.iterrows()):
    lista = (dados_row.values.tolist())
    listas.append(lista)

  resultado = []
  for i, l1 in enumerate(listas):
    r = []
    for j, l2 in enumerate(listas):
      result = distancia(l1, l2, dist)
      r.append(result)
    resultado.append(r)
  return resultado

def output_txt(listas):
  f = open("output.txt", "w")
  for lista in listas:
    f.write(str(lista[0]))
    for i in lista[1:]:
      f.write(','+ str(i))
    f.write("\n")
  f.close()

def centroides(k, data):
  centroides = []
  while True:
    n = random.randrange(0, data.shape[0])
    if n not in centroides:
      centroides.append(n)
    if len(centroides) == k:
      return centroides

def percorre(data, centros):
  lista_dist = []
  for i, (nome_col, dados_row) in enumerate(data.iteritems()):
    for centro in enumerate(centros):
      print(distancia(dados_row, centro, 1))
      break

def distancia_centroide(k,df):
    centros = centroides(k,df)
    for i in range(df.shape[0]):
        distancias = []
        inter =[]
        for m in centros:
            dist = distancia(df.iloc[i], df.iloc[m])
            inter.append(dist)
            valor_min = min(inter)
            distancias.append(valor_min)
            print(distancias)
            
def agrup_inicial(centroides, df=df):
  clusters = {n: 0 for n in range(0,df.shape[0])}
  for i in range(0, df.shape[0]):
    distancias = []
    for e, m in enumerate(centroides):
      dist = distancia(df.iloc[i], df.iloc[m])
      distancias.append(dist)
      if (e+1) == len(centroides):
        menor = min(distancias)
        for b, c in zip(distancias, centroides):
          if menor == b:
            clusters[i] = c
            break
  return clusters
