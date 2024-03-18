import customtkinter
import os
from Modules.GUI.GUIDesign import *
from Modules.GUI.LanguageManager import LanguageManager as LM
import Modules
from typing import Any
import pickle

class CustomersManagerFrame(Frames.MainWindowFrame):

    def __init__(self,
                 customers_manager_name: str,
                 command_case: Any,
                 title_case: str,
                 geometry_manager=True,
                 *args, **kwargs):
        super().__init__(geometry_manager=False, *args, **kwargs)
        self.customer_manager_name = customers_manager_name[:20]
        self.command_case = command_case
        self.title_case = title_case
        self.name_selected_customer = ''

        self.title_customer_manager_label = customtkinter.CTkLabel(master=self.title_menu_frame,
                                                                   height=60,
                                                                   width=180,
                                                                   corner_radius=8,
                                                                   font=Fonts.AppWindowButton,
                                                                   fg_color=Colors.CustomerManagerFrame_title_control_label)

        self.app_customer_manage_menu_frame = customtkinter.CTkFrame(master=self.menu_frame)
        self.app_system_menu_frame = customtkinter.CTkFrame(master=self.menu_frame)

        self.adding_new_customer_button = Buttons.WindowCustomerManagerButtons(
            master=self.app_customer_manage_menu_frame,
            font=Fonts.AppWindowButton,
            command=self.__adding_new_customer_button_func)
        self.customer_search_button = Buttons.WindowCustomerManagerButtons(master=self.app_customer_manage_menu_frame,
                                                                           color=Colors.SignInWindowFrame_sign_in_button,
                                                                           font=Fonts.AppWindowButton,
                                                                           command=self.__customer_search_button_func)
        self.setting_button = Buttons.WindowCustomerManagerButtons(master=self.app_system_menu_frame,
                                                                   color=Colors.EditSecurityDataButton,
                                                                   font=Fonts.AppWindowButton,
                                                                   image=Images.setting_icon(),
                                                                   command=self.__setting_button_func)
        self.edit_security_data_button = Buttons.WindowCustomerManagerButtons(master=self.app_system_menu_frame,
                                                                              color=Colors.EditSecurityDataButton,
                                                                              font=Fonts.AppWindowButton,
                                                                              command=self.__edit_security_data_button_func)
        self.sign_out_button = Buttons.WindowCustomerManagerButtons(master=self.app_system_menu_frame,
                                                                    color=Colors.CustomerManagerFrame_sign_out[0],
                                                                    font=Fonts.AppWindowButton,
                                                                    image=Images.sign_out_button_image,
                                                                    border_color=Colors.CustomerManagerFrame_sign_out[
                                                                        1],
                                                                    command=self.__sign_out_button_func)
        self.space_label = customtkinter.CTkLabel(master=self.app_system_menu_frame, height=0, text='')

        if geometry_manager:
            self.GeometryAndLanguageManager()

    def GeometryAndLanguageManager(self):
        super().GeometryAndLanguageManager()
        self.menu_frame.grid_rowconfigure(1, weight=1)
        self.menu_frame.grid_columnconfigure(0, weight=1)

        self.title_customer_manager_label.configure(
            text=LM.language_dict['Welcome'] + '\n' + self.customer_manager_name, wraplength=170)
        self.adding_new_customer_button.configure(text=LM.language_dict['Adding a new customer'])
        self.edit_security_data_button.configure(text=LM.language_dict['Edit security data'])
        self.customer_search_button.configure(text=LM.language_dict['Customer search'])
        self.setting_button.configure(text=LM.language_dict['Setting'],
                                      compound=LM.language_dict['justify'])
        self.sign_out_button.configure(text=LM.language_dict['Sign out'],
                                       compound=LM.language_dict['justify'])

        self.title_customer_manager_label.grid(row=0, column=0, sticky="nswe", padx=13, pady=25)
        self.app_customer_manage_menu_frame.grid(row=0, sticky="nswe")
        self.app_system_menu_frame.grid(row=2, sticky="nswe")

        self.adding_new_customer_button.grid(row=0, padx=13, pady=2)
        self.customer_search_button.grid(row=1, padx=13, pady=2)

        self.setting_button.grid(row=0, padx=13, pady=2)
        self.edit_security_data_button.grid(row=1, padx=13, pady=2)
        self.sign_out_button.grid(row=2, padx=13, pady=2)
        self.space_label.grid(row=4)

        self.window_frame.grid_rowconfigure(0, weight=1)
        self.window_frame.grid_columnconfigure(0, weight=1)

        if LM.language_dict['justify'] == 'right':
            pass

    def DisplayAppWindowsFrame(self, windows_frame):
        self.DisplayWindowsFrame(windows_frame)

    def DisplayAppMenuFrame(self, menu_frame):
        try:
            self.app_menu_frame.destroy()
        except:
            pass
        if isinstance(menu_frame, tkinter.Frame):
            self.app_menu_frame = menu_frame
            self.app_menu_frame.grid_rowconfigure(0, weight=1)
            self.app_menu_frame.grid_columnconfigure(0, weight=1)
            self.app_menu_frame.grid(row=1, sticky="nswe")

    # @staticmethod
    def __adding_new_customer_button_func(self):
        self.command_case(Case=self.title_case + 'adding_new_customer',
                          windows_master=self, )

    # @staticmethod
    def __customer_search_button_func(self):
        self.command_case(Case=self.title_case + 'search_customer',
                          windows_master=self)

    def __edit_security_data_button_func(self):
        self.command_case(Case=self.title_case + 'edit_security_data',
                          windows_master=self)

    def __sign_out_button_func(self):
        self.command_case(Case=self.title_case + 'sign_out')

    def __setting_button_func(self):
        self.command_case(Case=self.title_case + 'setting',
                          windows_master=self)


