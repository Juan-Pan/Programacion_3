def main():
    suma = 0
    contador = 0

    estatura = float(input("Ingrese una estatura en metros (0 para finalizar): "))

    if estatura == 0:
        print("Error: No se ingresaron datos válidos.")
        return

    while estatura != 0:
        suma += estatura
        contador += 1

        estatura = float(input("Ingrese otra estatura (0 para finalizar): "))

    if contador > 0:
        promedio = suma / contador
        print(f"La estatura promedio es: {promedio:.2f} cm")

if __name__ == "__main__":
    main()
