import cv2
import numpy as np


def definir_rangos_color(color):
    """Define el rango de tonos para cada color"""
    if color == "rojo":
        inferior = np.array([160, 50, 50])
        superior = np.array([180, 255, 255])
    elif color == "verde":
        inferior = np.array([36, 50, 50])
        superior = np.array([70, 255, 255])
    elif color == "azul":
        inferior = np.array([100, 50, 50])
        superior = np.array([140, 255, 255])
    else:
        raise ValueError("Color no válido.")
    return inferior, superior


def detectar_color(frame, color):

    # Convierte la imagen a espacio de color HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    inferior, superior = definir_rangos_color(color)

    # Crea una máscara para el color
    mascara = cv2.inRange(hsv, inferior, superior)

    # Encuentra los contornos en la máscara
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contornos:

        # Busca el contorno más grande
        mayor_contorno = max(contornos, key=cv2.contourArea)

        # Dibuja un rectángulo alrededor del contorno más grande
        x, y, w, h = cv2.boundingRect(mayor_contorno)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Muestra el resultado
    cv2.imshow("Detectando el color: " + color, frame)

# Capturar video de la cámara
camara = cv2.VideoCapture(0)

# Solicita color al usuario
color = input("Ingrese el color a detectar (rojo, verde o azul): ")


while color not in ["rojo", "verde", "azul"]:
    print("Color no válido. Inténtelo de nuevo.")
    color = input("Ingrese el color a detectar (rojo, verde o azul): ")

while True:
    # Lee el frame de la cámara
    ret, frame = camara.read()

    # Función principal
    detectar_color(frame, color)

    # Presionar 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara
camara.release()

# Cerrar todas las ventanas
cv2.destroyAllWindows()
