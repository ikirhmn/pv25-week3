import sys
 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()

        x = 0
        y = 0

        self.text = f'x: {x},  y: {y}'

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        # mouse tracking didisable secara default
        # perlu dienable dulu
        self.setMouseTracking(True)

        self.setLayout(grid)
        self.setWindowTitle("Task Week 3 - Rizki Rahman Maulana - F1D022093")
        self.setGeometry(350,350, 750, 600)
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = f'x: {x},  y: {y}'
        self.label.setText(text)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