class AppWindow:

    def __init__(self, windows_master, geometry_manager=True, menu_master=None):
        self.windows_master = windows_master
        self.app_menu_frame = None
        self.app_window_frame = customtkinter.CTkFrame(master=self.windows_master,
                                                       corner_radius=8,
                                                       fg_color=Colors.MainWindowFrame_app_background)

        self.title_label = customtkinter.CTkLabel(master=self.app_window_frame,
                                                  corner_radius=8,
                                                  text="",
                                                  font=Fonts.AppWindowsTitle,
                                                  fg_color=Colors.AppWindowsFrame,
                                                  height=50)
        self.window_frame = customtkinter.CTkFrame(master=self.app_window_frame,
                                                   corner_radius=8,
                                                   fg_color=Colors.AppWindowsFrame)

        if menu_master is not None:
            self.app_menu_frame = customtkinter.CTkFrame(master=menu_master)

        if geometry_manager:
            self.GeometryAndLanguageManager()

    def GeometryAndLanguageManager(self):
        self.app_window_frame.grid_rowconfigure(1, weight=1)
        self.app_window_frame.grid_columnconfigure(0, weight=1)

        self.title_label.grid(row=0, column=0, sticky="NSWE", padx=20, pady=10)
        self.window_frame.grid(row=1, column=0, sticky="nswe", padx=20, pady=10)


