import random
import string
import os
Failed_count = 0

PrescriptionData = {'Patient Name': None, 'Expiration Date': None, 'Pupillary Distance': None, 'Prescribed by': None}
DistanceOD = {'Sphere': None, 'Cylinder': None, 'Axis': None, 'Prism': None, 'Base': None}
DistanceOS = {'Sphere': None, 'Cylinder': None, 'Axis': None, 'Prism': None, 'Base': None}
AddOD = {'Sphere': None, 'Cylinder': None, 'Axis': None, 'Prism': None, 'Base': None}
AddOS = {'Sphere': None, 'Cylinder': None, 'Axis': None, 'Prism': None, 'Base': None}

PathRecovery = r"C:\Users\ASUS\OneDrive\שולחן העבודה\Irlen Israel\Shulamit\test"
FileRecovery = r'TestModules.test'
DeveloperKey = r'Shulamit'


def test_modules():
    test_Prescription_class()
    test_Order_class()
    test_OrdersManager_class()
    test_Customer_class()
    test_CustomerManager_class()
    test_SecurityManager_class()
    print(f"Failed counter = {Failed_count}")
    pass


def test_SecurityManager_class():
    import Modules

    print("SecurityManager class:\n")

    def init():
        print("Test of __init__ function:")
        list_para_test = [
            ((1,), 'exception'),
            ((), "success")]
        num_test = 1
        for para in list_para_test:
            test_object = test__init__fun(test_class=Modules.SecurityManager,
                                          parameters=para[0],
                                          num_test=num_test,
                                          correct_output=para[1],
                                          with_print=False)
            num_test += 1
        return test_object

    def repr_test(test_object):
        print("\nTest of __repr__ function:")
        test_fun(test_object=test_object,
                 fun=Modules.SecurityManager.__repr__,
                 parameters=None,
                 num_test=1,
                 correct_output='Security Manager Object',
                 with_print=True)

    def list_customers_managers(test_object, developer_key, extended_data=False):
        print("\nTest of list_customers_managers function (manual check!):")
        print(f"output:")
        list_customers_managers = test_object.list_customers_managers(developer_key)
        if list_customers_managers is None: print('the list is None!')
        elif extended_data:
            print('the list is:')
            for i in test_object.list_customers_managers(developer_key):
                print(f"\t\t{i}")
        return list_customers_managers

    def add_customers_manager(test_object, num_random_managers=1, extended_data=False):
        global Failed_count

        print("\nTest of add_customers_manager function:")

        list_manager = []
        for i in range(num_random_managers*2):
            if i <= num_random_managers:
                random_manager = (word_constructor(Hebrew=False), word_constructor(Hebrew=False))  # (username, password)
            else:
                random_manager = (word_constructor(Hebrew=False), None)  # (username, password=None)
            print(f"\t\tTest {i + 1}: ", end='')
            if extended_data:
                print(f'manager = "(username: {random_manager[0]} password {random_manager[1]}')
            result = test_object.add_customers_manager(*random_manager)
            if random_manager not in list_manager and result is not None:
                print(f"\t\t status = success")
            elif random_manager in list_manager and result is None:
                print(f"\t\t status = success")
            else:
                Failed_count += 1
                print(f"\t\t status = Failed")
                if extended_data:   print(f"\t\t return = {result}")
            print('\t\tchecking attempt Re-add:', end=' ')
            if test_object.add_customers_manager(*random_manager) is not None:
                print(f"\t\t status = Failed")
                if extended_data:   print(f"\t\t return = {result}")
                Failed_count += 1
            else:   print(f"\t\t status = success")
            list_manager += [random_manager]

    def get_customers_manager(test_object, list_managers):
        global Failed_count

        print("\nTest of get_customers_manager function:")

        manager = random.choice(list_managers)
        i = 0

        print(f"\t\tTest {i + 1}: checking of correct username and password", end=' -> ')
        if test_object.get_customers_manager(manager[0], manager[1]) is not None:
            print(f'Success')
        else:
            print(f"Failed")
            Failed_count += 1

        i += 1
        print(f"\t\tTest {i + 1}: checking of correct username and wronging password", end=' -> ')
        check = False
        while not check:
            wronging_password = word_constructor(Hebrew=False)
            check = wronging_password != manager[1]
        if test_object.get_customers_manager(manager[0], wronging_password) is None:
            print(f'Success')
        else:
            print(f"Failed")
            Failed_count += 1

        i += 1
        print(f"\t\tTest {i + 1}: checking of wronging username", end=' -> ')
        check = False
        while not check:
            wronging_username = word_constructor(Hebrew=False)
            check = wronging_username not in [i[0] for i in list_managers]
        if test_object.get_customers_manager(wronging_username, wronging_password) is None:
            print(f'Success')
        else:
            print(f"Failed")
            Failed_count += 1
        pass

    def remove_customers_manager(test_object, list_managers):
        global Failed_count

        print("\nTest of remove_customers_manager function:")

        manager = random.choice(list_managers)
        i = 0

        print(f"\t\tTest {i + 1}: checking of correct username and wronging password", end=' -> ')
        check = False
        while not check:
            wronging_password = word_constructor(Hebrew=False)
            check = wronging_password != manager[1]
        if test_object.remove_customers_manager(manager[0], wronging_password) == 'failed':
            print(f'Success')
        else:
            print(f"Failed")
            Failed_count += 1

        i += 1
        print(f"\t\tTest {i + 1}: checking of wronging username", end=' -> ')
        check = False
        while not check:
            wronging_username = word_constructor(Hebrew=False)
            check = wronging_username not in [i[0] for i in list_managers]
        if test_object.remove_customers_manager(wronging_username, wronging_password) == 'failed':
            print(f'Success')
        else:
            print(f"Failed")
            Failed_count += 1

        i += 1
        print(f"\t\tTest {i + 1}: checking of correct username and password", end=' -> ')
        if test_object.remove_customers_manager(manager[0], manager[1]) == 'success' and \
                manager[0] not in [i[0] for i in test_object.list_customers_managers(DeveloperKey)]:
            print(f'Success')
        else:
            print(f"Failed")
            Failed_count += 1
        return manager

    def data_backup(test_object, developer_key, path, file_name):
        global Failed_count

        print("\nTest of data_backup function:")

        i = 0

        print(f"\t\tTest {i + 1}: checking of wronging developer_key", end=' -> ')
        check = False
        while not check:
            wronging_developer_key = word_constructor(Hebrew=False)
            check = wronging_developer_key != developer_key
        if test_object.data_backup(wronging_developer_key, path, file_name) == 'ErrorKey':
            print(f'Success')
        else:
            print(f"Failed")
            Failed_count += 1

        i += 1
        print(f"\t\tTest {i + 1}: checking of correct developer_key and wronging path", end=' -> ')
        check = False
        while not check:
            wronging_path = path + f'\{word_constructor(Hebrew=False)}'
            check = not os.path.exists(wronging_path)
        if test_object.data_backup(developer_key, wronging_path, file_name) == 'ErrorPath':
            print(f'Success')
        else:
            print(f"Failed")
            Failed_count += 1

        i += 1
        print(f"\t\tTest {i + 1}: checking of correct developer_key and path", end=' -> ')
        if test_object.data_backup(developer_key, path, file_name) == 'success':
            print(f'Success')
        else:
            print(f"Failed")
            Failed_count += 1
        pass

    def data_recovery(test_object, developer_key, file):
        global Failed_count

        print("\nTest of data_recovery function:")

        i = 0

        print(f"\t\tTest {i + 1}: checking of wronging developer_key", end=' -> ')
        check = False
        while not check:
            wronging_developer_key = word_constructor(Hebrew=False)
            check = wronging_developer_key != developer_key
        if test_object.data_recovery(wronging_developer_key, file) == 'ErrorKey':
            print(f'Success')
        else:
            print(f"Failed")
            Failed_count += 1

        i += 1
        print(f"\t\tTest {i + 1}: checking of correct developer_key and file", end=' -> ')
        check = False
        while not check:
            wronging_file = file + f'{word_constructor(Hebrew=False)}'
            check = not os.path.exists(wronging_file)
        if test_object.data_recovery(developer_key, wronging_file) == 'ErrorFile':
            print(f'Success')
        else:
            print(f"Failed")
            Failed_count += 1

        i += 1
        print(f"\t\tTest {i + 1}: checking of correct developer_key and path", end=' -> ')
        if test_object.data_recovery(developer_key, file) == 'success':
            print(f'Success')
        else:
            print(f"Failed")
            Failed_count += 1
        pass

    def security_update_customers_manager(test_object, list_managers):
        global Failed_count

        print("\nTest of security_update_customers_manager function:")

        i = 0
        check = False
        while not check:
            new_username = word_constructor(Hebrew=False)
            check = new_username not in [i[0] for i in list_managers]

        update_manager = random.choice(list_managers)
        i = 0

        print(f"\t\tTest {i + 1}: checking of correct username and wronging password", end=' -> ')
        check = False
        while not check:
            wronging_password = word_constructor(Hebrew=False)
            check = wronging_password != update_manager[1]
        if test_object.security_update_customers_manager(update_manager[0], wronging_password, new_username, None)\
                == 'failed':
            print(f'Success')
        else:
            print(f"Failed")
            Failed_count += 1

        i += 1
        print(f"\t\tTest {i + 1}: checking of wronging username", end=' -> ')
        check = False
        while not check:
            wronging_username = word_constructor(Hebrew=False)
            check = wronging_username not in [i[0] for i in list_managers]
        if test_object.security_update_customers_manager(wronging_username, wronging_password, new_username, None)\
                == 'failed':
            print(f'Success')
        else:
            print(f"Failed")
            Failed_count += 1

        i += 1
        print(f"\t\tTest {i + 1}: checking of correct username and password bat new username already exists", end=' -> ')
        check = False
        while not check:
            exists_username = random.choice([i[0] for i in list_managers])
            check = update_manager[0] != exists_username
        if test_object.security_update_customers_manager(update_manager[0], update_manager[1], exists_username, None)\
                == 'ErrorUsername':
            print(f'Success')
        else:
            print(f"Failed")
            Failed_count += 1

        i += 1
        print(f"\t\tTest {i + 1}: Checking username and password are correct and the new username doesn't exists",
              end=' -> ')
        if test_object.security_update_customers_manager(update_manager[0], update_manager[1], new_username, None) \
                == 'success':
            print(f'Success')
        else:
            print(f"Failed")
            Failed_count += 1
        return update_manager, new_username

    pass
    temp_object = init()
    repr_test(temp_object)
    list_customers_managers(temp_object, 'sdf')
    list_customers_managers(temp_object, DeveloperKey)
    add_customers_manager(temp_object, num_random_managers=10)
    temp_list_managers = list_customers_managers(temp_object, DeveloperKey)
    get_customers_manager(temp_object, temp_list_managers)
    manager = remove_customers_manager(temp_object, temp_list_managers)
    print(manager)
    data_backup(temp_object, DeveloperKey, PathRecovery, FileRecovery)
    data_recovery(temp_object, DeveloperKey, f'{PathRecovery}\{FileRecovery}')
    temp_list_managers = list_customers_managers(temp_object, DeveloperKey, extended_data=False)
    result = security_update_customers_manager(temp_object, temp_list_managers)
    print(f'update_manager = {result[0]}, \nnew_username = {result[1]}')

    print("=================================================\n\n")


