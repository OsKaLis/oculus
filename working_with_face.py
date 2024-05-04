import os
import cv2
import numpy as np
from time import sleep

from configurations import (
    FACE_USER, HOST_MODEL, PICTURE_NAME
)


class WorkFace():
    """."""

    face_user = 'face_user'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_detector = cv2.CascadeClassifier(
            'haarcascade_frontalface_default.xml'
        )

    def creating_face_host(self, ) -> None:
        """Метод создания обущающих экземпляров хозяена."""
        cam = cv2.VideoCapture(0)
        if not os.path.isdir(self.face_user):
            os.mkdir(self.face_user)
        count: int = 0
        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.face_detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                count += 1
                cv2.imwrite(
                    f'{FACE_USER}\\{str(count)}.jpg',
                    gray[y:y+h, x:x + w]
                )
            k = cv2.waitKey(100) & 0xff
            if k == 27:
                break
            elif count >= 50:
                break
        cam.release()
        cv2.destroyAllWindows()

    def creating_host_model(self, ): 
        """Создаю мдель хозяина."""
        imgfiles = [os.path.join(FACE_USER, f) for f in os.listdir(FACE_USER)]
        faces = []
        ids = []
        for imagefile in imgfiles:
            img = cv2.imread(imagefile)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces.append(img)
            id = int(os.path.split(imagefile)[-1].split(".")[0])
            ids.append(id)
            os.remove(imagefile)
        self.recognizer.train(faces, np.array(ids))
        self.recognizer.write(HOST_MODEL)
        os.rmdir(self.face_user)

    def definitions_host(self, ):
        """Проверка на хозяина."""
        cam = cv2.VideoCapture(0)
        self.recognizer.read(HOST_MODEL)
        cam.set(3, 640)  # размер видеокадра - ширина
        cam.set(4, 480)  # размер видеокадра - высота
        host_recognized: bool = False
        probability_host: int = 0
        attempts: int = 0
        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.face_detector.detectMultiScale(
                gray, scaleFactor=1.2, minNeighbors=5, minSize=(10, 10),
            )
            for (x, y, w, h) in faces:
                cv2.rectangle(
                    img, (x, y), (x + w, y + h), (0, 255, 0), 2
                )
                id, confidence = self.recognizer.predict(
                    gray[y:y + h, x:x + w]
                )
                if (confidence < 100):
                    probability_host = round(100 - confidence)
                    if probability_host > 50:
                        host_recognized = True
                        break
                    if attempts > 30:
                        break
                attempts += 1
                sleep(1)
            k = cv2.waitKey(10) & 0xff
            if host_recognized or attempts > 30 or k == 27:
                break
        cam.release()
        cv2.imwrite(PICTURE_NAME, img)
        cv2.destroyAllWindows()
        return host_recognized, probability_host
