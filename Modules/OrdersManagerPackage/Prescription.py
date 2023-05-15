from Modules.ExceptionsAndGlobalFunctions import *


class Prescription:
    """
         Prescription type format:
            str: irlen_pre
            e_pre1 type: list [2X4] or Nune
            e_pre2 type: list [2X4] or Nune
    """

    # public methods:
    def __init__(self, irlen_pre, e_pre1=None, e_pre2=None):
        self.__check_prescription_type_format(irlen_pre, e_pre1, e_pre2)
        self.__check_EPre_format(e_pre1, e_pre2)

        self.__irlen_pre = irlen_pre
        self.__e_pre1 = e_pre1
        self.__e_pre2 = e_pre2

    def get(self):
        return self.__irlen_pre, self.__e_pre1 if self.__e_pre1 is None else list(self.__e_pre1), \
               self.__e_pre2 if self.__e_pre2 is None else list(self.__e_pre2)

    def __repr__(self):
        return 'Prescription Object'

    # private methods:
    @staticmethod
    def __check_prescription_type_format(irlen_pre, e_pre1, e_pre2):
        if type(irlen_pre) is not str or \
                (e_pre1 is not None and type(e_pre1) is not list) or \
                (e_pre2 is not None and type(e_pre2) is not list):
            raise PrescriptionTypeError()

    @staticmethod
    def __check_EPre_format(e_pre1, e_pre2):
        for e_pre in [e_pre1, e_pre2]:
            if e_pre is not None:
                if not(type(e_pre) is list and len(e_pre) == 2 and len(e_pre[0]) == 4 and len(e_pre[1]) == 4):
                    raise EPreTypeError()