def test_CustomerManager_class():
    import Modules

    print("CustomerManager class:\n")

    def init():
        print("Test of __init__ function:")
        list_para_test = [
            ((1, 2), 'exception'),
            ((), "success")]
        num_test = 1
        for para in list_para_test:
            test_object = test__init__fun(test_class=Modules.CustomerManager,
                                          parameters=para[0],
                                          num_test=num_test,
                                          correct_output=para[1],
                                          with_print=False)
            num_test += 1
        return test_object

    def repr_test(test_object):
        print("\nTest of __repr__ function:")
        test_fun(test_object=test_object,
                 fun=Modules.CustomerManager.__repr__,
                 parameters=None,
                 num_test=1,
                 correct_output='Customer Manager Object',
                 with_print=True)

        test_object.repr_name = "test repr"
        test_fun(test_object=test_object,
                 fun=Modules.CustomerManager.__repr__,
                 parameters=None,
                 num_test=2,
                 correct_output=f'Customer Manager Object for "test repr" customer manager',
                 with_print=True)

    def list_customers(test_object):
        print("\nTest of list_customers function (manual check!):")
        print(f"output:")
        for i in test_object.list_customers():
            print(f"\t\t{i}")

    #   Customer methods
    def search_cust(test_object):
        print("\nTest of search_cust function:")
        customer_list = test_object.list_customers()
        test_para_list = []
        while True:
            random_customer_name_not_in_customer_list = word_constructor() + ' ' + word_constructor()
            if random_customer_name_not_in_customer_list not in customer_list:
                break
        if len(customer_list) > 0:
            customer_name = random.choice(customer_list)
            test_para_list += [((customer_name,), True)]
        test_para_list += [((random_customer_name_not_in_customer_list,), False)]

        num_test = 1
        for para in test_para_list:
            print(f'\t', end='')
            test_fun(test_object=test_object,
                     fun=Modules.CustomerManager.search_cust,
                     parameters=para[0],
                     num_test=num_test,
                     correct_output=para[1],
                     with_print=True)
            print(f'\t\tcustomer name is "{para[0]}"')
            num_test += 1

    def add_cust(test_object, num_random_customers=1):
        print("\nTest of add_cust function (manual check!):")
        list_profile_keys = ["parent name", "phone", 'City', 'Street', 'Building number', 'Apartment', 'ZIP code',
                             "Email", "referred by", "reason for referral"]

        for i in range(num_random_customers):
            random_profile = {"first name": word_constructor(), "last name": word_constructor()}
            for key in list_profile_keys:
                random_profile[key] = None
            print(f"\t\tTest {i + 1} -> customer name = "
                  f"{random_profile['first name'] + ' ' + random_profile['last name']};", end='')
            if test_object.add_cust(random_profile) is not None:
                print(f" status = success")
            else:
                print(f" status = not success")
        i += 1
        print(f"\t\tTest {i + 1} -> customer name = "
              f"{random_profile['first name'] + ' ' + random_profile['last name']};", end='')
        if test_object.add_cust(random_profile) is not None:
            print(f" status = success")
        else:
            print(f" status = not success")

    def get_profile_cust(test_object):
        print("\nTest of get_profile_cust function:")
        list_profile_keys = ["first name", "last name", "parent name", "phone", 'City', 'Street', 'Building number',
                             'Apartment', 'ZIP code', "Email", "referred by", "reason for referral"]

        profile_test = []
        for profile in ["profile test", word_constructor()]:
            profile_dict = {}
            for key in list_profile_keys:
                profile_dict[key] = profile
            profile_test += [profile_dict]

        test_para_list = [((profile_test[0],), profile_test[0]), ((profile_test[1],), None)]
        test_object.add_cust(profile_test[0])

        num_test = 1
        for para in test_para_list:
            print(f'\t', end='')
            test_fun(test_object=test_object,
                     fun=Modules.CustomerManager.get_profile_cust,
                     parameters=(f"{para[0][0]['first name'] + ' ' + para[0][0]['last name']}",),
                     num_test=num_test,
                     correct_output=para[1],
                     with_print=True)
            num_test += 1

    def remove_cust(test_object):
        print("\nTest of remove_cust function:")
        list_profile_keys = ["first name", "last name", "parent name", "phone", 'City', 'Street', 'Building number',
                             'Apartment', 'ZIP code', "Email", "referred by", "reason for referral"]

        profile_test = []
        for profile in ["remove test", word_constructor()]:
            profile_dict = {}
            for key in list_profile_keys:
                profile_dict[key] = profile
            profile_test += [profile_dict]

        test_para_list = [((profile_test[0],), True), ((profile_test[1],), False)]
        test_object.add_cust(profile_test[0])

        num_test = 1
        for para in test_para_list:
            print(f'\t', end='')
            test_fun(test_object=test_object,
                     fun=Modules.CustomerManager.remove_cust,
                     parameters=(f"{para[0][0]['first name'] + ' ' + para[0][0]['last name']}",),
                     num_test=num_test,
                     correct_output=para[1],
                     with_print=True)
            num_test += 1

    def update_profile_cust(test_object):
        print("\nTest of update_profile_cust function:")
        list_profile_keys = ["parent name", "phone", 'City', 'Street', 'Building number', 'Apartment', 'ZIP code',
                             "Email", "referred by", "reason for referral"]
        customer_order_manager = None

        """ parameters value = (customer name, (parameter of a new profile), correct output) 
            parameter of a new profile = first name, last name, other values"""
        parameters = [(None, ("update test", "update test", None), None),
                      (f"{word_constructor()} {word_constructor()}", ("update test", "update test", None), False),
                      ("update test update test", ("update test", "update test", "update test"), True),
                      ("update test update test", ("update test 1", "update test", "update test 1"), True),
                      ("update test 1 update test", ("update test", "update test 2", "update test 2"), True),
                      ("update test update test 2", ("update test 3", "update test 3", "update test 3"), True),
                      ]

        test_para_list = []
        for para in parameters:
            profile_dict = {}
            profile_dict["first name"] = para[1][0]
            profile_dict["last name"] = para[1][1]
            for key in list_profile_keys:
                profile_dict[key] = para[1][2]
            if para[0] is not None:
                test_para_list += [[(para[0], profile_dict), para[2]]]
            else:
                test_object.add_cust(profile_dict)
                customer_order_manager = test_object.get_orders_manager_cust(f"{profile_dict['first name']} "
                                                                             f"{profile_dict['last name']}")

        num_test = 1
        for para in test_para_list:
            print(f'\t', end='')
            test_fun(test_object=test_object,
                     fun=Modules.CustomerManager.update_profile_cust,
                     parameters=(para[0]),
                     num_test=num_test,
                     correct_output=para[1],
                     with_print=True)
            if para[1] and customer_order_manager == test_object.get_orders_manager_cust(f"{para[0][1]['first name']} "
                                                                                         f"{para[0][1]['last name']}"):
                print(f"\t\t{customer_order_manager}")
            num_test += 1
        test_object.remove_cust("update test 3 update test 3")

    def get_orders_manager_cust(test_object):
        print("\nTest of get_orders_manager_cust function:")
        list_profile_keys = ["first name", "last name", "parent name", "phone", 'City', 'Street', 'Building number',
                             'Apartment', 'ZIP code', "Email", "referred by", "reason for referral"]

        profile_dict = {}
        for key in list_profile_keys:
            profile_dict[key] = "get_orders_manager_cust test"

        test_object.add_cust(profile_dict)

        print("\tTest 1\t", end='')
        if str(test_object.get_orders_manager_cust("get_orders_manager_cust test get_orders_manager_cust test")) == \
                'Orders Manager for "get_orders_manager_cust test get_orders_manager_cust test" customer':
            print("Passed => return: ", end='')
        else:
            print("Failed => return: ", end='')
        print(f"{test_object.get_orders_manager_cust('get_orders_manager_cust test get_orders_manager_cust test')}")

        print("\tTest 2\t", end='')
        random_name = word_constructor() + " " + word_constructor()
        if test_object.get_orders_manager_cust(random_name) is None:
            print("Passed => return: ", end='')
        else:
            print("Failed => return: ", end='')
        print(f"{test_object.get_orders_manager_cust(random_name)}")

    temp_object = init()
    repr_test(temp_object)
    list_customers(temp_object)
    search_cust(temp_object)
    add_cust(temp_object, 30)
    list_customers(temp_object)
    search_cust(temp_object)
    get_profile_cust(temp_object)
    remove_cust(temp_object)
    list_customers(temp_object)
    update_profile_cust(temp_object)
    get_orders_manager_cust(temp_object)
    print("=================================================\n\n")


