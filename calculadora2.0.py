print("=== Calculadora 2.0 ===")

num1= float(input("Digite o primeiro número: "))
num2= float(input("Digite o segundo número: "))

print("Que operacion resolveremos?")

print("1. Suma")
print("2. Resta")
print("3. Multiplicación") 
print("4. División")

opcion= input("Ingrese el número de la operación que desea realizar: ")

if opcion == "1":
    resultado= num1 + num2
    print("El resultado de la suma es: ", resultado)

elif opcion == "2":
    resultado= num1 - num2
    print("El resultado de la resta es: ", resultado)

elif opcion == "3":
    resultado= num1 * num2
    print("El resultado de la multiplicación es: ", resultado)

elif opcion == "4":
    if num2 != 0:
        resultado= num1 / num2
        print("El resultado de la división es: ", resultado)
    else:
        print("Error: No se puede dividir entre cero.")