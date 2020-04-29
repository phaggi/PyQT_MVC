import sys
from PyQt5.QtWidgets import QApplication

from Model.Cplusdmodel import Cplusdmodel
from Controller.Cplusdcontroller import Cplusdcontroller


def main():
    app = QApplication(sys.argv)

    # создаём модель
    model = Cplusdmodel()

    # создаём контроллер и передаём ему ссылку на модель
    controller = Cplusdcontroller(model)

    app.exec()


if __name__ == '__main__':
    sys.exit(main())
