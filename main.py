from Irlen_Israel_Modules import *
import time

def main():
    pass
    # # yakir = Customers_Manager.CustomersManager('yakir', '1234')
    # # yakir.save_manager()
    # yakir = Customers_Manager.CustomersManager.load_manager('yakir', '123')
    # # yakir.add_customer('yakir', phone='054')
    # # yakir.add_customer('anna')
    # # print(yakir.get_customers_list())
    # # yakir2 = yakir.get_customer('yakir')
    # # print(yakir2.phone)
    # # yakir2.add_order({1, 1, 2}, '1988-05-31')
    # # yakir2.add_order({0, 1, 7}, '1988-05-31')
    # # print(yakir2.get_orders())
    # # x = yakir.Customers_Manager.CustomersManager.security_code('yakir', 1234)
    # # yakir.Customers_Manager.CustomersManager.change_username_and_password(x, new_password='1234')
    # xx = yakir.security_code('yakir', '123')
    # time.sleep(0.5)
    # # xx = '15'
    # yakir.change_username_and_password(xx, 'yakir', '123')
    #
    # yakir.save_manager()
    app = GUI.App()
    app.start()
    print('manager:', app.manager)
    if app.manager is not None:
        app.manager.save_manager()




if __name__ == '__main__':
    main()