class ProfileEntryPack(customtkinter.CTkScrollableFrame):

    def __init__(self, profile_dict=None, geometry_manager=True, *args, **kwargs):
        super().__init__(fg_color=Colors.AppWindowsFrame, *args, **kwargs)
        list_profile_keys = ["first name", "last name", "parent name", "phone", 'City', 'Street', 'Building number',
                             'Apartment', 'ZIP code', "Email", "referred by", "reason for referral"]
        self.profile_dict = {}
        if profile_dict is None:
            for k in list_profile_keys:
                self.profile_dict[k] = None
        else:
            self.profile_dict = profile_dict


        self.first_name_EntryPack = Entries.EntryPack(self, text_key="First name",
                                                      entry_text_key="First name", add_start_entry_text='* ',
                                                      insert=self.profile_dict['first name'])
        self.last_name_EntryPack = Entries.EntryPack(self, text_key="Last name",
                                                     entry_text_key="Last name", add_start_entry_text='* ',
                                                     insert=self.profile_dict['last name'])
        self.parents_name_EntryPack = Entries.EntryPack(self, text_key="Parents name",
                                                        entry_text_key="Parents name",
                                                        insert=self.profile_dict['parent name'])
        self.phone_number_EntryPack = Entries.EntryPack(self, text_key="Phone number",
                                                        entry_text_key="Phone number",
                                                        insert=self.profile_dict['phone'])
        self.city_EntryPack = Entries.EntryPack(self, text_key="City", entry_text_key="City",
                                                insert=self.profile_dict['City'])
        self.street_EntryPack = Entries.EntryPack(self, text_key="Street", entry_text_key="Street",
                                                  insert=self.profile_dict['Street'])
        self.building_number_EntryPack = Entries.EntryPack(self, text_key="Building number",
                                                           entry_text_key="Building number",
                                                           insert=self.profile_dict['Building number'])
        self.apartment_EntryPack = Entries.EntryPack(self, text_key="Apartment", entry_text_key="Apartment",
                                                     insert=self.profile_dict['Apartment'])
        self.ZIP_EntryPack = Entries.EntryPack(self, text_key="ZIP code", entry_text_key="ZIP code",
                                               insert=self.profile_dict['ZIP code'])
        self.Email_EntryPack = Entries.EntryPack(self, text_key="Email", entry_text_key="Email",
                                                 insert=self.profile_dict['Email'])
        self.referred_by_EntryPack = Entries.EntryPack(self, text_key="Referred by",
                                                       entry_text_key="Referred by",
                                                       insert=self.profile_dict['referred by'])
        self.reason_for_referral_EntryPack = Entries.EntryPack(self, text_key="Reason for referral",
                                                               entry_text_key="Reason for referral",
                                                               insert=self.profile_dict['reason for referral'])

        self.dict_EntryPack = {'first_name_EntryPack': self.first_name_EntryPack,
                               'last_name_EntryPack': self.last_name_EntryPack,
                               'parents_name_EntryPack': self.parents_name_EntryPack,
                               'phone_number_EntryPack': self.phone_number_EntryPack,
                               'city_EntryPack': self.city_EntryPack,
                               'street_EntryPack': self.street_EntryPack,
                               'building_number_EntryPack': self.building_number_EntryPack,
                               'apartment_EntryPack': self.apartment_EntryPack,
                               'ZIP': self.ZIP_EntryPack,
                               'Email_EntryPack': self.Email_EntryPack,
                               'referred_by_EntryPack': self.referred_by_EntryPack,
                               'reason_for_referral_EntryPack': self.reason_for_referral_EntryPack,
                               }

        if geometry_manager:
            self.GeometryAndLanguageManager()

    def GeometryAndLanguageManager(self):
        for k in self.dict_EntryPack.keys():
            self.dict_EntryPack[k].GeometryAndLanguageManager()

    def GetProfileDict(self):
        return {
            'first name': LM.FixString(self.first_name_EntryPack.entry.get()),
            'last name': LM.FixString(self.last_name_EntryPack.entry.get()),
            'parent name': LM.FixString(self.parents_name_EntryPack.entry.get()),
            'phone': LM.FixString(self.phone_number_EntryPack.entry.get()),
            'City': LM.FixString(self.city_EntryPack.entry.get()),
            'Street': LM.FixString(self.street_EntryPack.entry.get()),
            'Building number': LM.FixString(self.building_number_EntryPack.entry.get()),
            'Apartment': LM.FixString(self.apartment_EntryPack.entry.get()),
            'ZIP code': LM.FixString(self.ZIP_EntryPack.entry.get()),
            'Email': LM.FixString(self.Email_EntryPack.entry.get()),
            'referred by': LM.FixString(self.referred_by_EntryPack.entry.get()),
            'reason for referral': LM.FixString(self.reason_for_referral_EntryPack.entry.get()),
        }


