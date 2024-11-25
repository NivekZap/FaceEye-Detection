FaceEye-Detection

Proyecto en Python que implementa un sistema de detección en tiempo real de rostros y ojos utilizando la biblioteca OpenCV. Este programa emplea modelos Haar Cascade para identificar las características faciales y oculares en imágenes capturadas desde una cámara web.

## Requisitos

- Python 3.8 o superior.
- OpenCV instalado (`pip install opencv-python` y `pip install opencv-python-headless`).
- Archivos Haar Cascade para detección de rostro y ojos:
  - `haarcascade_frontalface_default.xml`
  - `haarcascade_eye.xml`

## Configuración

1. Asegúrate de tener instalados los requisitos mencionados anteriormente.
2. Descarga los archivos Haar Cascade desde el repositorio oficial de OpenCV o usa los que ya tengas.
3. Modifica las rutas de los archivos Haar Cascade en el código para que apunten a la ubicación correcta en tu sistema.

```python
face_cascade = cv2.CascadeClassifier('path/to/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('path/to/haarcascade_eye.xml')
```
## Para Clonar este repo :
git clone https://github.com/tu-usuario/FaceEye-Detection.git
cd FaceEye-Detection
Ejecuta el script principal:
python main.py

Asegúrate de que la cámara web esté funcionando correctamente.
La ventana mostrará las detecciones en tiempo real. Presiona la tecla Esc para salir del programa.

## Funcionamiento
El script captura imágenes desde la cámara web.
Convierte las imágenes a escala de grises para procesarlas.
Detecta rostros y ojos utilizando modelos Haar Cascade y dibuja rectángulos alrededor de estas características.

## Notas
Asegúrate de estar en un entorno bien iluminado para mejorar la detección.
Si experimentas problemas con la cámara, verifica que esté correctamente conectada y que ningún otro programa esté utilizándola.

## Contribuciones
Las contribuciones son bienvenidas. Si tienes mejoras o nuevas ideas, no dudes en abrir un pull request.




















