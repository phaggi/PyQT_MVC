from View.Cplusdview import Cplusdview


class Cplusdcontroller():
    """
    Класс Cplusdcontroller представляет реализацию контроллера.
    Согласовывает работу представления с моделью.
    """

    def __init__(self, in_model):
        """
        Конструктор принимает ссылку на модель.
        Конструктор создаёт и отображает представление.
        """
        self.m_model = in_model
        self.m_view = Cplusdview(self, self.m_model)

        self.m_view.show()

    def set_c(self):
        """
        При завершении редактирования поля ввода данных для C,
        контроллер изменяет свойство c модели.
        """
        c = self.m_view.ui.le_c.text()
        self.m_model.c = float(c)

    def set_d(self):
        """
        При завершении редактирования поля ввода данных для D,
        контроллер изменяет свойство d модели.
        """
        d = self.m_view.ui.le_d.text()
        self.m_model.d = float(d)
