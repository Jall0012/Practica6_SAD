import numpy as np

provincias = ["Almeria","Cadiz","Cordoba","Granada","Huelva","Jaen","Malaga","Sevilla"]

def interpolacionLineal(x0, y0, x1, y1, x):
    return y0 + (((y1 - y0) / (x1 - x0)) * (x - x0))

def obtenervalor(matriz, matriz2, valor, columna):
    col = matriz[:, columna]
    col2 = matriz2[:, columna]

    if valor < col[0] or valor > col[-1]:
        return None

    idx = np.searchsorted(col, valor)

    if col[idx] == valor:
        return col2[idx]

    return interpolacionLineal(col[idx ], col2[idx], col[idx-1], col2[idx-1], valor)

valores = np.array([
    [23,     61,     20,     32,    8,     17,    58,    86],
    [17284,  26571,  14508, 19139, 11222, 7548,  46137, 52849],
    [2101,   3945,   1691,  2299,  1409,  718,   6377,  9662],
    [387,    722,    219,    368,   156,   175,   830,   716],
    [267,    818,    148,    622,   139,   129,   934,   415]
])

criterios = np.array([
    [1,5,3,7,3],
    [1/5,1,3,1/2,1/4],
    [1/3,1/3,1,1/5,1/5],
    [1/7,2,5,1,1/5],
    [1/3,4,5,5,1]
    ])

puntosReferencia = np.array([
    [0,0,0,0,0],
    [41.2 ,50914.4 ,7025.4 ,764.8 ,321.6],
    [82.4 ,101828.8 ,14050.8 ,1529.6 ,643.2],
    [123.6, 152743.2, 21076.2, 2294.4, 964.8],
    [164.8, 203657.6, 28101.6, 3059.2, 1286.4],
    [206, 254572, 35127, 3824, 1608]
    ])

perfilesCentrales = np.array(
    [[20,   5000,   5000,    300,    300],
     [100,  95000,  19000,   1800,    600],
    [160, 180000,  27000,   2500,    900]]
)

x = np.array([
    [0.0,       0.0,        0.0,        0.0,           0.0],
    [20.0,      5000.0,     5000.0,     300.0,         300.0],
    [41.2,      50914.4,    7025.4,     764.8,         321.6],
    [82.4,      95000.0,    14050.8,    1529.6,        600.0],
    [100.0,     101828.8,   19000.0,    1800.0,        643.2],
    [123.6,     152743.2,   21076.2,    2294.4,        900.0],
    [160.0,     180000.0,   27000.0,    2500.0,        964.8],
    [164.8,     203657.6,   28101.6,    3059.2,        1286.4],
    [206.0,     254572.0,   35127.0,    3824.0,        1608.0]
])

y = np.array([
    [0.336,     0.320,      0.459,      0.308,         0.385],
    [0.277,     0.261,      0.138,      0.259,         0.262],
    [0.132,     0.139,      0.124,      0.149,         0.112],
    [0.086,     0.075,      0.069,      0.071,         0.070],
    [0.058,     0.074,      0.063,      0.066,         0.062],
    [0.032,     0.047,      0.048,      0.060,         0.035],
    [0.029,     0.032,      0.040,      0.034,         0.033],
    [0.026,     0.031,      0.034,      0.032,         0.023],
    [0.023,     0.022,      0.026,      0.023,         0.018]
])

prioridades = ["Alto", "Medio", "Bajo"]

prioridadescp = np.array([
    [0.277, 0.261, 0.138, 0.259, 0.262],
    [0.058, 0.075, 0.063, 0.066, 0.070],
    [0.029, 0.032, 0.040, 0.034, 0.035]
])

valores_propios, vectores_propios = np.linalg.eig(criterios)
indice_max = np.argmax(valores_propios.real)
vector_principal = vectores_propios[:, indice_max].real
pesos = vector_principal / np.sum(vector_principal)
Valoresprioridades = prioridadescp * pesos

print(f"El valor global de la prioridad alta:{sum(Valoresprioridades[0])}")
print(f"El valor global de la prioridad media:{sum(Valoresprioridades[1])}")
print(f"El valor global de la prioridad baja:{sum(Valoresprioridades[2])} \n")
valoresFinales = []

provinciasbajas = []
provinciasmedias = []
provinciasaltas = []

for val,prov in zip(valores.T,provincias):
    valoresFinales2 = []

    for i in range(5):
        valcalc = obtenervalor(x, y, val[i], i)

        if valcalc is not None:
            valoresFinales2.append(valcalc * pesos[i])
        else:
            valoresFinales2.append(0)

    aux = sum(valoresFinales2)
    valoresFinales.append(aux)

    n = float('inf')
    res = -1

    for j in range(len(Valoresprioridades)):
        diferencia = abs(np.sum(Valoresprioridades[j]) - aux)
        if n > diferencia:
            n = diferencia
            res = j

    if res == 0:
        print(f"Valor de {prov}: {aux:.4f} -> Alto")
        provinciasaltas.append(prov)
    elif res == 1:
        print(f"Valor de {prov}: {aux:.4f} -> Medio")
        provinciasmedias.append(prov)
    elif res == 2:
        print(f"Valor de {prov}: {aux:.4f} -> Bajo")
        provinciasbajas.append(prov)

print("\nBajas:",provinciasbajas)
print("Medias:",provinciasmedias)
print("Altas:",provinciasaltas)