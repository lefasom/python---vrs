import os

def renombrar_videos(ruta_directorio):
    # Obtener la lista de archivos en el directorio
    archivos = [archivo for archivo in os.listdir(ruta_directorio) if archivo.endswith(('.mp4', '.avi', '.mkv'))]

    # Ordenar la lista de archivos
    archivos.sort()

    # Renombrar los archivos de video en formato numérico
    for i, archivo in enumerate(archivos, start=1):
        # Obtener la extensión del archivo
        _, extension = os.path.splitext(archivo)

        # Crear el nuevo nombre del archivo
        nuevo_nombre = f"{i}{extension}"

        # Ruta completa del archivo original y nuevo nombre
        ruta_original = os.path.join(ruta_directorio, archivo)
        ruta_nueva = os.path.join(ruta_directorio, nuevo_nombre)

        # Imprimir antes y después del renombrado
        print(f"Antes: {archivo}")
        print(f"Después: {nuevo_nombre}")

        # Renombrar el archivo
        os.rename(ruta_original, ruta_nueva)

# Especifica la ruta de tu directorio de videos
ruta_directorio_videos = "D:\Fullmetal Alchemist\Fullmetal Alchemist"

# Llama a la función para renombrar los videos
renombrar_videos(ruta_directorio_videos)
