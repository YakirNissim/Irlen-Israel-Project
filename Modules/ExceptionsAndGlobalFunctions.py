#   Exceptions:
class PrescriptionTypeError(TypeError):
    def __str__(self):
        return "The entered data does not match the Prescription type format"


class EPreTypeError(TypeError):
    def __init__(self, EPre, list_correct_EPre_keys, list_EPre_values):
        self.__EPre = EPre
        self.__EPre_keys = list_correct_EPre_keys
        self.__EPre_values = list_EPre_values

    def __str__(self):
        str_ret = f"The entered data does not match the EPre format!\n"
        if type(self.__EPre) is not dict:
            str_ret += f"\tAll value types in EPre are: <class 'dict'>" \
                       f"\n\tOne of the values is of {type(self.__EPre)} type\n"
        else:
            str_ret += f"\tcorrect items is:\n"
            for item in map(lambda k, v=self.__EPre_values: (k, v), self.__EPre_keys):
                str_ret += f"\t\t{item[0]} => {type(item[1][0])} or {type(item[1][1])}\n"
            str_ret += f"\tvalue items is:\n"
            for item in self.__EPre.items():
                str_ret += f"\t\t{item[0]} => {type(item[1])}\n"
        return str_ret


class DeliveryAddress(TypeError):
    def __init__(self, delivery_address, list_correct_delivery_address_keys, list_delivery_address_values):
        self.__delivery_address = delivery_address
        self.__delivery_address_keys = list_correct_delivery_address_keys
        self.__delivery_address_values = list_delivery_address_values

    def __str__(self):
        str_ret = f"The entered data does not match the DeliveryAddress format!\n"
        if type(self.__delivery_address) is not dict:
            str_ret += f"\tcorrect type is - <class 'dict'>" \
                       f"\n\tDeliveryAddress type is {type(self.__delivery_address)}\n"
        else:
            str_ret += f"\tcorrect items is:\n"
            for item in map(lambda k, v=self.__delivery_address_values: (k, v), self.__delivery_address_keys):
                str_ret += f"\t\t{item[0]} => {type(item[1][0])} or {type(item[1][1])}\n"
            str_ret += f"\tDeliveryAddress items is:\n"
            for item in self.__delivery_address.items():
                str_ret += f"\t\t{item[0]} => {type(item[1])}\n"
        return str_ret


class PaymentMethods(ValueError):
    def __init__(self, payment_methods):
        self.__payment_methods = payment_methods

    def __str__(self):
        return f"The entered PaymentMethods ({self.__payment_methods}) does not match the PaymentMethods format"


class OrderTypeError(TypeError):
    def __str__(self):
        return "The entered data does not match the Order type format"


class DateValueError(ValueError):
    def __init__(self, date):
        self.__date = date

    def __str__(self):
        return f"The entered data ({self.__date}) does not match the date format"


class PrescriptionListTypeError(ValueError):
    def __str__(self):
        return "The entered data does not match the prescriptions list format"


class ProfileError(Exception):
    def __init__(self, profile, list_correct_profile_keys, list_profile_values):
        self.__profile = profile
        self.__profile_keys = list_correct_profile_keys
        self.__profile_values = list_profile_values

    def __str__(self):
        str_ret = f"The entered data does not match the profile format!\n"
        if type(self.__profile) is not dict:
            str_ret += f"\tcorrect type is - <class 'dict'>\n\tprofile type is {type(self.__profile)}\n"
        else:
            str_ret += f"\tcorrect items is:\n"
            for item in map(lambda k, v=self.__profile_values: (k, v), self.__profile_keys):
                if item[0] in ["first name", "last name"]:
                    str_ret += f"\t\t{item[0]} => {type(item[1][1])}\n"
                    continue
                str_ret += f"\t\t{item[0]} => {type(item[1][0])} or {type(item[1][1])}\n"
            str_ret += f"\tprofile items is:\n"
            for item in self.__profile.items():
                str_ret += f"\t\t{item[0]} => {type(item[1])}\n"
            str_ret += f'Note that the value of the keys - "{self.__profile_keys[0]}" and "{self.__profile_keys[1]}"' \
                       f' cannot be {type(None)}!!!'
        return str_ret

    @staticmethod
    def __item_constructor(key, value):
        return key, value


class DeveloperKeyError(ValueError):
    def __str__(self):
        return "The Developer Key is wrong"


class LanguageFileError(FileNotFoundError):
    def __str__(self):
        return 'The "Language file" was not found!'


#   Global Functions
def date_to_string(date):
    return f'{date[0]}/{date[1]}/20{str(date[2]).zfill(2)}'