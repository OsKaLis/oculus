import cv2

from configurations import (
    CURRENT_DIRECTORY, USER_NAME
)


class WorkFace():
    """."""
    count = 0

    def photo_name(self, ):
        """."""
        return f'{CURRENT_DIRECTORY}\\{str(USER_NAME)}.{str(self.count)}.jpg',

    def creating_face_host(self, ):
        """Метод создания обущающих экземпляров хозяена."""
        cam = cv2.VideoCapture(0)
        face_detector = cv2.CascadeClassifier(
            'haarcascade_frontalface_default.xml'
        )
        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                self.count += 1
                cv2.imwrite(self.photo_name(), gray[y:y+h, x:x + w])
            cv2.imshow('image', img)
            k = cv2.waitKey(100) & 0xff
            if k == 27:
                break
            elif self.count >= 50:
                break
        cam.release()
        cv2.destroyAllWindows()


wf = WorkFace()
wf.creating_face_host()
