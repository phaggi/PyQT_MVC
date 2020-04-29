class Cplusdmodel:
    """
    Класс Cplusdmodel представляет собой реализацию модели данных.
    В модели хранятся значения переменных c, d и их сумма.
    Модель предоставляет интерфейс, через который можно работать
    с хранимыми значениями.

    Модель содержит методы регистрации, удаления и оповещения
    наблюдателей.
    """

    def __init__(self):
        self._model_c = 0
        self._model_d = 0
        self._model_sum = 0

        self._model_observers = []  # список наблюдателей

    @property
    def c(self):
        return self._model_c

    @property
    def d(self):
        return self._model_d

    @property
    def sum(self):
        return self._model_sum

    @c.setter
    def c(self, value):
        self._model_c = value
        self._model_sum = self._model_c + self._model_d
        self.notify_observers()

    @d.setter
    def d(self, value):
        self._model_d = value
        self._model_sum = self._model_c + self._model_d
        self.notify_observers()

    def add_observer(self, in_observer):
        self._model_observers.append(in_observer)

    def removeObserver(self, in_observer):
        self._model_observers.remove(in_observer)

    def notify_observers(self):
        for x in self._model_observers:
            x.model_is_changed()