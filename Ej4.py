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
    [0.207909, 160.2977,  2.435504, 6.860992, 3.801762], # 01 Araba_Alava
    [0.309938, 148.9253, 14.0247,   5.217292, 2.479505], # 02 Albacete
    [0.3948,   213.9454, 26.4208,   8.326681, 5.665629], # 03 Alicante_Alacant
    [0.490768, 149.7108, 19.29913,  8.60834,  6.194291], # 04 Almeria
    [0.315643,  91.91513, 6.754752, 3.345812, 2.462012], # 05 Avila
    [0.225534, 116.631,  11.74279,  4.435497, 3.428113], # 06 Badajoz
    [0.41762,  261.714,  41.9875,   7.634091, 6.481461], # 07 Balears_Illes
    [0.370338, 360.4668, 50.0422,   5.007321, 5.539575], # 08 Barcelona
    [0.111988, 127.1908, 11.5068,   5.739403, 2.295761], # 09 Burgos
    [0.154865,  79.7039,  5.317035, 3.303789, 2.245544], # 10 Caceres
    [0.503783, 156.4845, 27.23626,  8.084514, 6.309279], # 11 Cadiz
    [0.380825, 192.6974, 21.60768,  6.772061, 2.831351], # 12 Castellon_Castello
    [0.285059, 100.7886,  8.449953, 5.273585, 2.484083], # 13 Ciudad_Real
    [0.310079, 138.1013, 20.42644,  4.031023, 1.963832], # 14 Cordoba
    [0.249238, 132.3185, 16.99266,  3.685156, 1.397511], # 15 Coruna_A
    [0.304354, 115.3501, 14.00027,  4.108776, 2.485556], # 16 Cuenca
    [0.333636, 259.7168, 37.54019,  6.524431, 6.833353], # 17 Girona
    [0.419273, 142.3809, 17.81374,  5.429051, 12.6642],  # 18 Granada
    [0.254918, 136.7454, 25.60106,  3.969439, 2.257846], # 19 Guadalajara
    [0.35713,  162.5214,  3.653711, 7.170064, 3.488882], # 20 Gipuzkoa
    [0.207225, 161.692,  29.46363,  5.369011, 3.3156],   # 21 Huelva
    [0.308265, 113.3096,  7.750675, 4.66802,  4.403793], # 22 Huesca
    [0.306332,  98.89688, 9.689766, 4.401508, 2.595761], # 23 Jaen
    [0.312875, 119.4512, 12.31387,  3.88859,  1.340893], # 24 Leon
    [0.358108, 176.7933, 19.15876,  4.610636, 3.021533], # 25 Lleida
    [0.465131, 138.919,  10.17086,  4.620298, 2.88381],  # 26 Rioja_La
    [0.370421,  87.85144, 8.149255, 2.901629, 1.91384],  # 27 Lugo
    [0.300295, 264.5616, 42.30665,  8.317889, 4.940295], # 28 Madrid
    [0.405344, 217.5383, 31.75953,  7.855675, 7.130623], # 29 Malaga
    [0.515312, 186.4979, 27.16983,  6.602437, 3.736013], # 30 Murcia
    [0.56569,  179.6364, 11.6413,   8.023866, 2.35208],  # 31 Navarra
    [0.098506,  96.89706, 12.80578, 3.94024,  1.116401], # 32 Ourense
    [0.208896, 106.2984,  8.405593, 5.083146, 1.890015], # 33 Asturias
    [0.253563,  70.61717, 4.183782, 5.578376, 3.486485], # 34 Palencia
    [0.333258, 158.4378, 18.75014,  5.191807, 3.543058], # 35 Palmas_Las
    [0.285943, 107.7898, 13.42872,  3.81257,  2.488761], # 36 Pontevedra
    [0.152826, 131.583,  17.39157,  3.362166, 2.047865], # 37 Salamanca
    [0.367304, 168.4891, 21.49201,  4.774955, 3.390501], # 38 Santa_Cruz_de_Tenerife
    [0.169947, 133.9692, 10.65567,  4.775509, 1.937395], # 39 Cantabria
    [0.064409,  98.28801, 8.566386, 5.732394, 2.898401], # 40 Segovia
    [0.505822, 222.434,  47.74654,  5.334124, 3.157556], # 41 Sevilla
    [0.447017,  98.56731, 4.470173, 7.599294, 3.240875], # 42 Soria
    [0.613522, 231.6162, 38.92322,  6.2532,   5.4745],   # 43 Tarragona
    [0.073944,  66.77167, 3.253547, 2.809882, 1.922551], # 44 Teruel
    [0.288265, 137.2691, 20.24719,  5.902572, 3.651358], # 45 Toledo
    [0.376465, 255.3937, 41.87041,  7.480355, 4.856396], # 46 Valencia_Valencia
    [0.345442, 115.3969,  9.039075, 3.454424, 1.132283], # 47 Valladolid
    [0.147275, 219.6211,  3.751172, 5.648416, 1.862591], # 48 Bizkaia
    [0.180325,  91.84569, 6.070952, 3.666615, 3.366072], # 49 Zamora
    [0.399012, 141.1993, 11.6839,   8.420187, 4.358444]  # 50 Zaragoza
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