from Modules.ExceptionsAndGlobalFunctions import *
from Modules.OrdersManager import OrdersManager


class Customer:
    # public methods:
    def __init__(self, profile):
        self.repr_name = profile["first name"] + " " + profile["last name"]
        self.__profile = profile
        self.__orders_manager = OrdersManager()

        # optional
        self.__questionnaires = None

    def __repr__(self):
        if self.repr_name is None:
            return 'Customer Object'
        else:
            return f'Customer Object for "{self.repr_name}" customer'

    def get_profile(self):
        return self.__profile

    def update_profile(self, new_profile):
        self.__profile = new_profile
        self.repr_name = self.__profile["first name"] + " " + self.__profile["last name"]

    def get_orders_manager(self):
        return self.__orders_manager

    # private methods:


class CustomerManager:
    # public methods:
    def __init__(self, username=None):
        """ values in list_customer is - (customer_name, Customer Object) """
        self.__list_customer = []
        self.repr_name = username

    def __repr__(self):
        if self.repr_name is None:
            return f'Customer Manager Object'
        else:
            return f'Customer Manager Object for "{self.repr_name}" customer manager'

    #   Customers methods
    def list_customers(self):
        return [customer[0] for customer in self.__list_customer]

    #   Customer methods
    def search_cust(self, customer_name):
        if self.__search_customer(customer_name) is None:
            return False
        return True

    def add_cust(self, profile, CustomerObject=None):
        self.__check_profile_dictionary(profile)
        customer_name = profile["first name"] + " " + profile["last name"]
        if customer_name not in [customer[0] for customer in self.__list_customer]:
            if CustomerObject is None:
                CustomerObject = Customer(profile)
            CustomerObject.repr_name = CustomerObject.get_orders_manager().repr_name = customer_name
            self.__list_customer += [(customer_name, CustomerObject)]
            self.__list_customer = sorted(self.__list_customer)
            return customer_name
        return None

    def get_profile_cust(self, customer_name):
        customer = self.__search_customer(customer_name)
        if customer is not None:
            return customer[1].get_profile()

    def remove_cust(self, customer_name):
        customer = self.__search_customer(customer_name)
        if customer is not None:
            self.__list_customer.remove(customer)
            return True
        return False

    def update_profile_cust(self, customer_name, new_profile):
        old_customer = self.__search_customer(customer_name)
        if old_customer is None:
            return False
        new_customer_name = new_profile["first name"] + " " + new_profile["last name"]

        if self.add_cust(new_profile, old_customer[1]) is not None:  # The new profile included a new customer name
            self.remove_cust(old_customer)
            return True
        elif old_customer[0] == new_customer_name:
            old_customer[1].update_profile(new_profile)
            return True
        return False

    def get_orders_manager_cust(self, customer_name):
        customer = self.__search_customer(customer_name)
        if customer is not None:
            return customer[1].get_orders_manager()
        return None

    # private methods:
    @staticmethod
    def __check_profile_dictionary(profile):
        list_profile_keys = ["first name", "last name", "parent name", "phone", 'City', 'Street', 'Building number',
                             'Apartment', 'ZIP code', "Email", "referred by", "reason for referral"]
        list_profile_values = [None, ""]
        if type(profile) is not dict:
            raise ProfileError(profile, list_profile_keys, list_profile_values)
        for key in list_profile_keys:
            if key not in profile.keys():
                raise ProfileError(profile, list_profile_keys, list_profile_values)
        for value in profile.values():
            if value is not None and type(value) is not str:
                raise ProfileError(profile, list_profile_keys, list_profile_values)
        if profile["first name"] is None or profile["last name"] is None:
            raise ProfileError(profile, list_profile_keys, list_profile_values)

    def __search_customer(self, customer_name):
        date_list = self.list_customers()
        if customer_name in date_list:
            return self.__list_customer[date_list.index(customer_name)]
