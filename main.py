import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import (
    QPainter,
    QColor,
)
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QMainWindow
)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.gen.clicked.connect(self.draw_circle)
        self.draw_circle_flag = False
    
    def draw_circle(self):
        self.draw_circle_flag = True
        self.update()

    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(245, 245, 0))
        if self.draw_circle_flag:
            x, y = randint(0, 400), randint(0, 500)
            d = randint(100, 200)
            qp.drawEllipse(x, y, d, d)
            self.draw_circle_flag = False
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
