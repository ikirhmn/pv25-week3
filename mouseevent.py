import sys
import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


class Task3(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()

        x = 0
        y = 0

        self.text = f'x: {x},  y: {y}'

        self.label = QLabel(self.text, self)
        self.label.setStyleSheet("font-size: 14px; padding: 5px;")
        self.label.move(50, 50)

        self.setMouseTracking(True)
        self.label.setMouseTracking(True)
        self.label.setAttribute(Qt.WA_Hover)

        self.label.installEventFilter(self) 

        self.setLayout(grid)
        self.setWindowTitle("Task Week 3 - Rizki Rahman Maulana - F1D022093")
        self.setGeometry(350,350, 750, 600)
        self.show()

    def mouseMoveEvent(self, e):
        if e.button() == Qt.NoButton:
            x = e.x()
            y = e.y()
            text = f'x: {x},  y: {y}'
            self.label.setText(text)
    def eventFilter(self, obj, e):
        if obj == self.label and e.type() == e.Enter:
            self.moveLabelRandomly()
        return super().eventFilter(obj, e)
         
     def moveLabelRandomly(self):
        max_x = max(0, self.width() - self.label.width())
        max_y = max(0, self.height() - self.label.height())
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)
        self.label.move(QPoint(new_x, new_y))

def main():
    app = QApplication(sys.argv)
    ex = Task3()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
