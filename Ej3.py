import numpy as np

Araba_Alava = 326574 # 01
Albacete = 390032 # 02
Alicante_Alacant = 1825332 # 03
Almeria = 706672 # 04
Avila = 160700 # 05
Badajoz = 679884 # 06
Balears_Illes = 1115999 # 07
Barcelona = 5576037 # 08
Burgos = 358171 # 09
Caceres = 400036 # 10
Cadiz = 1239435 # 11
Castellon_Castello = 575470 # 12
Ciudad_Real = 502578 # 13
Cordoba = 788219 # 14
Coruna_A = 1120294 # 15
Cuenca = 198718 # 16
Girona = 755716 # 17
Granada = 912938 # 18
Guadalajara = 253310 # 19
Gipuzkoa = 719282 # 20
Huelva = 518930 # 21
Huesca = 219702 # 22
Jaen = 643484 # 23
Leon = 468316 # 24
Lleida = 432384 # 25
Rioja_La = 315381 # 26
Lugo = 333634 # 27
Madrid = 6507184 # 28
Malaga = 1630615 # 29
Murcia = 1470273 # 30
Navarra = 643234 # 31
Ourense = 311680 # 32
Asturias = 1034960 # 33
Palencia = 163390 # 34
Palmas_Las = 1100480 # 35
Pontevedra = 942731 # 36
Salamanca = 333603 # 37
Santa_Cruz_de_Tenerife = 1007641 # 38
Cantabria = 580295 # 39
Segovia = 154184 # 40
Sevilla = 1939527 # 41
Soria = 88903 # 42
Tarragona = 791693 # 43
Teruel = 135562 # 44
Toledo = 686841 # 45
Valencia_Valencia = 2540707 # 46
Valladolid = 521130 # 47
Bizkaia = 1148302 # 48
Zamora = 177404 # 49
Zaragoza = 953486 # 50

provincias = [
    "Araba_Alava", "Albacete", "Alicante_Alacant", "Almeria", "Avila",
    "Badajoz", "Balears_Illes", "Barcelona", "Burgos", "Caceres",
    "Cadiz", "Castellon_Castello", "Ciudad_Real", "Cordoba", "Coruna_A",
    "Cuenca", "Girona", "Granada", "Guadalajara", "Gipuzkoa",
    "Huelva", "Huesca", "Jaen", "Leon", "Lleida",
    "Rioja_La", "Lugo", "Madrid", "Malaga", "Murcia",
    "Navarra", "Ourense", "Asturias", "Palencia", "Palmas_Las",
    "Pontevedra", "Salamanca", "Santa_Cruz_de_Tenerife", "Cantabria", "Segovia",
    "Sevilla", "Soria", "Tarragona", "Teruel", "Toledo",
    "Valencia_Valencia", "Valladolid", "Bizkaia", "Zamora", "Zaragoza"
]

def interpolacionLineal(x0, y0, x1, y1, x):
    return y0 + (((y1 - y0) / (x1 - x0)) * (x - x0))

def obtenervalor(matriz_x, matriz_y, valor, columna):
    col_x = matriz_x[:, columna]
    col_y = matriz_y[:, columna]

    indices_orden = np.argsort(col_x)
    col_x = col_x[indices_orden]
    col_y = col_y[indices_orden]

    if valor <= col_x[0]:
        return col_y[0]
    if valor >= col_x[-1]:
        return col_y[-1]

    idx = np.searchsorted(col_x, valor)

    if col_x[idx] == valor:
        return col_y[idx]

    return interpolacionLineal(col_x[idx], col_y[idx], col_x[idx-1], col_y[idx-1], valor)

divisores = np.array([
    Araba_Alava, Albacete, Alicante_Alacant, Almeria, Avila,
    Badajoz, Balears_Illes, Barcelona, Burgos, Caceres,
    Cadiz, Castellon_Castello, Ciudad_Real, Cordoba, Coruna_A,
    Cuenca, Girona, Granada, Guadalajara, Gipuzkoa,
    Huelva, Huesca, Jaen, Leon, Lleida,
    Rioja_La, Lugo, Madrid, Malaga, Murcia,
    Navarra, Ourense, Asturias, Palencia, Palmas_Las,
    Pontevedra, Salamanca, Santa_Cruz_de_Tenerife, Cantabria, Segovia,
    Sevilla, Soria, Tarragona, Teruel, Toledo,
    Valencia_Valencia, Valladolid, Bizkaia, Zamora, Zaragoza
])

