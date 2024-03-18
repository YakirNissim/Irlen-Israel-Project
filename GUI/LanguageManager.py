import os
import pandas as pd
import pickle
from Modules.ExceptionsAndGlobalFunctions import *

PathRecovery = r"Modules\GUI\Data"
FileRecovery = r'language_key.data'
PathLanguageFile = r'Modules\GUI\Language file.csv'


def loading_language_dict():
    if not os.path.exists(PathLanguageFile):
        raise LanguageFileError()
    languages_dict = pd.read_csv(PathLanguageFile).set_index('keys').to_dict()

    if os.path.exists(PathRecovery + r'\\' + FileRecovery):
        with open(PathRecovery + r'\\' + FileRecovery, 'rb') as language_key_data:
            language_key = pickle.load(language_key_data)
    else:
        language_key = 'English'
        if not os.path.exists(PathRecovery):    os.makedirs(PathRecovery)
        with open(PathRecovery + r'\\' + FileRecovery, 'wb') as language_key_data:
            pickle.dump(language_key, language_key_data)
    return languages_dict, language_key


class LanguageManager:
    (__languages_dict, __language_key) = loading_language_dict()
    language_dict = __languages_dict[__language_key]

    @classmethod
    def __repr__(cls):
        return "Language Manager"

    @classmethod
    def language_dict_updating(cls, new_key='English'):
        if new_key in cls.__languages_dict.keys():
            cls.__language_key = new_key
            with open(r'Modules\GUI\Data\language_key.data', 'wb') as language_key_data:
                pickle.dump(cls.__language_key, language_key_data)
            cls.language_dict = cls.__languages_dict[cls.__language_key]

    @classmethod
    def get_language_dictionary(cls):
        return cls.__languages_dict[cls.__language_key]

    @classmethod
    def get_language_options_list(cls):
        return list(cls.__languages_dict.keys())

    @classmethod
    def str_concat_fix(cls, key, str_s='', str_e=''):
        if cls.language_dict['justify'] == 'right' and len(str_s) > 0 and len(str_e) == 0:
            return cls.language_dict[key] + str_s[::-1]
        if cls.language_dict['justify'] == 'right' and len(str_s) == 0 and len(str_e) > 0:
            return str_e[::-1] + cls.language_dict[key]
        return str_s + cls.language_dict[key] + str_e

    @staticmethod
    def FixString(str_in):
        str_in = str_in.strip()
        while '  ' in str_in:
            str_in = str_in.replace("  ", " ")
        if str_in != '':
            return str_in

    @staticmethod
    def linebreak_string(str_in, char_num=None, char_linebreak=False):
        """the char linebreak is '#'"""
        if char_num is int:
            i = str_in[:char_num].rindex(" ")
            return str_in[:i] + '\n' + str_in[i + 1:]
        if char_linebreak:
            return str_in.replace('#', '\n')
