from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import pyqtSignal
from Utility.CplusDObserver import CplusDObserver
from Utility.CplusDMeta import CplusDMeta
from View.MainWindow import Ui_MainWindow


class Cplusdview(QMainWindow, CplusDObserver, metaclass=CplusDMeta):
    """
    Класс отвечающий за визуальное представление Cplusdmodel.
    """

    def __init__(self, in_controller, in_model, parent=None):
        """
        Конструктор принимает ссылки на модель и контроллер.
        """
        super(QMainWindow, self).__init__(parent)
        self.m_controller = in_controller
        self.m_model = in_model

        # подключаем визуальное представление
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # регистрируем представление в качестве наблюдателя
        self.m_model.add_observer(self)

        # устанавливаем валидаторы полей ввода данных
        self.ui.le_c.setValidator(QDoubleValidator())
        self.ui.le_d.setValidator(QDoubleValidator())

        # связываем событие завершения редактирования с методом контроллера
        self.ui.le_c.editingFinished.connect(self.m_controller.set_c)
        self.ui.le_d.editingFinished.connect(self.m_controller.set_d)

    def model_is_changed(self):
        """
        Метод вызывается при изменении модели.
        Запрашивает и отображает значение суммы.
        """
        sum = str(self.m_model.sum)
        self.ui.le_result.setText(sum)
