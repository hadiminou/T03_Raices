a = float(input("primer coeficiente="))
if a == 0 :
     print("no es una ecuacion segundo grado, escribe cualquier numero excepto cero")
     a = float(input("primer coeficiente="))   
b = float(input("segundo coeficiente="))
c = float(input("tercer coeficiente="))
delta = (b**2-4*a*c)
if float(delta)<0 :
     print("no hay resueltos reales")     
raiz1 = (-b+(delta**0.5))/2*a
raiz2 = (-b-(delta**0.5))/2*a
print("raiz1=",(raiz1))
print("raiz2=",(raiz2))