class SettingFrames(Frames.SettingFrame):
    def __init__(self, geometry_manager: bool = True, *args, **kwargs):
        super().__init__(*args, **kwargs,
                         fg_color=Colors.AppWindowsFrame)
        if geometry_manager:
            self.GeometryAndLanguageManager()

    def GeometryAndLanguageManager(self):
        self.language_combo_box_pack_frame.place(relx=0.09, rely=0.1)
        self.OK_button.place(relx=0.68, rely=0.85, anchor=tkinter.CENTER)
        self.back_button.place(relx=0.32, rely=0.85, anchor=tkinter.CENTER)
        if LM.language_dict['justify'] == 'right':
            self.language_combo_box_pack_frame.place(relx=0.3, rely=0.1)


class AppAddingNewCustomer(AppWindow):

    def __init__(self,
                 command_case: Any,
                 title_case: str,
                 geometry_manager=True,
                 *args, **kwargs):
        super().__init__(geometry_manager=False, *args, **kwargs)

        self.EntryPack_frame = ProfileEntryPack(master=self.window_frame)
        for k in self.EntryPack_frame.dict_EntryPack.keys():
            self.EntryPack_frame.dict_EntryPack[k].entry.bind('<Key>', self.__KP_Enter)
        self.command_add_customer_button = command_case
        self.title_case = title_case
        self.add_customer_button = Buttons.WindowCustomerManagerButtons(master=self.window_frame,
                                                                        color=Colors.SignInWindowFrame_sign_in_button,
                                                                        font=Fonts.AppWindowButton,
                                                                        command=self.__add_customer_button_func)
        self.windows_master.DisplayAppWindowsFrame(self.app_window_frame)
        self.windows_master.DisplayAppMenuFrame(self.app_menu_frame)

        if geometry_manager:
            tryAndLanguageManager()

    def GeometryAndLanguageManager(self):
        super().GeometryAndLanguageManager()
        self.EntryPack_frame.GeometryAndLanguageManager()
        self.window_frame.grid_rowconfigure(0, weight=1)
        self.window_frame.grid_columnconfigure(0, weight=1)
        self.title_label.configure(text=LM.language_dict['Adding a new customer'])
        self.add_customer_button.configure(text=LM.language_dict['Add a customer'])
        self.add_customer_button.grid(row=8, column=0, pady=16)
        i = 0
        for k in self.EntryPack_frame.dict_EntryPack.keys():
            self.EntryPack_frame.dict_EntryPack[k].text.grid(row=i, column=0, sticky="E", padx=10)
            self.EntryPack_frame.dict_EntryPack[k].entry.grid(row=i, column=1, sticky="W", padx=10)
            if LM.language_dict['justify'] == 'right':
                self.EntryPack_frame.dict_EntryPack[k].text.grid(row=i, column=1, sticky="E", padx=10)
                self.EntryPack_frame.dict_EntryPack[k].entry.grid(row=i, column=0, sticky="E", padx=10)
            i += 1

        self.EntryPack_frame.grid(row=0, column=0, padx=14, pady=10, sticky="Wnse")

        if LM.language_dict['justify'] == 'right':
            self.EntryPack_frame.grid_columnconfigure(0, weight=1)
            self.EntryPack_frame.grid(row=0, column=0, padx=10, pady=10, sticky="Ensw")
        else:   self.EntryPack_frame.grid_columnconfigure(1, weight=1)

    def __add_customer_button_func(self):
        if self.EntryPack_frame.GetProfileDict()['first name'] and \
                self.EntryPack_frame.GetProfileDict()['last name'] is not None:
            if self.command_add_customer_button(Case=self.title_case + 'add_customer',
                                                windows_master=self.windows_master,
                                                Profile=self.EntryPack_frame.GetProfileDict()) is False:
                mb.showinfo(LM.language_dict['Note'],
                            LM.linebreak_string(LM.language_dict['Message 7'], char_linebreak=True))
        else:
            mb.showinfo(LM.language_dict['Note'],
                        LM.linebreak_string(LM.language_dict['Message 8'], char_linebreak=True))

    def __KP_Enter(self, evt):
        if evt.keysym == "Return":
            self.__add_customer_button_func()


