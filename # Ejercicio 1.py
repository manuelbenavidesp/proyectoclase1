ejer1
horas = int(input("Ingrese horas diarias: "))
tramo = input("Ingrese tramo (A, B, C o D): ").upper()

mensualidad = 160000
matricula = 35000

# --- Mensualidad ---
if horas >= 8:
    if tramo in ["A", "B"]:
        mensualidad *= 0.80
    else:
        mensualidad *= 0.86
elif horas >= 4:
    if tramo in ["A", "B"]:
        mensualidad *= 0.88
    else:
        mensualidad *= 0.92
#horas sin descuento

# --- Matrícula ---
if tramo in ["A", "B"]:
    matricula *= 0.90
    if horas >= 6:
        matricula *= 0.95

print("El valor de la mensualidad es:", int(mensualidad))
print("El valor de la matrícula es:", int(matricula))
