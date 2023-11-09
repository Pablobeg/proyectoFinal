import cv2

def detector():
    url_camara = 'http://192.168.10.166:8080/video'

    # Inicializa la captura de video con la URL de la cámara IP
    captura_video = cv2.VideoCapture(url_camara)

    # Inicializa el detector de códigos QR
    detector_qr = cv2.QRCodeDetector()

    # Variable de estado para controlar la ejecución del bucle
    ejecucion = True

    while ejecucion:
        ret, fotograma = captura_video.read()

        # Intenta detectar códigos QR en cada frame
        data_qr, bbox_qr, rectified_qr = detector_qr.detectAndDecode(fotograma)

        # Si se detecta un código QR con contenido, retorna la información
        if data_qr:
            captura_video.release()
            return str(data_qr)

    captura_video.release()
    return "No se detectó ningún código QR"