class AppCustomerSearch(AppWindow):

    def __init__(self,
                 customers_list: list,
                 command_case: Any,
                 title_case: str,
                 geometry_manager=True,
                 *args, **kwargs):
        super().__init__(geometry_manager=False, *args, **kwargs)
        self.customers_list = customers_list
        self.command_case = command_case
        self.title_case = title_case

        self.customer_search_entry = customtkinter.CTkEntry(master=self.window_frame,
                                                            corner_radius=6,
                                                            font=Fonts.WindowLoginEntry,
                                                            fg_color=Colors.Entries[0],
                                                            border_color=Colors.Entries[1])
        self.list_results = Boxs.ListBoxPack(master=self.window_frame)
        self.customer_search_button = Buttons.WindowCustomerManagerButtons(master=self.window_frame,
                                                                           color=Colors.SignInWindowFrame_sign_in_button,
                                                                           font=Fonts.AppWindowButton,
                                                                           command=self.__customer_search_button_func)

        self.customer_search_entry.bind("<KeyRelease>", self.__check_customer_search_entry)
        self.list_results.update_list(self.customers_list)
        self.list_results.bind("<<ListboxSelect>>", self.listbox_select)
        self.windows_master.DisplayAppWindowsFrame(self.app_window_frame)
        self.windows_master.DisplayAppMenuFrame(self.app_menu_frame)

        if geometry_manager:
            self.GeometryAndLanguageManager()

    def GeometryAndLanguageManager(self):
        super().GeometryAndLanguageManager()
        self.title_label.configure(text=LM.language_dict['Customer search'])
        self.customer_search_entry.configure(placeholder_text=LM.language_dict["the customer's name"])
        self.customer_search_button.configure(text=LM.language_dict['Search'])
        self.list_results.configure(justify=LM.language_dict['justify'])
        self.customer_search_entry.configure(justify=LM.language_dict['justify'])

        self.window_frame.grid_rowconfigure(0, weight=0)
        self.window_frame.grid_rowconfigure(1, weight=1)
        self.window_frame.grid_columnconfigure(0, weight=0)
        self.window_frame.grid_columnconfigure(1, weight=1)

        self.customer_search_entry.grid(row=0, column=0, columnspan=2, sticky="nswe", padx=10, pady=28)

        self.list_results.grid(row=1, column=1, sticky="nswe", pady=2)
        self.list_results.scroll.grid(row=1, column=0, sticky="nswe", padx=8, pady=2)

        self.customer_search_button.grid(row=2, column=0, columnspan=2, pady=14, sticky='S')

        if LM.language_dict['justify'] == 'right':
            self.window_frame.grid_columnconfigure(0, weight=1)
            self.window_frame.grid_columnconfigure(1, weight=0)

            self.list_results.grid(row=1, column=0, sticky="nswe", pady=2)
            self.list_results.scroll.grid(row=1, column=1, sticky="nswe", padx=8, pady=2)

    def __check_customer_search_entry(self, evt):
        if self.customer_search_entry.get() == "":
            self.list_results.update_list(self.customers_list)
        else:
            self.list_results.update_list(
                [name for name in self.customers_list if name.startswith(self.customer_search_entry.get())])

        if evt.keysym == "Return":
            self.__customer_search_button_func()

    def listbox_select(self, evt):
        if self.list_results.get(tkinter.ANCHOR) != '':
            self.command_case(Case=self.title_case + 'results_search',
                              windows_master=self.windows_master,
                              results_search=self.list_results.get(tkinter.ANCHOR))

    def __customer_search_button_func(self):
        if self.customer_search_entry.get() != '':
            self.list_results.update_list(
                [name for name in self.customers_list if self.customer_search_entry.get() in name])


