class CplusDModel:
    """
    Класс CplusDModel представляет собой реализацию модели данных.
    В модели хранятся значения переменных c, d и их сумма.
    Модель предоставляет интерфейс, через который можно работать
    с хранимыми значениями.

    Модель содержит методы регистрации, удаления и оповещения
    наблюдателей.
    """

    def __init__(self):
        self._mC = 0
        self._mD = 0
        self._mSum = 0

        self._mObservers = []  # список наблюдателей

    @property
    def c(self):
        return self._mC

    @property
    def d(self):
        return self._mD

    @property
    def sum(self):
        return self._mSum

    @c.setter
    def c(self, value):
        self._mC = value
        self._mSum = self._mC + self._mD
        self.notifyObservers()

    @d.setter
    def d(self, value):
        self._mD = value
        self._mSum = self._mC + self._mD
        self.notifyObservers()

    def addObserver(self, inObserver):
        self._mObservers.append(inObserver)

    def removeObserver(self, inObserver):
        self._mObservers.remove(inObserver)

    def notifyObservers(self):
        for x in self._mObservers:
            x.modelIsChanged()