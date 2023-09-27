def cacular_perimetro_ciruclo(diametro: float)-> float:
    PI = 3.14
    try:
        perimetro = diametro * PI
    except:
        perimetro = None
    return perimetro

def calcular_perimetro_rectangulo(base, altura):
    perimetro = base * 2 + altura * 2
    return perimetro

def calcular_perimetro_triangulo(a,b,c):
    perimetro = a + b + c
    return perimetro

def calcualr_perimetro_cuadrado(lado):
    perimetro = lado * 4
    return perimetro
     