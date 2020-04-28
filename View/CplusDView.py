from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import pyqtSignal
from Utility.CplusDObserver import CplusDObserver
from Utility.CplusDMeta import CplusDMeta
from View.MainWindow import Ui_MainWindow


class CplusDView(QMainWindow, CplusDObserver, metaclass=CplusDMeta):
    """
    Класс отвечающий за визуальное представление CplusDModel.
    """

    def __init__(self, inController, inModel, parent=None):
        """
        Конструктор принимает ссылки на модель и контроллер.
        """
        super(QMainWindow, self).__init__(parent)
        self.mController = inController
        self.mModel = inModel

        # подключаем визуальное представление
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # регистрируем представление в качестве наблюдателя
        self.mModel.addObserver(self)

        # устанавливаем валидаторы полей ввода данных
        self.ui.le_c.setValidator(QDoubleValidator())
        self.ui.le_d.setValidator(QDoubleValidator())

        # связываем событие завершения редактирования с методом контроллера
        '''self.connectNotify(self.ui.le_c, pyqtSignal("editingFinished()"),
                     self.mController.setC)
        self.connectNotify(self.ui.le_d, pyqtSignal("editingFinished()"),
                     self.mController.setD)'''
        self.ui.le_c.editingFinished.connect(self.mController.setC)
        self.ui.le_d.editingFinished.connect(self.mController.setD)

    def modelIsChanged(self):
        """
        Метод вызывается при изменении модели.
        Запрашивает и отображает значение суммы.
        """
        sum = str(self.mModel.sum)
        self.ui.le_result.setText(sum)
