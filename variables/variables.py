nombre = "juan David"

#concatenar con +
bienvenida = "hola " + nombre + ", como esta?"
print ( bienvenida)

#concatenar con f string
numero = 10
numero += 5
bienvenidaDos = f"hola {numero}, como esta?"

#del #borra una variable
print(bienvenidaDos)


#operadores de pertenecencia (in, not in)
print("ola "  in bienvenida) #false
print("Ash " not in bienvenida) #true