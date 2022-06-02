import os
import pickle
import random
import threading

from Irlen_Israel_Modules.Customers import *


class CustomersManager:
    if not os.path.exists('Manager'):
        os.makedirs('Manager')

    def __init__(self, username, password=None):
        self.__security_code = None
        self.__username = username
        self.__password = password
        self.customers_dict = {}

    def add_customer(self, full_name, parent_name=None, phone=None, email=None):
        if full_name not in self.customers_dict.keys():
            self.customers_dict[full_name] = Customers(full_name, parent_name, phone, email)
        else:
            raise ValueError("A customer name already exists")

    def edit_profile(self, customer, full_name=None, parent_name=None, phone=None, email=None):
        if not full_name is None:
            self.customers_dict[full_name] = self.customers_dict[customer]
            del self.customers_dict[customer]
            customer = full_name
        self.customers_dict[customer].Customers.edit_profile(full_name, parent_name, phone, email)

    def get_customer(self, mame):
        return self.customers_dict[mame]

    def get_customers_list(self):
        return sorted(self.customers_dict.keys())

    def save_manager(self):
        with open(f'Manager/{self.__username}.pickle', 'wb') as save_pickle_file:
            pickle.dump(self, save_pickle_file)

    def security(self):
        self.__security_code = None

    def security_code(self, username, password=None):
        if (self.__password == password or self.__password is None) and self.__username == username:
            self.__security_code = str(random.randint(1, 99999)).zfill(5)
            threading.Timer(1.0, self.security).start()
            return self.__security_code
        else:
            print('tttt')
            return None

    def change_username_and_password(self, security_code, new_username=None, new_password=None):
        if self.__security_code == security_code and self.__security_code is not None:
            if new_username is not None:
                os.remove(f'Manager/{self.__username}.pickle')
                self.__username = new_username
                self.save_manager()

            if new_password is not None:
                self.__password = new_password
        else:
            self.__security_code = None

    @classmethod
    def load_manager(cls, username, password=None):
        try:
            with open(f'Manager/{username}.pickle', 'rb') as load_pickle_file:
                Manager = pickle.load(load_pickle_file)
                if password == Manager.__password or Manager.__password is None:
                    return Manager
                else:
                    return None
        except IOError:  # add more!!! (הקובץ לא נימצע)
            print(f'Manager/{username}.pickle')
            print('IOError')
            return 'IOError'
