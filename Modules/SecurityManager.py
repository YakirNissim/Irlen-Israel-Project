from Modules.ExceptionsAndGlobalFunctions import *
import pickle
from Modules.CustomerManager import CustomerManager


class SecurityManager:
    # public methods:

    def __int__(self):
        self.__developer_key = 'pvcpvc311'
        self.__list_customer_manager = []

    def list_customers_managers(self, developer_key):
        if self.__developer_key == developer_key:
            return self.__list_customer_manager
        return None

    def add_customers_manager(self, username, password=None, CustomerManagerObject=None):
        if self.__search_customers_manager(username) is None:
            if CustomerManagerObject is None:
                CustomerManagerObject = CustomerManager()
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

    def data_backup(self, developer_key, path):
        if developer_key == self.__developer_key:
            with open(f'{path}.BackupPickle', 'wb') as backup_pickle_file:
                pickle.dump(self.__list_customer_manager, backup_pickle_file)
                return "success"
        return "ErrorKey"

    def data_recovery(self, developer_key, file):
        if developer_key == self.__developer_key:
            try:
                with open(file, 'rb') as recovery_pickle_file:
                    self.__list_customer_manager = pickle.load(recovery_pickle_file)
                    return "success"
            except IOError:
                return "ErrorFile"
        return "ErrorKey"

    def security_update_customers_manager(self, username, password, new_username, new_password):
        customers_manager = self.__search_customers_manager(username)
        if self.remove_customers_manager(username, password) is "success":
            if self.add_customers_manager(new_username, new_password, customers_manager[2]) is None:
                self.add_customers_manager(*customers_manager)
                return "ErrorUsername"
            else:
                return "success"
        else:
            return "failed"

    # private methods:
    def __search_customers_manager(self, username):
        date_list = self.list_customers_managers(self.__developer_key)
        if date_list is None:
            raise DeveloperKeyError()

        if username in date_list:
            return self.__list_customer_manager[date_list.index(username)]