def test_Customer_class():
    from Modules.CustomerManager import Customer

    print("Test Customer class:\n")

    def init():
        print("Test of __init__ function:")
        list_para_test = [
            ((), 'exception'),
            (({'first name': "Hello", 'last name': "World"},), "success")]
        num_test = 1
        for para in list_para_test:
            test_object = test__init__fun(test_class=Customer,
                                          parameters=para[0],
                                          num_test=num_test,
                                          correct_output=para[1],
                                          with_print=False)
            num_test += 1
        return test_object

    def repr_test(test_object):
        print("\nTest of __repr__ function:")
        print(test_object.repr_name)
        test_object.repr_name = "test repr"
        test_fun(test_object=test_object,
                 fun=Customer.__repr__,
                 parameters=None,
                 num_test=2,
                 correct_output=f'Customer Object for "test repr" customer',
                 with_print=True)

    def get_profile(test_object, correct_output):
        print("\nTest of get_profile function:")
        test_fun(test_object=test_object,
                 fun=Customer.get_profile,
                 parameters=None,
                 num_test=1,
                 correct_output=correct_output,
                 with_print=True)

    def update_profile(test_object, new_profile):
        print("\nTest of update_profile function:")
        new_profile = (new_profile,)
        test_fun(test_object=test_object,
                 fun=Customer.update_profile,
                 parameters=new_profile,
                 num_test=1,
                 with_print=True)
        pass

    def get_orders_manager(test_object):
        print("\nTest of get_order_manager function (Also included an object, manual check!):")
        manual_result_check(test_object=test_object,
                            correct_output="Orders Manager",
                            fun=Customer.get_orders_manager)

    temp_object = init()
    repr_test(temp_object)
    get_profile(temp_object, {'first name': "Hello", 'last name': "World"})
    update_profile(temp_object, {'first name': "Hello", 'last name': "World2"})
    get_profile(temp_object, {'first name': "Hello", 'last name': "World2"})
    get_orders_manager(temp_object)
    print("=================================================\n\n")


