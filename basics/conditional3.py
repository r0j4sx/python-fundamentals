

temperature = input("introduce the current temperature")

humidity = 0.2

# Idea general: Crear un programa que toma decisiones de riesgo
# dependiendo de los factores de temperatura y humedad
if temperature > 50:
    if humidity > 0 and humidity < 0.2:
        print("irrigate 1L per squere meter")





light = float(input("introduce el nivel de luz (0 a 100): "))
lamp_on = True

# Idea general: programa que decide que hacer con una lámpara
# dependiendo del nivel de luz que hay.
if light > 70:
    if lamp_on:
        print("Hay mucha luz: apagar la lampara")
elif light < 30:
    print("Hay poca luz: encender la lámpara")
else:
    print("la luz es correcta: no hacer nada")