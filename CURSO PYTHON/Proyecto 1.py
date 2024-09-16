
""" Programa que calcula el IMC de una persona, dado su peso y estatura, posteriormente, indicar su nivel de peso:"
  IMC            CLASIFICACIÓN
---------------------------------
  < 18.5    ---->  Bajo Peso
18.5 - 24.9 ---->  Peso normal
25 - 29.9   ---->  Sobrepeso
30 - 34.9   ---->  Obesidad I
35  - 39.9  ----> Obesidad II
>40 - 49.9  ----> Obesidad III
   > 50     ----> besidad  IV

IMC = peso / (estatura * estatura) 
"""

Nombre = input ("Ingrese su nombre: ")
Apellido1 = input ("Ingrese su Apellido paterno: ")
Apellido2 = input ("Ingrese su Apellido materno: ")
Sexo = input ("Ingrese su sexo: ")
Edad = int(input ("Ingrese su edad:  "))
peso = float(input("Ingrese su peso (Kg): " ))
estatura = float(input("Ingrese su estatura (m): "))

imc = peso / (estatura ** 2)

def Clasificar_imc(IMC):
    if IMC < 18.5:
        return "Bajo peso"
    elif 18.5 <= IMC <= 24.9:
        return "Normal"
    elif 25 <= IMC <= 29.9:
        return "Sobrepeso"
    elif 30 <= IMC <= 34.9:
        return "Obesidad I"
    elif 35 <= IMC <= 39.9:
        return "Obesidad II"
    elif 40 <= IMC <= 49.9:
        return "Obesidad III"
    else:
        return "Obesidad IV"

print ("¡Hola " + Nombre, Apellido1, Apellido2 + "!")
print("Su IMC es de:", round(imc, 2))
print("Clasificacion", Clasificar_imc(imc))