def test_OrdersManager_class():
    import Modules

    print("Test OrdersManager class:\n")

    def init():
        print("Test of __init__ function:")
        list_para_test = [
            ((1,), 'exception'),
            ((), "success")]
        num_test = 1
        for para in list_para_test:
            test__init__fun(test_class=Modules.OrdersManager,
                            parameters=para[0],
                            num_test=num_test,
                            correct_output=para[1],
                            with_print=False)
            num_test += 1

    def repr_test(test_object):
        print("\nTest of __repr__ function:")
        test_fun(test_object=test_object,
                 fun=Modules.OrdersManager.__repr__,
                 parameters=None,
                 num_test=1,
                 correct_output=f'Orders Manager',
                 with_print=True)

        test_object.repr_name = "test repr"
        test_fun(test_object=test_object,
                 fun=Modules.OrdersManager.__repr__,
                 parameters=None,
                 num_test=2,
                 correct_output=f'Orders Manager for "test repr" customer',
                 with_print=True)

    # Orders methods
    def list_orders(test_object):
        print("\nTest of list_orders function (manual check!):")
        print(f"output:")
        for i in test_object.list_orders():
            print(f"\t\t{i}")

    def list_date_orders(test_object):
        print("\nTest of list_date_orders function (manual check!):")
        print(f"output:")
        for i in list(map(Modules.date_to_string, test_object.list_date_orders())):
            print(f"\t\t{i}")

    # Order methods
    def add_order(test_object, date=None, list_prescriptions=None, num_random_orders=1):
        print("\nTest of add_order function (manual check!):")
        if date is None:
            random_order = None
            for i in range(num_random_orders):
                random_order = order_constructor(str(i+1))
                print(f"\t\tTest {i+1} -> date = {Modules.date_to_string(random_order[0])};"
                      f" status = {test_object.add_order(*tuple(random_order))}")
            i += 1
            print(f"\t\tTest {i+1} -> date = {Modules.date_to_string(random_order[0])};"
                  f" status = {test_object.add_order(*tuple(random_order))}")
        else:
            print(f"\t\tTest 1 -> date = {Modules.date_to_string(date)};"
                  f" status = {test_object.add_order(date, list_prescriptions)}")

    def remove_order(test_object, date=None, correct_output=None, with_print=True):
        print("\nTest of remove_order function:")
        if date is None:
            random_date_remove = random.choice(test_object.list_date_orders())
            if with_print:
                print(f'random date is {random_date_remove}')

            print("\t", end='')
            test_fun(test_object=test_object,
                     fun=Modules.OrdersManager.remove_order,
                     parameters=(random_date_remove,),
                     correct_output=True,
                     num_test=1,
                     with_print=with_print)

            print("\t", end='')
            test_fun(test_object=test_object,
                     fun=Modules.OrdersManager.remove_order,
                     parameters=(random_date_remove,),
                     correct_output=False,
                     num_test=2,
                     with_print=with_print)
        elif correct_output is not None:
            print("\t", end='')
            test_fun(test_object=test_object,
                     fun=Modules.OrdersManager.remove_order,
                     parameters=date,
                     correct_output=correct_output,
                     num_test=1,
                     with_print=with_print)
        else:
            print("Error:\tcorrect_output is None!")

    def update_date(test_object, with_print=True):
        print("\nTest of update_date function:")
        date_list = test_object.list_date_orders()
        random_date_in_date_list = []
        random_date_not_in_date_list = []

        for i in range(2):
            random_date_in_date_list += [random.choice(date_list)]
            while True:
                random_date = order_constructor()[0]
                if random_date not in date_list:
                    random_date_not_in_date_list += [random_date]
                    break

        if with_print:
            print(f'\trandom dates in date_list is {random_date_in_date_list}')
            print(f'\trandom dates not in date_list is {random_date_not_in_date_list}\n')

        """ parameters=(new_date, old_date) """
        test_para_list = [((random_date_not_in_date_list[0], random_date_not_in_date_list[1]), False),
                          ((random_date_in_date_list[0], random_date_in_date_list[1]), False),
                          ((random_date_not_in_date_list[0], random_date_in_date_list[0]), True)]
        num_test = 1
        for t in test_para_list:
            print("\t", end='')
            test_fun(test_object=test_object,
                     fun=Modules.OrdersManager.update_date,
                     parameters=t[0],
                     correct_output=t[1],
                     num_test=num_test,
                     with_print=with_print)
            num_test += 1
        print(f"\tTest {num_test-1}:\t{t[0][1]} => {t[0][0]}")

    def search_order(test_object, date=None, correct_output=None):
        print("\nTest of search_order function (Also included an object, manual check!):")
        date_list = test_object.list_date_orders()
        test_para_list = []
        if date is None:
            while True:
                random_date_not_in_date_list = order_constructor()[0]
                if random_date_not_in_date_list not in date_list:
                    break
            date = random.choice(date_list)

            test_para_list += [(date, "order", f"date = {Modules.date_to_string(date)}"),
                               (random_date_not_in_date_list, None,
                                f"date not in date list = {Modules.date_to_string(random_date_not_in_date_list)}")]
        else:
            test_para_list += [(date, correct_output, f"date = {Modules.date_to_string(date)}")]

        num_test = 1
        for t in test_para_list:
            print(f"Test{num_test} ({t[2]}):")
            print(f"\tResult test:")
            print(f"\t\tcorrect output = {t[1]}")
            print(f"\t\toutput\t\t   = {test_object.search_order(t[0])}")
            num_test += 1

    def get_last_order(test_object):
        print("\nTest of get_last_order function (Also included an object, manual check!):")
        if len(test_object.list_orders()) > 0:
            correct_output = "last order"
        else:
            correct_output = None
        manual_result_check(test_object=test_object,
                            correct_output=correct_output,
                            fun=Modules.OrdersManager.get_last_order)
        pass

    # Prescription methods
    def add_pre(test_object):
        print("\nTest of add_pre function:")
        date_list = test_object.list_date_orders()
        while True:
            random_date_not_in_date_list = order_constructor()[0]
            if random_date_not_in_date_list not in date_list:
                break
        date = random.choice(date_list)

        test_para_list = [((date, "add_pre_test", [1], None), False, "exception"),
                          ((random_date_not_in_date_list, "add_pre_test", None, None), True, False),
                          ((date, "add_pre_test", None, None), True, True)]

        num_test = 1
        for t in test_para_list:
            print("\t", end='')
            test_fun(test_object=test_object,
                     fun=Modules.OrdersManager.add_pre,
                     parameters=t[0],
                     correct_output=t[2],
                     num_test=num_test,
                     with_print=t[1])
            num_test += 1
        print(f"\tResult Test 3:\n\t\t{test_object.search_order(date)}")

    def remove_pre(test_object):
        print("\nTest of remove_pre function:")
        date_list = test_object.list_date_orders()
        while True:
            random_date_not_in_date_list = order_constructor()[0]
            if random_date_not_in_date_list not in date_list:
                break
        date = random.choice(date_list)
        """ date, pre_o """
        test_para_list = [((random_date_not_in_date_list, None), "order not found"),
                          ((date, None), "Pre not found"),
                          ]

        for pre in test_object.search_order(date)[1][:-1]:
            test_para_list += [((date, pre[0]), "remove Pre")]

        test_para_list += [((date, test_object.search_order(date)[1][-1][0]), "remove order")]

        num_test = 1
        for t in test_para_list:
            print("\t", end='')
            test_fun(test_object=test_object,
                     fun=Modules.OrdersManager.remove_pre,
                     parameters=t[0],
                     correct_output=t[1],
                     num_test=num_test,
                     with_print=True)
            num_test += 1
        pass

    init()
    temp_object = Modules.OrdersManager()
    repr_test(temp_object)
    list_orders(temp_object)
    list_date_orders(temp_object)
    add_order(temp_object, num_random_orders=10)
    list_orders(temp_object)
    list_date_orders(temp_object)
    remove_order(temp_object)
    list_date_orders(temp_object)
    list_orders(temp_object)
    update_date(temp_object)
    list_orders(temp_object)
    search_order(temp_object)
    get_last_order(temp_object)
    get_last_order(Modules.OrdersManager())
    add_pre(temp_object)
    remove_pre(temp_object)
    print("=================================================\n\n")


