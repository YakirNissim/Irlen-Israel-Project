from Modules.ExceptionsAndGlobalFunctions import *
from Modules.OrdersManagerPackage.Prescription import Prescription


class Order:
    """
    date struct:
        date = (dd, mm, yy)
     date type and value range:
        tuple: date
        int: dd; value range: 1 ~ 31
        int: mm; value range: 1 ~ 12
        int: yy; value range: 0 ~ 99

    list prescriptions struct:
        list_prescriptions = [(prescription1), (prescriptions2), ...]
            * type prescription: tuple
        len(list_prescriptions) > 0
    """

    # public methods:
    def __init__(self, date, list_prescriptions):
        self.__check_order_format(date, list_prescriptions)
        self.__check_date_format(date)
        self.__check_prescriptions_list_format(list_prescriptions)

        self.__date = date

        self.__tuple_prescriptions = []
        for p in list_prescriptions:
            self.__tuple_prescriptions += [Prescription(*tuple(p))]
        self.__tuple_prescriptions = tuple(self.__tuple_prescriptions)

    def get(self):
        return self.__date, [(pre, pre.get()) for pre in self.__tuple_prescriptions]

    def add_pre(self, irlen_pre, e_pre1=None, e_pre2=None):
        self.__tuple_prescriptions = self.__tuple_prescriptions + (Prescription(irlen_pre, e_pre1, e_pre2),)

    def remove_pre(self, pre_o):
        if pre_o in self.__tuple_prescriptions:
            self.__tuple_prescriptions = list(self.__tuple_prescriptions)
            self.__tuple_prescriptions.remove(pre_o)
            self.__tuple_prescriptions = tuple(self.__tuple_prescriptions)
            return True
        else:
            return False

    def len(self):
        return len(self.__tuple_prescriptions)

    def date(self):
        return self.__date

    def update_date(self, new_date):
        try:
            self.__check_date_format(new_date)
        except:
            return False
        else:
            self.__date = new_date
            return True

    def __repr__(self):
        return f'Order Object -> "{date_to_string(self.__date)}"'

    # private methods:
    @staticmethod
    def __check_order_format(date, list_prescriptions):
        if type(date) is not tuple or \
                type(list_prescriptions) is not list or \
                len(list_prescriptions) < 1:
            raise OrderTypeError()

    @staticmethod
    def __check_date_format(date):
        if len(date) != 3 or \
                type(date[0]) is not int or not 31 >= date[0] >= 1 or \
                type(date[1]) is not int or not 12 >= date[1] >= 1 or \
                type(date[2]) is not int or not 99 >= date[2] >= 0:
            raise DateValueError(date)

    @staticmethod
    def __check_prescriptions_list_format(list_prescriptions):
        for p in list_prescriptions:
            if type(p) is not tuple:
                raise PrescriptionListTypeError()
