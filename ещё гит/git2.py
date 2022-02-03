import sys
import random

from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.color = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan',
                       'Blue', 'Magenta', 'Purple', 'Brown', 'Black']
        self.flag = False

    def run(self):
        self.flag = True
        self.repaint()

    def paintEvent(self, event):
        if self.flag:
            pen = QPen()
            pen.setWidth(3)
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(QColor(random.choice(self.color)))
            radius = random.randint(1, 600)
            painter.drawEllipse(random.randint(1, self.width() - radius), random.randint(1, self.height() - radius), radius, radius)
            painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())