def test_Order_class():
    from Modules.OrdersManager import Order
    print("Test Order class:\n")

    def init():
        print("Test of __init__ function:")
        list_para_test = [
            (),
            (1,),
            (1, 2),
            ((13, 8, 1), 2),
            ((13, 8, 1), []),
            ((31, 81, 111), [[]]),
            ((13, 8, 1), [[]]),
            ((13, 8, 1), [()]),
            ((13, 8, 1), [["IrlenPre", [[1, 2, 3, 4], [1, 3, 4]]]])
        ]
        num_test = 1
        for para in list_para_test:
            test__init__fun(test_class=Order,
                            parameters=para,
                            num_test=num_test,
                            with_print=False)
            num_test += 1

        test__init__fun(test_class=Order,
                        parameters=((13, 8, 1), [["IrlenPre", [PrescriptionData, DistanceOD, DistanceOS, AddOD, AddOS]]]),
                        num_test=num_test,
                        correct_output="success",
                        with_print=True)

    def get():
        print("\nTest of get function (Also included an object, manual check!):")
        test_object = Order((13, 8, 1), [["IrlenPre", [PrescriptionData, DistanceOD, DistanceOS, AddOD, AddOS]]])
        correct_output = ((13, 8, 1), [('Prescription Object', ('IrlenPre', [PrescriptionData, DistanceOD, DistanceOS, AddOD, AddOS], None))])
        manual_result_check(test_object, correct_output, fun=Order.get)
        return test_object

    def add_pte(test_object):
        print("\nTest of add_pre function:")
        list_para_test = [(),
                          (1,),
                          (1, 2),
                          ("IrlenPre", 3),
                          ("IrlenPre", [[1]]),
                          (1, [[1, 2, 3, 4], [1, 2, 3, 4]])
                          ]
        num_test = 1

        for para in list_para_test:
            test_fun(test_object=test_object,
                     fun=Order.add_pre,
                     parameters=para,
                     correct_output="exception",
                     num_test=num_test,
                     with_print=False)
            num_test += 1

        test_fun(test_object=test_object,
                 fun=Order.add_pre,
                 parameters=("IrlenPre", [PrescriptionData, DistanceOD, DistanceOS, AddOD, AddOS]),
                 num_test=num_test,
                 with_print=True)
        num_test += 1

        correct_output = ((13, 8, 1), [('Prescription Object', ('IrlenPre', [[1, 2, 3, 4], [1, 2, 3, 4]], None)),
                                       ('Prescription Object', ('IrlenPre', [[1, 2, 3, 4], [1, 2, 3, 4]], None))])
        manual_result_check(test_object, correct_output, fun=Order.get)
        print("")

    def remove_pre(test_object):
        print("\nTest of remove_pre function:")
        num_test = 1
        temp_pre = test_object.get()[1][0][0]
        for correct_output in [True, False]:
            test_fun(test_object=test_object,
                     fun=Order.remove_pre,
                     parameters=(temp_pre,),
                     num_test=num_test,
                     correct_output=correct_output)
            manual_result_check(test_object=test_object, correct_output=((13, 8, 1),
                                                                         [('Prescription Object',
                                                                           ('IrlenPre', [[1, 2, 3, 4], [1, 2, 3, 4]],
                                                                            None))]), fun=Order.get)
            num_test += 1

    def len_test(test_object, correct_output):
        print("\nTest of len function:")
        test_fun(test_object=test_object,
                 fun=Order.len,
                 parameters=None,
                 num_test=1,
                 correct_output=correct_output)

    def date(test_object, correct_output):
        print("\nTest of date function:")
        test_fun(test_object=test_object,
                 fun=Order.date,
                 parameters=None,
                 num_test=1,
                 correct_output=correct_output)

    def update_date(test_object):
        print("\nTest of update_date function:")
        num_test = 1
        list_correct_output = [False, True]
        for new_date in [(32, -5, 120), (31, 5, 88)]:
            test_fun(test_object=test_object,
                     fun=Order.update_date,
                     parameters=(new_date,),
                     num_test=num_test,
                     correct_output=list_correct_output[num_test - 1])
            num_test += 1

    def repr_test(test_object):
        print("\nTest of __repr__ function:")
        test_fun(test_object=test_object,
                 fun=Order.__repr__,
                 parameters=None,
                 num_test=1,
                 correct_output=f'Order Object -> "{test_object.date()[0]}/{test_object.date()[1]}'
                                f'/20{str(test_object.date()[2]).zfill(2)}"',
                 with_print=True)

    init()
    temp_object = get()
    add_pte(temp_object)
    len_test(temp_object, 2)
    remove_pre(temp_object)
    len_test(temp_object, 1)
    date(temp_object, (13, 8, 1))
    repr_test(temp_object)
    update_date(temp_object)
    date(temp_object, (31, 5, 88))
    repr_test(temp_object)
    print("=================================================\n\n")