class AppCustomer(AppWindow):

    def __init__(self,
                 customer_name: str,
                 command_case: Any,
                 title_case: str,
                 geometry_manager=True, *args, **kwargs):
        super().__init__(geometry_manager=False, *args, **kwargs)
        self.command_case = command_case
        self.title_case = title_case
        self.customer_name = customer_name

        self.app_menu_frame = customtkinter.CTkFrame(master=self.windows_master.menu_frame)
        self.customer_menu_frame = customtkinter.CTkFrame(master=self.app_menu_frame, fg_color=Colors.CustomerMenuFrame)

        self.customer_name_label = customtkinter.CTkLabel(master=self.customer_menu_frame, text=self.customer_name)
        self.customer_profile_button = Buttons.WindowCustomerManagerButtons(master=self.customer_menu_frame,
                                                                            font=Fonts.AppWindowButton,
                                                                            command=self.__customer_profile_button_func)
        self.adding_new_order_button = Buttons.WindowCustomerManagerButtons(master=self.customer_menu_frame,
                                                                            font=Fonts.AppWindowButton,
                                                                            command=self.__adding_new_order_button_func)
        self.order_search_button = Buttons.WindowCustomerManagerButtons(master=self.customer_menu_frame,
                                                                        font=Fonts.AppWindowButton,
                                                                        command=self.__order_search_button_func)
        self.order_report_button = Buttons.WindowCustomerManagerButtons(master=self.customer_menu_frame,
                                                                        font=Fonts.AppWindowButton,
                                                                        command=self.__order_report_button_func)

        self.windows_master.DisplayAppWindowsFrame(self.app_window_frame)
        self.windows_master.DisplayAppMenuFrame(self.app_menu_frame)

        if geometry_manager:
            self.GeometryAndLanguageManager()

    def GeometryAndLanguageManager(self):
        super().GeometryAndLanguageManager()
        self.customer_menu_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.customer_profile_button.configure(text=LM.language_dict['Profile'])
        self.adding_new_order_button.configure(text=LM.language_dict['Adding a new order'])
        self.order_search_button.configure(text=LM.language_dict['Order search'])
        self.order_report_button.configure(text=LM.language_dict['Order report'])

        self.customer_name_label.grid(row=0, padx=8)
        self.customer_profile_button.grid(row=1, padx=8, pady=4)
        self.adding_new_order_button.grid(row=2, padx=8, pady=4)
        self.order_search_button.grid(row=3, padx=8, pady=4)
        self.order_report_button.grid(row=4, padx=8, pady=4)

    def __customer_profile_button_func(self):
        self.command_case(Case=self.title_case + 'customer_profile',
                          windows_master=self.windows_master, )

    def __adding_new_order_button_func(self):
        self.command_case(Case=self.title_case + 'adding_new_order',
                          windows_master=self.windows_master, )

    def __order_search_button_func(self):
        self.command_case(Case=self.title_case + 'order_search',
                          windows_master=self.windows_master, )

    def __order_report_button_func(self):
        self.command_case(Case=self.title_case + 'order_report',
                          windows_master=self.windows_master, )


