# Autor: Sofía Daniela Méndez Sandoval, A01242259
# Descripción: Este programa calcula el precio de los boletos requeridos dependiendo de la zona.

def main():

    cboletosA = int(input("Ingresa el número de boletos A requeridos: "))
    cboletosB = int(input("Ingresa el número de boletos B requeridos: "))
    cboletosC = int(input("Ingresa el número de boletos C requeridos: "))

    calcularPrecio(cboletosA, cboletosB, cboletosC)

    print("El costo total de los boletos es: ", calcularPrecio(cboletosA, cboletosB, cboletosC), "pesos")

def calcularPrecio (cboletosA, cboletosB, cboletosC):

    boletosA = cboletosA*3250
    boletosB = cboletosB*1730
    boletosC = cboletosC*850

    p = boletosA + boletosB + boletosC

    return p

main()