def test_Prescription_class():
    from Modules.OrdersManager import Prescription

    print("Test Prescription class:\n")

    def init_test():
        print("Test of __init__ function:")
        list_para_test = [(),
                          (1,),
                          (1, 2),
                          ("IrlenPre", 3),
                          ("IrlenPre", [[1]]),
                          (1, [[1, 2, 3, 4], [1, 2, 3, 4]])
                          ]
        num_test = 1
        for para in list_para_test:
            test__init__fun(test_class=Prescription,
                            parameters=para,
                            num_test=num_test,
                            with_print=False)
            num_test += 1

        test__init__fun(test_class=Prescription,
                        parameters=("IrlenPre", [PrescriptionData, DistanceOD, DistanceOS, AddOD, AddOS]),
                        num_test=num_test,
                        correct_output="success",
                        with_print=True)
        print("")

    def get_test():
        print("Test of get function:")
        # test 1:

        list_correct_output = [
            ("IrlenPre", None, None, None, None, None, None),

            ("IrlenPre", [PrescriptionData, DistanceOD, DistanceOS, AddOD, AddOS], None, None, None, None, None),

            ("IrlenPre", [PrescriptionData, DistanceOD, DistanceOS, AddOD, AddOS],
             [PrescriptionData, DistanceOD, DistanceOS, AddOD, AddOS], None, None, None, None)
        ]

        num_test = 1
        for correct_output in list_correct_output:
            test_object = Prescription(*correct_output)
            test_fun(test_object=test_object,
                     fun=Prescription.get,
                     parameters=None,
                     correct_output=correct_output,
                     num_test=num_test,
                     with_print=True)
            num_test += 1
        return test_object

    def repr_test(test_object):
        print("\nTest of __repr__ function:")
        test_fun(test_object=test_object,
                 fun=Prescription.__repr__,
                 parameters=None,
                 num_test=1,
                 correct_output='Prescription Object',
                 with_print=True)

    def private_methods(test_object):
        print('\nTest of "private methods":')
        print("Test 1", end=" ")
        try:
            test_object.__check_prescription_type_format("IrlenPre", [[1, 2, 3, 4], [1, 2, 3, 4]], None)
        except Exception as inst:
            print('Passed' + ":", end=" ")
            exception_func(inst, False)

        print("Test 2", end=" ")
        try:
            test_object.__check_EPre_format([[1, 2, 3, 4], [1, 2, 3, 4]], None)
        except Exception as inst:
            print('Passed' + ":", end=" ")
            exception_func(inst, False)

    init_test()
    temp_object = get_test()
    repr_test(temp_object)
    private_methods(temp_object)
    print("=================================================\n\n")


