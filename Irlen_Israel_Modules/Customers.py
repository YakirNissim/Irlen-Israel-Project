import pickle
import time
import datetime
from Irlen_Israel_Modules.Orders import *


class Customers:

    def __init__(self, full_name, parent_name=None, phone=None, email=None):
        self.__name = full_name
        self.parent_name = parent_name
        self.phone = phone
        self.email = email
        self.order_log = {}

    def ger_profile(self):
        return {"full_name": self.__name, "parent_name": self.parent_name, "phone": self.phone, "email": self.email}

    def edit_profile(self, full_name=None, parent_name=None, phone=None, email=None):
        if not full_name is None:
            self.__name = full_name

        if not parent_name is None:
            self.parent_name = parent_name

        if not phone is None:
            self.phone = phone

        if not email is None:
            self.email = email

    def add_order(self, order, date=None):
        """ The "date" parameter type is a string and the format is: "YYYY-MM-DD" """
        if date is None:
            date = datetime.date.today()
        else:
            date = datetime.date.fromisoformat(date)
        if date in self.order_log.keys():
            self.order_log[date] += [order]
        else:
            self.order_log[date] = [order]

    def order_removal(self, order_removal):
        if order_removal in self.order_log.keys():
            del self.order_log[order_removal]
        else:
            return 'The order does not exist!'

    def get_orders(self, key=None, from_date=None, to_date=None):
        try:
            if key is None:
                return [list(x) for x in self.order_log.items()]

            elif key == 'date':
                return [from_date, self.order_log[from_date]]

            elif key == 'range dates':
                return [list(x) for x in self.order_log.items() if from_date >= x[0] >= to_date]

            elif key == 'last order':
                return [max(self.order_log.keys()), self.order_log[max(self.order_log.keys())]]

            elif key == 'first order':
                return [min(self.order_log.keys()), self.order_log[min(self.order_log.keys())]]

        except:
            return []

    def get_list_order(self):
        return list(sorted(self.order_log.keys()).__reversed__())


def main():
    pass


if __name__ == '__main__':
    main()
