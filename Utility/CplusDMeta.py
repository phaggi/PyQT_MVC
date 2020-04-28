"""
Модуль реализации метакласса, необходимого для работы представления.

pyqtWrapperType - метакласс общий для оконных компонентов Qt.
ABCMeta - метакласс для реализации абстрактных суперклассов.

CplusDMeta - метакласс для представления.
"""

from PyQt5.QtCore import QObject
from abc import ABCMeta

pyqtWrapperType = type(QObject)


class CplusDMeta(pyqtWrapperType, ABCMeta): pass
