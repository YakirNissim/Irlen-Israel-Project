from Modules.Exceptions import *
import pickle
from Modules.CustomerManager import CustomerManager
import os

DeveloperKey = r'Shulamit'


class SecurityManager:
    # public methods:

    def __init__(self):
        self.__developer_key = DeveloperKey
        self.__list_customer_manager = []

    def __repr__(self):
        return f'Security Manager Object'

    def list_customers_managers(self, developer_key):
        if self.__developer_key == developer_key:
            return self.__list_customer_manager
        return None

    def add_customers_manager(self, username, password=None, CustomerManagerObject=None):
        if self.__search_customers_manager(username) is None:
            if CustomerManagerObject is None:
                CustomerManagerObject = CustomerManager(username)
            self.__list_customer_manager += [(username, password, CustomerManagerObject)]
            return CustomerManagerObject
        return None

    def get_customers_manager(self, username, password):
        customers_manager = self.__search_customers_manager(username)
        if customers_manager is not None:
            if customers_manager[1] == password:
                return customers_manager[2]

    def remove_customers_manager(self, username, password):
        customers_manager = self.__search_customers_manager(username)
        if customers_manager is not None and customers_manager[1] == password:
            self.__list_customer_manager.remove(customers_manager)
            return "success"
        return "failed"

    def data_backup(self, developer_key, path, file_name):
        if developer_key == self.__developer_key:
            if not os.path.exists(path):    return "ErrorPath"
            with open(f'{path}\{file_name}', 'wb') as backup_pickle_file:
                pickle.dump(self.__list_customer_manager, backup_pickle_file)
                return "success"
        return "ErrorKey"

    def data_recovery(self, developer_key, file):
        if developer_key == self.__developer_key:
            if not os.path.exists(file):    return "ErrorFile"
            with open(file, 'rb') as recovery_pickle_file:
                self.__list_customer_manager = pickle.load(recovery_pickle_file)
                return "success"
        return "ErrorKey"

    def security_update_customers_manager(self, username, password, new_username, new_password):
        customers_manager = self.__search_customers_manager(username)
        if self.remove_customers_manager(username, password) == "success":
            if self.add_customers_manager(new_username, new_password, customers_manager[2]) is None:
                self.add_customers_manager(*customers_manager)
                return "ErrorUsername"
            else:
                customers_manager[2].repr_name = new_username
                return "success"
        else:
            return "failed"

    # private methods:
    def __search_customers_manager(self, username):
        date_list = self.list_customers_managers(self.__developer_key)
        username_list = [i[0] for i in date_list]
        if date_list is None:
            raise DeveloperKeyError()
        elif username in username_list:
            return date_list[username_list.index(username)]
