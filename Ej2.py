import numpy as np

Almeria = 706672
Cadiz = 1239435
Cordoba = 788219
Granada = 912938
Huelva = 518930
Jaen = 643484
Malaga = 1630615
Sevilla = 1939527

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

divisores =np.array([Almeria,Cadiz,Cordoba,Granada,Huelva,Jaen,Malaga,Sevilla])

valoresaNormalizar = np.array([
    [23,     61,     20,     32,    8,     17,    58,    86],
    [17284,  26571,  14508, 19139, 11222, 7548,  46137, 52849],
    [2101,   3945,   1691,  2299,  1409,  718,   6377,  9662],
    [387,    722,    219,    368,   156,   175,   830,   716],
    [267,    818,    148,    622,   139,   129,   934,   415]
])
divisores = divisores /10000

valores = valoresaNormalizar / divisores

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

perfilesCentrales = np.array([
    [0.26, 0.34, 0.41],
    [194.29, 215.32, 261.32],
    [22.95, 28.44, 36.20],
    [2.87, 3.86, 5.32],
    [2.06, 3.23, 6.25]
    ]
)

perfilesCentrales = perfilesCentrales.T

x = np.array([
    [0.00, 0.00,   0.00,  0.00, 0.00],
    [0.10, 56.59,  9.96,  1.17, 1.36],
    [0.20, 113.18, 19.93, 2.33, 2.06],
    [0.26, 169.77, 22.95, 2.87, 2.73],
    [0.30, 194.29, 28.44, 3.50, 3.23],
    [0.34, 215.32, 29.89, 3.86, 4.09],
    [0.39, 226.35, 36.20, 4.66, 5.45],
    [0.41, 261.32, 39.85, 5.32, 6.25],
    [0.49, 282.94, 49.82, 5.83, 6.81]
])

y = np.array([
    [0.34, 0.32, 0.46, 0.31, 0.39],
    [0.13, 0.14, 0.12, 0.15, 0.11],
    [0.09, 0.07, 0.07, 0.07, 0.09],
    [0.05, 0.05, 0.06, 0.07, 0.06],
    [0.03, 0.04, 0.05, 0.06, 0.05],
    [0.03, 0.03, 0.05, 0.05, 0.03],
    [0.03, 0.03, 0.04, 0.03, 0.02],
    [0.03, 0.03, 0.03, 0.03, 0.02],
    [0.02, 0.02, 0.03, 0.02, 0.02]
])

prioridades = ["Alto", "Medio", "Bajo"]

prioridadescp = np.array([
    [0.05 , 0.05, 0.06, 0.07, 0.06],
    [0.03, 0.03, 0.05, 0.05, 0.03],
    [0.03, 0.03, 0.03, 0.03, 0.02]
])

valores_propios, vectores_propios = np.linalg.eig(criterios)
indice_max = np.argmax(valores_propios.real)
vector_principal = vectores_propios[:, indice_max].real
pesos = vector_principal / np.sum(vector_principal)
Valoresprioridades = prioridadescp * pesos

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
        print(f"Valor: {aux:.4f} -> Alto")
        provinciasaltas.append(prov)
    elif res == 1:
        print(f"Valor: {aux:.4f} -> Medio")
        provinciasmedias.append(prov)
    elif res == 2:
        print(f"Valor: {aux:.4f} -> Bajo")
        provinciasbajas.append(prov)


print("Bajas:",provinciasbajas)
print("Medias:",provinciasmedias)
print("Altas:",provinciasaltas)