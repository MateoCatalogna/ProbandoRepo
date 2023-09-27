

def cacular_superficie_ractangulo(largo: float, ancho: float)-> float:
    """calcula a superficie de un rectangulo

    Args:
        largo (float): argo de rectangulo
        ancho (float): ancho del rectangulo

    Returns:
        superficie: retorna la superficie del rectangulo
    """    
    try:
       superficie = largo * ancho
    except:
        superficie = None
    return superficie

print(cacular_superficie_ractangulo(5,2))

def cacular_superficie_cuadrado(lado: float)-> float:
    """calcula la supericie de un cuadrado

    Args:
        lado (float): lado de un cuadrado

    Returns:
        superficie: retorna la superficie de un cuadrado
    """
    return cacular_superficie_ractangulo(lado, lado)

print(cacular_superficie_cuadrado(5))


