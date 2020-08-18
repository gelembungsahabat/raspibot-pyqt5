'''
This code made by Muhammad Wildan
release time: 19-08-2020, 04:07 WIB

nb: ini program logicnya.. kalo pengen ngirim data serial ke microcontroller, 
    hilangkan semua yang mempunyai satu hashtag (#)

'''

##import librarynya
import cv2
import sys
import imutils
# import serial

##import dependencynya
from UI_main import *
from PyQt5.Qt import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication

## ini port serialnya, jika error, bisa di googling hehe
# serialData = serial.Serial('/dev/ttyUSB0')


##ini class main windownya
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ##set timer agar dapat mengakses camera tiap satuan waktu
        self.timer = QTimer()
        self.timer.timeout.connect(self.viewCam)
        self.controlTimer()

        ##set/connect push buttonnya ke fungsi stop
        self.ui.pushButton_4.clicked.connect(self.stop)
        self.ui.pushButton_5.clicked.connect(self.stop)
        self.ui.pushButton_6.clicked.connect(self.stop)
        self.ui.pushButton_7.clicked.connect(self.stop)

    ##fungsi untuk mengakses camera dengan opencv 
    def viewCam(self):
        ##ngeread capture image dari webcam/camera
        ret, image = self.cap.read()
        
        ##format warnanya diconvert dari BGR ke RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        ##resize gambar pake library `imutils` trus hasilnya dimasukkan kedalam QPixmap
        img = imutils.resize(image, width=480)
        height, width, channel = img.shape
        step = channel * width
        qImg = QImage(img.data, width, height, step, QImage.Format_RGB888)
        self.ui.label.setPixmap(QPixmap.fromImage(qImg))

    ##ini buat ngontrol timer buat ngambil gambar `frame by frame`
    def controlTimer(self):
        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(1)

    ##tekan esc untuk exit dari GUI
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


    ##ini buat ngakses tombolnya pake keyboard trus ngirim data serial berupa karakter
    def keyReleaseEvent(self, event):
        ##tombol arah atas
        if event.key() == Qt.Key_Up:
            print("Maju")
            # data = str("w")
            # serialData.write(data.encode())

        ##tombol arah kanan
        elif event.key() == Qt.Key_Right:
            print("Kanan")
            # data = str("d")
            # serialData.write(data.encode())

        ##tombol arah bawah
        elif event.key() == Qt.Key_Down:
            print("Mundur")
            # data = str("s")
            # serialData.write(data.encode())

        ##tombol arah kiri
        elif event.key() == Qt.Key_Left:
            print("Kiri")
            # data = str("a")
            # serialData.write(data.encode())

    ##fungsi buat deteksi tombol keyboardnya telah dilepas (key_release)
    def stop(self):
        print("stop!")


## ini program intinya
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
