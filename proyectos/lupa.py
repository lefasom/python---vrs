import cv2
import pyautogui
import numpy as np

def magnify_screen(x, y, width, height, scale_factor):
    # Captura la pantalla en la región especificada
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot = np.array(screenshot)

    # Escala la imagen
    screenshot = cv2.resize(screenshot, None, fx=scale_factor, fy=scale_factor)

    # Muestra la imagen ampliada
    cv2.imshow('Magnifier', screenshot)

    # Espera por una tecla y cierra la ventana al presionar 'q'
    key = cv2.waitKey(0)
    if key == ord('q'):
        cv2.destroyAllWindows()

# Especifica la región de la pantalla a capturar
x, y, width, height = 100, 100, 400, 400

# Factor de escala para ampliar la imagen
scale_factor = 2.0

# Llama a la función para mostrar la lupa
magnify_screen(x, y, width, height, scale_factor)
