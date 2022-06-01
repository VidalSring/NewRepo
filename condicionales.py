    # Declaramos una variable
calificacion = input("Introduce tu calificacion de AZ-900")

calificacion=int(calificacion)

    # Preguntamos si la calificacion es menor a 700
if calificacion < 700:
    print("Vees, por no estudiar, BURRO!")
elif calificacion > 1000:
    print("MIENTES!!!, no puedes sacar mas de 1000")

else:   # Si no se ejecuta ninguno de los if este se cumple
    print("Felicidades, pasa por tu certificado")

#verificador de mayoria de edad
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <=115:
    print("Bienvenid@ al mamitas")
elif edad > 100:
    print("Si vienes acompañado de tu abuelos te podemos fiar")
elif edad < 0:
    print("Ni que fueras vieajero del tiempo")
else:
    print("No puedes levarte esos cigarros")

#En python no hay switch case