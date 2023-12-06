from math import sqrt
def raices(a:float, b:float, c:float):
    raiz1=None
    raiz2=None
    descriminante = (b**2-4*a*c)
    if a!=0 and descriminante>=0:
        raiz1=(-b+sqrt(descriminante))/2*a
        raiz2=(-b-sqrt(descriminante))/2*a    
    return(raiz1,raiz2)