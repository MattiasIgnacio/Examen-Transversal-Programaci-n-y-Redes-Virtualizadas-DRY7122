# vlan_rango.py

# Función para determinar el rango de VLAN
def determinar_rango_vlan(vlan):
    if 1 <= vlan <= 1005:
        return "normal"
    elif 1006 <= vlan <= 4094:
        return "extendido"
    else:
        return "inválido"

# Bucle para ingresar y procesar múltiples VLAN
while True:
    try:
        # Entrada de usuario para el número de VLAN
        vlan = int(input("Ingrese el número de VLAN (o '0' para salir): "))
        
        # Salir del bucle si el usuario ingresa '0'
        if vlan == 0:
            break
        
        # Llamar a la función y mostrar el resultado
        rango_vlan = determinar_rango_vlan(vlan)
        print(f"La VLAN {vlan} corresponde al rango {rango_vlan}.")
    
    except ValueError:
        print("Error: Ingrese un número entero válido.")