class AppCustomerProfile(AppWindow):

    def __init__(self,
                 profile: dict,
                 command_case: Any,
                 title_case: str,
                 geometry_manager=True, *args, **kwargs):
        super().__init__(geometry_manager=False, *args, **kwargs)

        self.profile_dict = profile
        self.command_case = command_case
        self.title_case = title_case

        label_data_tuple = (('First name', "first name"),
                            ("Last name", "last name"),
                            ("Parents name", 'parent name'),
                            ('Phone number', "phone"),
                            ('City', 'City'),
                            ('Street', 'Street'),
                            ('Building number', 'Building number'),
                            ('Apartment', 'Apartment'),
                            ('ZIP code', 'ZIP code'),
                            ("Email", "Email"),
                            ("Referred by", 'referred by'),
                            ("Reason for referral", 'reason for referral'))

        self.details_frame = customtkinter.CTkScrollableFrame(master=self.window_frame, fg_color=Colors.AppWindowsFrame)
        self.details_LabelPack = [Pack.LabelPack(master=self.details_frame, title_key=i[0], add_end_title_text=': ',
                                                 data_text=self.profile_dict[i[1]]) for i in label_data_tuple]
        self.edit_profile_button = Buttons.WindowCustomerManagerButtons(master=self.window_frame,
                                                                        color=Colors.SignInWindowFrame_sign_in_button,
                                                                        font=Fonts.AppWindowButton,
                                                                        command=self.__edit_profile_button_func)

        self.windows_master.DisplayAppWindowsFrame(self.app_window_frame)
        if geometry_manager:
            self.GeometryAndLanguageManager()

    def GeometryAndLanguageManager(self):
        super().GeometryAndLanguageManager()
        self.window_frame.grid_rowconfigure(0, weight=1)
        self.window_frame.grid_columnconfigure(0, weight=1)
        self.title_label.configure(text=LM.language_dict['Customer profile'])
        self.edit_profile_button.configure(text=LM.language_dict['Edit Profile'])
        self.edit_profile_button.grid(row=8, column=0, pady=16)

        self.details_frame.grid(row=0, column=0, padx=14, pady=1, sticky="Wens")
        title_column = 0
        title_sticky = "E"
        data_column = 1
        data_sticky = "W"

        if LM.language_dict['justify'] == 'right':
            self.details_frame.grid(row=0, column=0, padx=10, pady=10, sticky="Ewns")
            self.details_frame.grid_columnconfigure(0, weight=1)
            title_column = 1
            title_sticky = 'E'
            data_column = 0
            data_sticky = 'E'

        i = 0
        for label_pack in self.details_LabelPack:
            label_pack.GeometryAndLanguageManager()
            label_pack.title.grid(row=i, column=title_column, sticky=title_sticky, padx=10, pady=5)
            label_pack.data.grid(row=i, column=data_column, sticky=data_sticky, padx=10, pady=5)
            i += 1

    def __edit_profile_button_func(self):
        self.command_case(Case=self.title_case + 'edit_profile',
                          windows_master=self.windows_master, )


class AppSetting(AppWindow):
    def __init__(self,
                 command_case: Any,
                 title_case: str,
                 geometry_manager=True,
                 *args, **kwargs):
        super().__init__(geometry_manager=False, *args, **kwargs)

        self.command_back_button = command_case
        self.title_case = title_case

        self.setting_frame = SettingFrames(master=self.window_frame, geometry_manager=False,
                                           command_back_button=self.__command_back_button)
        self.windows_master.DisplayAppWindowsFrame(self.app_window_frame)
        if geometry_manager:
            self.GeometryAndLanguageManager()

    def GeometryAndLanguageManager(self):
        super().GeometryAndLanguageManager()
        self.setting_frame.GeometryAndLanguageManager()
        self.window_frame.grid_rowconfigure(0, weight=1)
        self.window_frame.grid_columnconfigure(0, weight=1)
        self.title_label.configure(text=LM.language_dict['Setting'])
        self.setting_frame.grid(row=0, column=0, sticky="NSWE", padx=20, pady=10)

    def __command_back_button(self):
        print(f'case = {self.title_case + "back"}')
        self.command_back_button(Case=self.title_case + 'back', windows_master=self.windows_master)


