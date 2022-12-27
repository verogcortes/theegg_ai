palabra = input ("Introduce la palabra que quieras comprobar:")
palabra_inv = palabra [::-1]
if palabra == palabra_inv:
    print ("La palabra es palídroma")
else:
    print ("La palabra no es palídroma")
