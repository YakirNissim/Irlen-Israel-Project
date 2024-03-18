import pickle
import os
from Modules import *
from typing import Any

PathRecovery = r"C:\Users\ASUS\OneDrive\שולחן העבודה\Irlen Israel\Shulamit\test"
FileRecovery = r'MainTeat.test'
DeveloperKey = r'Shulamit'


class ShulamitSoftware:
    def __init__(self):
        self.__security_manager = None
        self.__loading()
        self.__manager = None
        self.__manager_name = None
        self.__customer_name = None
        self.root_window = RootWindow()
        self.__case_dict = {'LogInFrame: sign_in': self.sign_in,
                            'LogInFrame: sign_up': self.sign_up,

                            'CustomersManagerFrame: adding_new_customer': self.adding_new_customer,
                            'CustomersManagerFrame: search_customer': self.search_customer,
                            'CustomersManagerFrame: edit_security_data': self.edit_security_data,
                            'CustomersManagerFrame: sign_out': self.sign_out,
                            'CustomersManagerFrame: setting': self.setting,

                            'AppSetting: back': self.setting_back,
                            'AppAddingNewCustomer: add_customer': self.add_customer,
                            'AppCustomerSearch: results_search': self.results_search,

                            'AppCustomer: customer_profile': self.customer_profile,
                            'AppCustomer: adding_new_order': self.adding_new_order,
                            'AppCustomer: order_search': self.order_search,
                            'AppCustomer: order_report': self.order_report,

                            'AppCustomerProfile: edit_profile': self.edit_profile,

                            'AppCustomerEditProfile: update_profile': self.update_profile,
                            'AppCustomerEditProfile: update_profile_back': self.update_profile_back,
                            }

        self.root_window.WindowFrame(LogInFrame,
                                     command_case=self.__CaseManager,
                                     title_case='LogInFrame: ')
        self.root_window.mainloop()
        self.__data_backup()

    def __loading(self):
        print('\n=================')
        print('__loading')
        print('=================\n')
        LanguageManager()
        self.__security_manager = SecurityManager()
        if os.path.exists(PathRecovery + r'\\' + FileRecovery):
            self.__security_manager.data_recovery(DeveloperKey, PathRecovery + r'\\' + FileRecovery)

    def __data_backup(self):
        print('\n=================')
        print('__data_backup')
        print('=================\n')
        if not os.path.exists(PathRecovery):    os.makedirs(PathRecovery)
        self.__security_manager.data_backup(DeveloperKey, PathRecovery, FileRecovery)

    def __CaseManager(self, *args, **kwargs):
        print('\n=================')
        print('__CaseManager')
        print('=================\n')
        return self.__case_dict[kwargs['Case']](*args, **kwargs)

    """ LogInFrame """

    def sign_in(self, Username: str, Password: str, *args, **kwargs):
        print('\n=================')
        print('sign_in')
        print('=================\n')
        if Password == '':  Password = None
        self.__manager = self.__security_manager.get_customers_manager(Username, Password)
        if self.__manager is None:
            return False
        self.__manager_name = Username
        self.root_window.WindowFrame(CustomersManagerFrame,
                                     customers_manager_name=self.__manager_name,
                                     command_case=self.__CaseManager,
                                     title_case='CustomersManagerFrame: ')
        return True

    def sign_up(self, Username: str, Password: str, *args, **kwargs):
        print('\n=================')
        print('sign_up')
        print('=================\n')
        self.__manager = self.__security_manager.add_customers_manager(Username, Password)
        if self.__manager is None:
            return False
        self.__manager_name = Username
        self.root_window.WindowFrame(CustomersManagerFrame,
                                     customers_manager_name=self.__manager_name,
                                     command_case=self.__CaseManager,
                                     title_case='CustomersManagerFrame: ')
        return True

    """ CustomersManagerFrame """

    def adding_new_customer(self, windows_master: Any, *args, **kwargs):
        print('\n=================')
        print('adding_new_customer')
        print('=================\n')
        AppAddingNewCustomer(windows_master=windows_master,
                             command_case=self.__CaseManager,
                             title_case='AppAddingNewCustomer: ')

    def search_customer(self, windows_master: Any, *args, **kwargs):
        print('\n=================')
        print('search_customer')
        print('=================\n')
        AppCustomerSearch(windows_master=windows_master,
                          command_case=self.__CaseManager,
                          title_case='AppCustomerSearch: ',
                          customers_list=self.__manager.list_customers())
        print('ShulamitSoftware')
        print('search_customer')

    def setting(self, windows_master: Any, *args, **kwargs):
        print('\n=================')
        print('setting')
        print('=================\n')
        AppSetting(windows_master=windows_master,
                   command_case=self.__CaseManager,
                   title_case='AppSetting: ')

    def edit_security_data(self, windows_master: Any, *args, **kwargs):
        print('\n=================')
        print('edit_security_data')
        print('=================\n')

    def sign_out(self, *args, **kwargs):
        print('\n=================')
        print('sign_out')
        print('=================\n')
        self.__data_backup()
        self.__manager = None
        self.__manager_name = None
        self.__customer_name = None
        self.root_window.WindowFrame(LogInFrame,
                                     command_case=self.__CaseManager,
                                     title_case='LogInFrame: ')

    def app_customer(self, windows_master: Any, *args, **kwargs):
        print('\n=================')
        print('app_customer')
        print('=================\n')
        AppCustomer(windows_master=windows_master,
                    command_case=self.__CaseManager,
                    title_case='AppCustomer: ',
                    customer_name=self.__customer_name)
        self.customer_profile(windows_master=windows_master)

    """ AppAddingNewCustomer """

    def add_customer(self, windows_master: Any, Profile: dict, *args, **kwargs):
        print('\n=================')
        print('add_customer')
        print('=================\n')
        self.__customer_name = self.__manager.add_cust(Profile)
        if self.__customer_name is not None:
            self.app_customer(windows_master=windows_master,  *args, **kwargs)
            return True
        else:
            return False

    """ AppSetting """

    def setting_back(self, windows_master: Any, *args, **kwargs):
        print('\n=================')
        print('setting_back')
        print('=================\n')
        self.root_window.frame.GeometryAndLanguageManager()
        self.adding_new_customer(windows_master=windows_master,
                                 *args, **kwargs)
        print('back')

    """ AppCustomerSearch """

    def results_search(self, windows_master: Any, results_search: str, *args, **kwargs):
        print('\n=================')
        print('results_search')
        print('=================\n')
        self.__customer_name = results_search
        self.app_customer(windows_master=windows_master, *args, **kwargs)
        print(results_search)

    """ AppCustomer """

    def customer_profile(self, windows_master: Any, *args, **kwargs):
        print('\n=================')
        print('customer_profile')
        print('=================\n')
        AppCustomerProfile(windows_master=windows_master,
                           command_case=self.__CaseManager,
                           title_case='AppCustomerProfile: ',
                           profile=self.__manager.get_profile_cust(self.__customer_name))

    def adding_new_order(self, windows_master: Any, *args, **kwargs):
        print('\n=================')
        print('adding_new_order')
        print('=================\n')

    def order_search(self, windows_master: Any, *args, **kwargs):
        print('\n=================')
        print('order_search')
        print('=================\n')

    def order_report(self, windows_master: Any, *args, **kwargs):
        print('\n=================')
        print('order_report')
        print('=================\n')

    """ AppCustomerProfile """

    def edit_profile(self, windows_master: Any, *args, **kwargs):
        print('\n=================')
        print('edit_profile')
        print('=================\n')
        AppCustomerEditProfile(windows_master=windows_master,
                               command_case=self.__CaseManager,
                               title_case='AppCustomerEditProfile: ',
                               old_profile=self.__manager.get_profile_cust(self.__customer_name))

    """ AppCustomerEditProfile """

    def update_profile(self, windows_master: Any, Profile: dict, *args, **kwargs):
        print('\n=================')
        print('update_profile')
        print('=================\n')
        self.__manager.update_profile_cust(self.__customer_name, Profile)
        self.update_profile_back(windows_master, *args, **kwargs)

    def update_profile_back(self, windows_master: Any, *args, **kwargs):
        print('\n=================')
        print('update_profile_back')
        print('=================\n')
        self.customer_profile(windows_master=windows_master,  *args, **kwargs)


if __name__ == '__main__':
    ShulamitSoftware()
    pass