def test_fun(test_object,
             fun,
             parameters,
             num_test,
             correct_output=None,
             with_print=True):
    global Failed_count
    str_exception = "Failed"
    str_correct_output = "Passed"
    print(f"Test {num_test}", end='\t')
    if correct_output == "exception":
        str_exception, str_correct_output = str_correct_output, str_exception
    try:
        if parameters is None:
            output = fun(test_object)
        else:
            output = fun(test_object, *parameters)
    except Exception as inst:
        print(str_exception + ":", end=" ")
        exception_func(inst, with_print)
        if str_exception == "Failed":
            Failed_count += 1
    else:
        if with_print:
            if output == correct_output and with_print:
                print(f"{str_correct_output} => return: {correct_output}")
            else:
                Failed_count += 1
                print("Failed")
                print(f"value:\n output\t\t\t= {output}\n correct output = {correct_output}")



def test__init__fun(test_class,
                    parameters,
                    num_test,
                    correct_output="exception",
                    with_print=True):
    global Failed_count
    str_success = "Failed"
    str_exception = "Passed"
    if correct_output != "exception":
        str_exception, str_success = str_success, str_exception
    print(f"Test {num_test}", end='\t')
    try:
        test_object = test_class(*parameters)
        print(str_success + ':\tAn exception was not thrown!!!')
    except Exception as inst:
        print(str_exception + ":", end=" ")
        exception_func(inst, with_print)
        if str_exception == "Failed":
            Failed_count += 1
    else:
        return test_object


