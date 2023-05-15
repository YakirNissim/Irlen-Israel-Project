from Modules.ExceptionsAndGlobalFunctions import *


class Prescription:
    """
         Prescription type format:
            str: irlen_pre
            e_pre1 type: list [2X4] or Nune
            e_pre2 type: list [2X4] or Nune
    """

    # public methods:
    def __init__(self, irlen_pre, e_pre1=None, e_pre2=None):
        self.__check_prescription_type_format(irlen_pre, e_pre1, e_pre2)
        self.__check_EPre_format(e_pre1, e_pre2)

        self.__irlen_pre = irlen_pre
        self.__e_pre1 = e_pre1
        self.__e_pre2 = e_pre2

    def __repr__(self):
        return 'Prescription Object'

    def get(self):
        return self.__irlen_pre, self.__e_pre1 if self.__e_pre1 is None else list(self.__e_pre1), \
               self.__e_pre2 if self.__e_pre2 is None else list(self.__e_pre2)

    # private methods:
    @staticmethod
    def __check_prescription_type_format(irlen_pre, e_pre1, e_pre2):
        if type(irlen_pre) is not str or \
                (e_pre1 is not None and type(e_pre1) is not list) or \
                (e_pre2 is not None and type(e_pre2) is not list):
            raise PrescriptionTypeError()

    @staticmethod
    def __check_EPre_format(e_pre1, e_pre2):
        for e_pre in [e_pre1, e_pre2]:
            if e_pre is not None:
                if not(type(e_pre) is list and len(e_pre) == 2 and len(e_pre[0]) == 4 and len(e_pre[1]) == 4):
                    raise EPreTypeError()


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

    def __repr__(self):
        return f'Order Object -> "{date_to_string(self.__date)}"'

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
            if type(p) is not list:
                raise PrescriptionListTypeError()


class OrdersManager:
    # public methods:
    def __init__(self):
        self.repr_name = None
        self.__list_orders = ()

    def __repr__(self):
        if self.repr_name is None:
            return "Orders Manager"
        else:
            return f'Orders Manager for "{self.repr_name}" customer'

    #   Orders methods
    def list_orders(self):
        return [order[1].get() for order in self.__list_orders]

    def list_date_orders(self):
        return [order[0] for order in self.__list_orders]

    def create_orders_report(self, file, mode, orders):
        pass

    #   Order methods
    def add_order(self, date, list_prescriptions):
        if date not in self.list_date_orders():
            order = Order(date, list_prescriptions)
            self.__sorted_add(date, order)
            return True
        return False

    def remove_order(self, date):
        date_list = self.list_date_orders()
        if date in date_list:
            index_date = date_list.index(date)
            self.__list_orders = self.__list_orders[:index_date] + self.__list_orders[index_date+1:]
            return True
        return False

    def update_date(self, new_date, old_date):
        date_list = self.list_date_orders()
        if new_date in date_list or old_date not in date_list:
            return False
        order = self.__list_orders[date_list.index(old_date)]
        if order[1].update_date(new_date):
            self.__sorted_add(new_date, order[1])
            self.remove_order(old_date)
            return True
        return False

    def search_order(self, date):
        order = self.__search_order(date)
        if order is None:
            return None
        return order[1].get()

    def get_last_order(self):
        if len(self.__list_orders) > 0:
            return self.__list_orders[0][1].get()
        return None

    #   Prescription methods
    def add_pre(self, date, irlen_pre, e_pre1=None, e_pre2=None):
        order = self.__search_order(date)
        if order is not None:
            order[1].add_pre(irlen_pre, e_pre1, e_pre2)
            return True
        return False

    def remove_pre(self, date, pre_o):
        order = self.__search_order(date)
        if order is None:
            return "order not found"
        if not order[1].remove_pre(pre_o):
            return "Pre not found"
        if order[1].len() > 0:
            return "remove Pre"
        else:
            self.remove_order(date)
            return "remove order"

    # private methods:
    def __search_order(self, date):
        date_list = self.list_date_orders()
        if date in date_list:
            return self.__list_orders[date_list.index(date)]
        return None

    def __sorted_add(self, date, order):
        num_date = self.__date_number(date)
        list_orders = [(date, order)] + list(self.__list_orders)
        new_order_index = 0
        while True:
            if new_order_index+1 > len(list_orders)-1:
                break

            if num_date < self.__date_number(list_orders[new_order_index+1][0]):
                list_orders[new_order_index], list_orders[new_order_index+1] = \
                    list_orders[new_order_index+1], list_orders[new_order_index]
                new_order_index += 1
                continue
            break
        self.__list_orders = tuple(list_orders)

    @staticmethod
    def __date_number(date):
        return int(f'{date[2]}{str(date[1]).zfill(2)}{str(date[0]).zfill(2)}')