valores = np.array([
    [0.2143, 209.5697,  2.0210, 4.1644, 1.4392],
    [0.3333, 183.2670, 12.3067, 4.5125, 2.0511],
    [0.2027, 322.0017, 35.1936, 5.7359, 3.4295],
    [0.3255, 244.5831, 29.7309, 5.4764, 3.7783],
    [0.1245, 129.5582,  7.6540, 3.1736, 2.1157],
    [0.2942, 149.4225, 11.9285, 2.7358, 1.8680],
    [0.3226, 399.8749, 41.3262, 5.6810, 4.3280],
    [0.3694, 406.4643, 46.5940, 3.0577, 2.5753],
    [0.0279, 158.1368, 12.7593, 4.1042, 2.0661],
    [0.3000,  93.6916,  6.7494, 2.3748, 1.8498],
    [0.4922, 214.3799, 31.8290, 5.8252, 6.5998],
    [0.2433, 254.7309, 21.7388, 4.0836, 2.5197],
    [0.3184, 132.7754, 11.8191, 2.9647, 1.9102],
    [0.2537, 184.0605, 21.4534, 2.7784, 1.8777],
    [0.2410, 151.9780, 16.9866, 2.5261, 0.9997],
    [0.0503, 159.0696, 14.4426, 1.8619, 1.7110],
    [0.3176, 324.4870, 45.6521, 4.8563, 5.7826],
    [0.3505, 209.6418, 25.1824, 4.0309, 6.8132],
    [0.1184, 188.6226, 24.1206, 3.3950, 1.4607],
    [0.2502, 174.8271,  3.8650, 5.1996, 1.7796],
    [0.1542, 216.2527, 27.1520, 3.0062, 2.6786],
    [0.3641, 111.5602,  7.0095, 3.1861, 1.9572],
    [0.2642, 117.2990, 11.1580, 2.7196, 2.0047],
    [0.2135, 167.8140, 10.6979, 2.8400, 0.8541],
    [0.4394, 207.9633, 26.1110, 2.6828, 2.0584],
    [0.1902, 150.2310,  9.8611, 3.9952, 2.5366],
    [0.0899,  99.1805,  9.7712, 2.6076, 1.4986],
    [0.2520, 391.2168, 53.9819, 5.8766, 2.4711],
    [0.3557, 282.9423, 39.1079, 5.0901, 5.7279],
    [0.4013, 248.1648, 30.7154, 3.7408, 1.9928],
    [0.5752, 197.7507, 12.9502, 4.5707, 2.0832],
    [0.1925, 112.6155,  7.2831, 2.7272, 1.2834],
    [0.2029, 119.0674,  8.4931, 3.9518, 1.2561],
    [0.0000, 103.5559,  3.9170, 3.7946, 1.5301],
    [0.3362, 215.1425, 25.2981, 4.2254, 3.1168],
    [0.1803, 147.1682, 14.4262, 2.9383, 1.7927],
    [0.2398, 168.8234, 12.6498, 2.3681, 1.8285],
    [0.3870, 268.4984, 36.5904, 4.1781, 2.5207],
    [0.1723, 165.4848, 11.9422, 2.8434, 1.0857],
    [0.1297, 126.2777,  6.3560, 3.1132, 1.7512],
    [0.4434, 272.4840, 49.8163, 3.6916, 2.1397],
    [0.0000, 127.6672,  7.4238, 1.9122, 1.2373],
    [0.3158, 289.8851, 40.8618, 4.4335, 3.8778],
    [0.7377,  76.4226,  2.8769, 2.7294, 0.9590],
    [0.3640, 235.3965, 24.9839, 2.9264, 2.6061],
    [0.3778, 272.8414, 29.6374, 4.9199, 3.2314],
    [0.3070, 169.1517,  9.1340, 2.2259, 0.5565],
    [0.1829, 270.9479,  5.0771, 3.3702, 1.3672],
    [0.2255, 135.1153,  7.3843, 2.5930, 1.8602],
    [0.1363, 175.4824, 15.7842, 3.8385, 2.2444]
])

valores = valores.T
# divisores = divisores /10000

# valores = valoresaNormalizar / divisores

criterios = np.array([
    [1,5,3,7,3],
    [1/5,1,3,1/2,1/4],
    [1/3,1/3,1,1/5,1/5],
    [1/7,2,5,1,1/5],
    [1/3,4,5,5,1]
    ])

puntosReferencia = np.array([
    [0.00, 0.00,   0.00,  0.00, 0.00],
    [0.15, 81.29,  10.80, 1.18, 1.36],
    [0.30, 162.59, 21.59, 2.35, 2.73],
    [0.44, 243.88, 32.39, 3.53, 4.09],
    [0.59, 325.17, 43.19, 4.70, 5.45],
    [0.74, 406.46, 53.98, 5.88, 6.81]
])

perfilesCentrales = np.array([
    [0.17,   0.25,   0.36],
    [129.18, 179.38, 268.99],
    [7.42,   13.69,  30.94],
    [2.73,   3.38,   4.52],
    [1.46,   2.00,   2.77]
])

perfilesCentrales = perfilesCentrales.T


x = np.vstack((puntosReferencia,perfilesCentrales))

rp = np.array([
    [0.336, 0.320, 0.459, 0.308, 0.385],
    [0.132, 0.139, 0.124, 0.149, 0.112],
    [0.086, 0.074, 0.069, 0.071, 0.062],
    [0.032, 0.047, 0.048, 0.060, 0.033],
    [0.026, 0.031, 0.034, 0.032, 0.023],
    [0.023, 0.022, 0.026, 0.023, 0.018]
])

prioridadescp = np.array([
    [0.125, 0.101, 0.229, 0.067, 0.109], # CP1 - Alta
    [0.099, 0.068, 0.109, 0.061, 0.089], # CP2 - Media
    [0.061, 0.042, 0.051, 0.036, 0.061]  # CP3 - Baja
])

y = np.vstack((rp,prioridadescp))

prioridades = ["Alto", "Medio", "Bajo"]


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
        print(f"Valor de {prov}: {aux:.4f} -> Alto")
        provinciasaltas.append(prov)
    elif res == 1:
        print(f"Valor de {prov}: {aux:.4f} -> Medio")
        provinciasmedias.append(prov)
    elif res == 2:
        print(f"Valor de {prov}: {aux:.4f} -> Bajo")
        provinciasbajas.append(prov)


print("Bajas:",provinciasbajas)
print("Medias:",provinciasmedias)
print("Altas:",provinciasaltas)