class AppCustomerEditProfile(AppWindow):

    def __init__(self,
                 old_profile: dict,
                 command_case: Any,
                 title_case: str,
                 geometry_manager=True,
                 *args, **kwargs):
        super().__init__(geometry_manager=False, *args, **kwargs)

        self.command_case = command_case
        self.title_case = title_case
        self.old_profile = old_profile
        self.EntryPack_frame = ProfileEntryPack(master=self.window_frame, profile_dict=self.old_profile)
        for k in self.EntryPack_frame.dict_EntryPack.keys():
            self.EntryPack_frame.dict_EntryPack[k].entry.bind('<Key>', self.__KP_Enter)
        self.update_profile_button = Buttons.WindowCustomerManagerButtons(master=self.window_frame,
                                                                          color=Colors.SignInWindowFrame_sign_in_button,
                                                                          font=Fonts.AppWindowButton,
                                                                          command=self.__update_profile_button_func)
        self.back_button = Buttons.WindowCustomerManagerButtons(master=self.window_frame,
                                                                color=Colors.SignUpWindow_back_button,
                                                                font=Fonts.AppWindowButton,
                                                                command=self.__back_button_func)
        self.windows_master.DisplayAppWindowsFrame(self.app_window_frame)

        if geometry_manager:
            self.GeometryAndLanguageManager()

    def GeometryAndLanguageManager(self):
        super().GeometryAndLanguageManager()
        self.EntryPack_frame.GeometryAndLanguageManager()
        self.window_frame.grid_rowconfigure(0, weight=1)
        self.window_frame.grid_columnconfigure(0, weight=1)
        self.window_frame.grid_columnconfigure(1, weight=1)
        self.title_label.configure(text=LM.language_dict['Customer profile'])
        self.update_profile_button.configure(text=LM.language_dict['Update'])
        self.update_profile_button.grid(row=1, column=0, pady=16, sticky="S")
        self.back_button.configure(text=LM.language_dict['Back'])
        self.back_button.grid(row=1, column=1, pady=16, sticky="S")
        i = 0
        for k in self.EntryPack_frame.dict_EntryPack.keys():
            self.EntryPack_frame.dict_EntryPack[k].text.grid(row=i, column=0, sticky="E", padx=10)
            self.EntryPack_frame.dict_EntryPack[k].entry.grid(row=i, column=1, sticky="W", padx=10)
            if LM.language_dict['justify'] == 'right':
                self.EntryPack_frame.dict_EntryPack[k].text.grid(row=i, column=1, sticky="E", padx=10)
                self.EntryPack_frame.dict_EntryPack[k].entry.grid(row=i, column=0, sticky="E", padx=10)
            i += 1

        self.EntryPack_frame.grid(row=0, column=0, padx=14, pady=10, sticky="Wnse", columnspan=2)
        if LM.language_dict['justify'] == 'right':
            self.EntryPack_frame.grid_columnconfigure(0, weight=1)
            self.EntryPack_frame.grid(row=0, column=0, padx=10, pady=10, sticky="Ewns", columnspan=2)
        else:   self.EntryPack_frame.grid_columnconfigure(1, weight=1)

    def __update_profile_button_func(self):
        if self.EntryPack_frame.GetProfileDict()['first name'] and \
                self.EntryPack_frame.GetProfileDict()['last name'] is not None:
            if self.command_case(Case=self.title_case + 'update_profile',
                                 windows_master=self.windows_master,
                                 Profile=self.EntryPack_frame.GetProfileDict()) is False:
                mb.showinfo(LM.language_dict['Note'],
                            LM.linebreak_string(LM.language_dict['Message 7'], char_linebreak=True))
        else:
            mb.showinfo(LM.language_dict['Note'],
                        LM.linebreak_string(LM.language_dict['Message 8'], char_linebreak=True))

    def __back_button_func(self):
        self.command_case(Case=self.title_case + 'update_profile_back',
                          windows_master=self.windows_master)

    def __KP_Enter(self, evt):
        if evt.keysym == "Return":
            self.__update_profile_button_func()