def exception_func(inst, with_print):
    print(f"An exception was thrown!!!\t{type(inst)}, \t{inst}")  # with the exception instance
    if with_print:
        print("Data exception:")
        print(f"\t{inst.args}")  # arguments stored in .args
        print(f"\t{inst}")  # __str__ allows args to be printed directly


def manual_result_check(test_object, correct_output, fun):
    print(f"\tResult test:")
    print(f"\t\toutput\t\t   = {fun(test_object)}")
    print(f"\t\tcorrect output = {correct_output}")


def order_constructor(num_pre=''):
    date = (random.randint(1, 31), random.randint(1, 12), random.randint(0, 99))
    list_pre = []
    for i in range(random.randint(1, 3)):
        list_pre += [Prescription_constructor(num_pre)]
    return date, list_pre


def Prescription_constructor(num_pre=''):
    return [f'IrlenPre {num_pre}'] + EPre_constructor()


def EPre_constructor():
    EPre = []
    for i in range(random.randint(1, 2)):
        EPre += [[PrescriptionData, DistanceOD, DistanceOS, AddOD, AddOS]]
    return EPre


def word_constructor(Hebrew=True):
    letter_list = ['א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'כ', 'ל', 'מ', 'נ', 'ס', 'ע', 'פ', 'צ', 'ק', 'ר',
                   'ש', 'ת']
    final_letter_list = ['א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'ך', 'ל', 'ם', 'ן', 'ס', 'ע', 'ף', 'ץ', 'ק',
                         'ר', 'ש', 'ת']
    word = ''
    for i in range(random.randint(1, 6)):
        if Hebrew:   word += random.choice(letter_list)
        else:   word += random.choice(string.ascii_letters)
    if Hebrew:   word += random.choice(final_letter_list)
    return word


if __name__ == '__main__':
    test_modules()

# Failed / Passed / manual check!
