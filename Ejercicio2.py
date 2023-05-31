número_desde = int(input("Ingrese desde qué número quiere ver números en la pantalla: "))
número_hasta = int(input("Ingrese hasta qué número quiere ver números en la pantalla: "))
print("\n")
for número in range(número_desde, número_hasta + 1):
    print(número, end = "")
    if número != número_hasta:
        print(",", end = " ")