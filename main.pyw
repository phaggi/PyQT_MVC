import sys
from PyQt5.QtWidgets import QApplication

from Model.CplusDModel import CplusDModel
from Controller.CplusDController import CplusDController


def main():
    app = QApplication(sys.argv)

    # создаём модель
    model = CplusDModel()

    # создаём контроллер и передаём ему ссылку на модель
    controller = CplusDController(model)

    app.exec()


if __name__ == '__main__':
    sys.exit(main())
