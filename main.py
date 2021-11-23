import sys
from random import randint

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import QPoint, Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False

    def run(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            painter = QPainter()
            painter.begin(self)
            painter.setPen(QPen(Qt.red, 5, Qt.SolidLine))
            painter.drawEllipse(QPoint(50, 50), randint(10, 50), randint(10, 50))
            self.pushButton.hide()
            painter.end()
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())