from View.CplusDView import CplusDView


class CplusDController():
    """
    Класс CplusDController представляет реализацию контроллера.
    Согласовывает работу представления с моделью.
    """

    def __init__(self, inModel):
        """
        Конструктор принимает ссылку на модель.
        Конструктор создаёт и отображает представление.
        """
        self.mModel = inModel
        self.mView = CplusDView(self, self.mModel)

        self.mView.show()

    def setC(self):
        """
        При завершении редактирования поля ввода данных для C,
        контроллер изменяет свойство c модели.
        """
        c = self.mView.ui.le_c.text()
        self.mModel.c = float(c)

    def setD(self):
        """
        При завершении редактирования поля ввода данных для D,
        контроллер изменяет свойство d модели.
        """
        d = self.mView.ui.le_d.text()
        self.mModel.d = float(d)
