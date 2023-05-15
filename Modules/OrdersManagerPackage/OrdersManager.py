from Modules.OrdersManagerPackage.Order import Order


class OrdersManager:
    # public methods:
    def __init__(self):
        self.__list_orders = ()

    def __repr__(self):
        return "Orders Manager"

    # Orders methods
    def list_orders(self):
        return [order[1].get() for order in self.__list_orders]

    def list_date_orders(self):
        return [order[0] for order in self.__list_orders]

    def create_orders_report(self, file, mode, orders):
        pass

    # Order methods
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
        date_list = self.list_date_orders()
        if date in date_list:
            order = self.__list_orders[date_list.index(date)]
            return order.get_order(), order
        return None

    def get_last_order(self):
        if len(self.__list_orders) > 0:
            last_order = self.__list_orders[0][1]
            return last_order.get(), last_order
        return None

    # Prescription methods
    @staticmethod
    def add_pre(order, irlen_pre, e_pre1=None, e_pre2=None):
        order.add_pre(irlen_pre, e_pre1, e_pre2)
        return True

    def remove_pre(self, order, pre):
        if order.len() < 2:
            self.remove_order(order.date())
            return "remove order"
        else:
            return order.remove_pre(pre)

    # private methods:
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
