import sys
import random

from PyQt5 import uic
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.do_paint = False

        self.CircleButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        D = random.randint(20, 121)
        x = random.randint(int(D / 2), 480 - int(D / 2))
        y = random.randint(int(D / 2), 450 - int(D / 2))
        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(QPoint(x, y), int(D / 2), int(D / 2))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())