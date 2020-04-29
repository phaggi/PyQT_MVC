from abc import ABCMeta, abstractmethod


class CplusDObserver(metaclass=ABCMeta):
    """
    Абстрактный суперкласс для всех наблюдателей.
    """

    @abstractmethod
    def model_is_changed(self):
        """
        Метод который будет вызван у наблюдателя при изменении модели.
        """
        pass
