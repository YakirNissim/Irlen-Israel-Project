import os
import tkinter
import customtkinter
from PIL import Image
from tkinter import END
from Modules.GUI.LanguageManager import LanguageManager as LM
from Modules.GUI import Test
from typing import Any, Tuple
import calendar
from tkinter import messagebox as mb

customtkinter.set_appearance_mode("Dark")
# customtkinter.set_appearance_mode("Light")


class Constants:
    APP_NAME = "Shulamit"

    # App Window frame constants:
    APP_WINDOW_FRAME_WIDTH = 900
    APP_WINDOW_FRAME_HEIGHT = 600

    # Secondary Window frame constants:
    SECONDARY_WINDOW_FRAME_WIDTH = 310
    SECONDARY_WINDOW_FRAME_HEIGHT = 350

    SECONDARY_WIDGETS_FRAME_WIDTH = 300
    SECONDARY_WIDGETS_FRAME_HEIGHT = 229


class Images:
    icon_app = r'Modules\GUI\images\icon4.ico'

    @staticmethod
    def setting_icon():
        return customtkinter.CTkImage(light_image=Image.open(r'Modules\GUI\images\setting gray.png'),
                                      dark_image=Image.open(r'Modules\GUI\images\setting blue.png'))

    @staticmethod
    def logo_image():
        return customtkinter.CTkImage(light_image=Image.open(r'Modules\GUI\images\logo irlen israel.png'),
                                      dark_image=Image.open(r'Modules\GUI\images\logo irlen israel.png'))

    eye_button_off_image = customtkinter.CTkImage(light_image=Image.open(r'Modules\GUI\images\Blue Eye.png'),
                                                  dark_image=Image.open(r'Modules\GUI\images\Blue Eye.png'),
                                                  size=(30, 19))
    eye_button_on_image = customtkinter.CTkImage(light_image=Image.open(r'Modules\GUI\images\White Eye.png'),
                                                 dark_image=Image.open(r'Modules\GUI\images\White Eye.png'),
                                                 size=(30, 19))

    sign_out_button_image = customtkinter.CTkImage(light_image=Image.open(r'Modules\GUI\images\logout3.png'),
                                                   dark_image=Image.open(r'Modules\GUI\images\logout3.png'),
                                                   size=(25, 25))


class Colors:
    # fg_color = (light_color, dark_color)
    # customtkinter.set_appearance_mode("Dark", "Light" or "System" (only macOS))
    test_color1 = ("green", "green")
    test_color2 = ("red", "red")
    test_color3 = ("blue", 'blue')
    test_purple = ('purple', 'purple')
    eye_button_color = ("gray17", "gray17")

    # MainWindowFrame:
    MainWindowFrame_background = ("gray100", "gray12")
    MainWindowFrame_logo_background = ("gray70", "gray55")
    MainWindowFrame_app_background = ("gray70", "gray16")

    # LogIn window Frame
    SecondaryWindowFrame_background = ("gray70", "gray16")
    SecondaryWindowFrame_logo_background = ("gray70", "gray100")

    # SignIn Frame
    SignInWindowFrame_sign_in_button = (None, None)
    SignInWindow_add_user_button = ("gray60", "gray0")
    WindowLoginEntry = "gray23"
    WindowLoginEntryBorder = "gray30"

    # SignUp Frame
    SignUpWindow_add_user_button = SignInWindowFrame_sign_in_button
    SignUpWindow_back_button = SignInWindow_add_user_button

    # App:
    ListResults_background = 'gray25'
    ListResults_text = 'white'
    ScrollListResults = (
        ('white', 'gray41'), ('white', 'gray53'))  # (button_color, button_hover_color) = (light_color, dark_color)
    Entries = (
        ('white', 'gray24'), ('white', 'gray32'))  # (button_color, button_hover_color) = (fg_color, border_color)
    EntryDatePack_LabelBackslash = ("gray0", "gray60")
    EntryDatePack_border = ('white', 'gray32')

    # Customers Manager Frame
    AppWindowsFrame = ('white', "gray25")
    EditSecurityDataButton = (("gray84", "gray25"), None)
    CustomerManagerFrame_sign_out = (("gray25", "#C77C78"), "#D35B58")  # ((fg_color, hover_color), border_color)
    CustomerManagerFrame_title_control_label = ('white', "gray38")  # fg_color = (light_color, dark_color)

    # Customer Frame
    CustomerMenuFrame = ("white", "gray40")


class Fonts:
    EntryDatePackLabelBackslash = ('Arial', 28)
    ListBoxPack = ("Arial", 15)
    AppWindowButton = ("Arial", 15)
    WindowLoginEntry = ("bold Arial", 16)
    AppWindowsTitle = ("Arial BOLD", 32)


    @staticmethod
    def WindowLoginLabel():
        return "bold Arial" + LM.get_language_dictionary()['justify'], 16


class Buttons:
    @staticmethod
    def SettingButton(master, command, fg_color):
        setting_icon = Images.setting_icon()
        setting_icon.configure(size=(25, 25))
        return customtkinter.CTkButton(master=master,
                                       command=command,
                                       fg_color=fg_color,
                                       text='',
                                       image=setting_icon,
                                       width=0,
                                       height=0,
                                       border_width=0,
                                       hover=False,
                                       )

    @staticmethod
    def EntryButtonShow(master, entry, fg_color, on_image, off_image, show='*'):
        return Entries.EntryButtonShowObject(master, entry, fg_color, on_image, off_image, show)

    @staticmethod
    def WindowSignInButtons(master, text='', command=None, color=(None, None), font=("right", 20)):
        # color=(fg_color, hover_color)
        return customtkinter.CTkButton(master=master,
                                       text=text,
                                       font=font,
                                       corner_radius=6,
                                       command=command,
                                       fg_color=color[0],
                                       hover_color=color[1],
                                       width=200,
                                       height=30)

    @staticmethod
    def WindowSignUpButtons(master, text='', command=None, color=(None, None), font=("right", 20)):
        # color=(fg_color, hover_color)
        return customtkinter.CTkButton(master=master,
                                       text=text,
                                       font=font,
                                       corner_radius=6,
                                       command=command,
                                       fg_color=color[0],
                                       hover_color=color[1],
                                       width=90,
                                       height=30)

    class WindowCustomerManagerButtons(customtkinter.CTkButton):
        def __init__(self, text='', color=(None, None), border_color='white', width=180, height=30, corner_radius=8,
                     border_width=1, font=Fonts.AppWindowButton, *args, **kwargs):
            super().__init__(*args, **kwargs, corner_radius=corner_radius, text=text, font=font,
                             border_color=border_color, width=width, height=height, border_width=border_width,
                             fg_color=color[0], hover_color=color[1])


class Boxs:
    class ListBoxPack(tkinter.Listbox):
        def __init__(self, highlightthickness=0, bd=0, bg=Colors.ListResults_background,
                     fg=Colors.ListResults_text, font=Fonts.ListBoxPack, *args, **kwargs):
            super().__init__(*args, **kwargs, highlightthickness=highlightthickness, bd=bd, bg=bg, selectbackground=bg,
                             fg=fg, font=font)
            self.scroll = customtkinter.CTkScrollbar(master=kwargs['master'], command=self.yview)
            self.configure(yscrollcommand=self.scroll.set)
            self.bind('<Configure>', self.__scroll_show)

        def update_list(self, new_list):
            self.delete(0, END)
            for item in new_list:
                self.insert(END, item)
            self.__scroll_show()

        def __scroll_show(self, evt=None):
            if self.yview()[1] < 1:
                self.scroll.configure(button_color=(Colors.ScrollListResults[0]),
                                      button_hover_color=(Colors.ScrollListResults[1]))
            else:
                self.scroll.configure(button_color=Colors.ListResults_background,
                                      button_hover_color=Colors.ListResults_background)


class Entries:
    @staticmethod
    def WindowLoginEntry(master, text='', justify="right", show=None):
        return customtkinter.CTkEntry(master=master,
                                      corner_radius=6,
                                      width=200,
                                      height=33,
                                      border_color=Colors.WindowLoginEntryBorder,
                                      fg_color=Colors.WindowLoginEntry,
                                      font=Fonts.WindowLoginEntry,
                                      justify=justify,
                                      placeholder_text=text,
                                      show=show)

    class EntryPack:
        def __init__(self, master,
                     text_key=None,
                     add_start_text='',
                     add_end_text='',
                     entry_text_key=None,
                     add_start_entry_text='',
                     add_end_entry_text='',
                     insert=''):

            self.text_key = text_key
            self.text_concat = False
            self.entry_text_concat = False
            if len(add_start_text + add_end_text) > 0:
                self.text_concat = True
                self.s_text = add_start_text
                self.e_text = add_end_text
            self.entry_text_key = entry_text_key
            if len(add_start_entry_text + add_end_entry_text) > 0:
                self.entry_text_concat = True
                self.s_entry_text = add_start_entry_text
                self.e_entry_text = add_end_entry_text
            self.text = customtkinter.CTkLabel(master=master,
                                               font=Fonts.WindowLoginEntry,
                                               text='',
                                               height=35,
                                               width=20)
            self.entry = customtkinter.CTkEntry(master=master,
                                                placeholder_text='',
                                                corner_radius=6,
                                                width=200,
                                                font=Fonts.WindowLoginEntry,
                                                fg_color=Colors.Entries[0],
                                                border_color=Colors.Entries[1])
            if insert is not None:
                self.entry.insert(0, insert)
            self.GeometryAndLanguageManager()

        def GeometryAndLanguageManager(self):
            if self.text_key is not None:
                text = LM.language_dict[self.text_key]
                if self.text_concat:
                    text = LM.str_concat_fix(key=self.text_key, str_s=self.s_text, str_e=self.e_text)
                self.text.configure(text=text)

            if self.entry_text_key is not None:
                text = LM.language_dict[self.entry_text_key]
                if self.entry_text_concat:
                    text = LM.str_concat_fix(key=self.entry_text_key, str_s=self.s_entry_text, str_e=self.e_entry_text)
                self.entry.configure(placeholder_text=text)
                self.entry.configure(justify=LM.language_dict['justify'])

    class EntryButtonShowObject:
        def __init__(self, master, entry, fg_color, on_image, off_image, show):
            self.status = False
            self.entry = entry
            self.on_image = on_image
            self.off_image = off_image
            self.fg_color = fg_color
            self.show = show
            self.entry.configure(show=self.show)
            self.show_button = customtkinter.CTkButton(master=master,
                                                       text='',
                                                       image=self.off_image,
                                                       width=0,
                                                       height=0,
                                                       border_width=0,
                                                       fg_color=self.fg_color,
                                                       hover=False,
                                                       command=self.__clicked)

        def __clicked(self):
            if not self.status:
                self.entry.configure(show='')
                self.show_button.configure(image=self.on_image)
            else:
                self.entry.configure(show=self.show)
                self.show_button.configure(image=self.off_image)
            self.status = not self.status

    class EntryDate(customtkinter.CTkEntry):
        def __init__(self,
                     master: Any,
                     placeholder_text: str = 'DD / MM / YY',
                     *args, **kwargs):
            super().__init__(master=master, placeholder_text=placeholder_text, *args, **kwargs)
            self.__super_get = super().get
            self.__super_delete = super().delete
            self.__super_insert = super().insert
            self.letter_input = False
            self.temp = ""
            self.bind("<KeyRelease>", self.__check_entry)

        def get(self):
            date_int_list = []
            for i in self.__super_get().split(' / '):
                if not i.isdigit() or len(i) != 2:
                    return False
                date_int_list += [int(i)]
            if date_int_list[1] > 12 or (calendar.monthrange(2000 + date_int_list[2], date_int_list[1])[1]) < date_int_list[0]:
                return False
            return tuple(date_int_list)

        def delete(self, first_index, last_index=None):
            self.__super_delete(0, END)
            self.__super_insert(0, self.temp)
            self.__super_delete(first_index, last_index)
            self.temp = self.__super_get()
            self.__insert_fix()

            if not self._is_focused and self._entry.get() == "":
                self._activate_placeholder()

        def insert(self, index, string=None, date=None):
            if date is not None and type(date) == tuple and len(date) == 3:
                string = ''
                for i in date:
                    if type(i) == int and i < 100:
                        string += str(i)
                    else:   raise TypeError('The format of a "date" is (DD, MM, YY) where DD, MM, YY is an integer!')
                if date[1] > 12 or (calendar.monthrange(2000 + date[2], date[1])[1]) < date[0]:
                    raise ValueError('The "date" is invalid!')
                self.temp = string
                return self.__insert_fix()
            if string is not None:
                if type(string) != str:   raise TypeError('The type "string" likes to be "str".'
                                                          '\nThe format of a "string" is "DDMMYY"')
                if string.isdigit():
                    self.__super_delete(0, END)
                    self.__super_insert(0, self.temp)
                    self.__super_insert(index, string)
                    self.temp = self.__super_get()
                    return self.__insert_fix()
                raise ValueError('The "string" can only contain numbers!')

        def __insert_fix(self):
            if len(self.temp) > 6:  self.temp = self.temp[-6:]
            insert_str = ''
            for i in range(len(self.temp)):
                insert_str += self.temp[i]
                if i % 2 == 1 and i < 5:  insert_str += ' / '
            self.__super_delete(0, END)
            self.__super_insert(0, insert_str)

        def __check_entry(self, evt):
            if evt.char.isdigit():
                self.temp += evt.char
            elif evt.keysym != 'BackSpace':
                self.delete(0, END)
                self.letter_input = True
            else:
                self.temp = self.temp[:-1]
            if len(self.__super_get()) == 2:
                self.__super_insert(END, ' / ')
            if len(self.__super_get()) == 7:
                self.__super_insert(END, ' / ')

            if len(self.__super_get()) > 12 or evt.keysym == 'BackSpace' or self.letter_input:
                self.__insert_fix()
                self.letter_input = False


class Pack:
    class ComboBoxPackFrame(customtkinter.CTkFrame):
        def __init__(self, command: Any, values: list = [], text: str = '', *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fg_color = kwargs['fg_color']
            self.combo_box = customtkinter.CTkComboBox(master=self, values=values, command=command)
            self.label_text = customtkinter.CTkLabel(master=self, text=text)
            self.GeometryAndLanguageManager()

        def GeometryAndLanguageManager(self):
            self.configure(fg_color=self.fg_color, corner_radius=0)
            self.combo_box.configure(fg_color=self.fg_color)
            self.label_text.configure(fg_color=self.fg_color)
            self.combo_box.configure(justify='center')

            self.label_text.grid(row=0, column=0, padx=8)
            self.combo_box.grid(row=0, column=1)

            if LM.language_dict['justify'] == 'right':
                self.label_text.grid(row=0, column=1, padx=8)
                self.combo_box.grid(row=0, column=0)

    class LabelPack:
        def __init__(self, master,
                     title_key=None,
                     add_start_title_text='',
                     add_end_title_text='',
                     data_text=None,
                     add_start_data_text='',
                     add_end_data_text=''):
            self.title = customtkinter.CTkLabel(master=master, font=Fonts.WindowLoginEntry)
            self.data = customtkinter.CTkLabel(master=master, font=Fonts.WindowLoginEntry)

            self.title_key = title_key
            self.title_concat = False
            self.data_concat = False
            if len(add_start_title_text + add_end_title_text) > 0:
                self.title_concat = True
                self.s_title_text = add_start_title_text
                self.e_title_text = add_end_title_text
            self.data_text = data_text
            if self.data_text is None:
                self.data_text = ''
            if len(add_start_data_text + add_end_data_text) > 0:
                self.data_concat = True
                self.s_data_text = add_start_data_text
                self.e_data_text = add_end_data_text

            self.GeometryAndLanguageManager()

        def GeometryAndLanguageManager(self):
            if self.title_key is not None:
                text = LM.language_dict[self.title_key]
                if self.title_concat:
                    text = LM.str_concat_fix(key=self.title_key, str_s=self.s_title_text, str_e=self.e_title_text)
                self.title.configure(text=text)

            if self.data_text is not None:
                text = self.data_text
                if self.data_concat:
                    text = self.s_data_text + self.data_text + self.e_data_text
                self.data.configure(text=text)

class RootWindow(customtkinter.CTk):

    def __init__(self, frame=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(Constants.APP_NAME)
        self.iconbitmap(Images.icon_app)
        self.frame = None
        if frame is not None:
            self.WindowFrame(frame)
        self.protocol("WM_DELETE_WINDOW", self.close)

    def WindowFrame(self, frame, *args, **kwargs):
        if self.frame is not None:
            self.frame.destroy()
        self.frame = frame(master=self, *args, **kwargs)

    def close(self):
        print("close")
        self.quit()

    def geometry_and_display_center_screen(self, window_width: int, window_height: int):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


class Frames:
    class SettingFrame(customtkinter.CTkFrame):
        def __init__(self, fg_color, command_back_button, *args, **kwargs):
            super().__init__(*args, **kwargs, fg_color=fg_color)

            self.language_selection = LM.language_dict['Language']
            self.command_back_button = command_back_button
            self.fg_color = fg_color

            self.language_combo_box_pack_frame = Pack.ComboBoxPackFrame(master=self,
                                                                        text=LM.language_dict['Language.w'] + '  ',
                                                                        values=LM.get_language_options_list(),
                                                                        command=self.language_combo_box_selection,
                                                                        fg_color=self.fg_color)
            self.language_combo_box_pack_frame.combo_box.set(self.language_selection)

            self.OK_button = Buttons.WindowSignUpButtons(self,
                                                         color=Colors.SignUpWindow_add_user_button,
                                                         command=self.OK_button_fonc,
                                                         text=LM.language_dict['OK'],
                                                         font=Fonts.WindowLoginLabel())

            self.back_button = Buttons.WindowSignUpButtons(self,
                                                           color=Colors.SignUpWindow_back_button,
                                                           command=self.command_back_button,
                                                           text=LM.language_dict['Back'],
                                                           font=Fonts.WindowLoginLabel())

            self.GeometryAndLanguageManager()

        def GeometryAndLanguageManager(self):
            pass

        def __repr__(self):
            return "Setting Window"

        # button method
        def language_combo_box_selection(self, value):
            self.language_selection = value

        def OK_button_fonc(self):
            LM.language_dict_updating(new_key=self.language_selection)
            self.command_back_button()

    class SecondaryWindowFrame(customtkinter.CTkFrame):

        def __init__(self, master, *args, **kwargs):
            super().__init__(*args, **kwargs, master=master)

            #  Master window settings:
            master.minsize(Constants.SECONDARY_WINDOW_FRAME_WIDTH, Constants.SECONDARY_WINDOW_FRAME_HEIGHT)
            master.geometry_and_display_center_screen(window_width=Constants.SECONDARY_WINDOW_FRAME_WIDTH,
                                                      window_height=Constants.SECONDARY_WINDOW_FRAME_HEIGHT)

            master.resizable(False, False)
            logo_image = Images.logo_image()
            logo_image.configure(size=(295, 85))

            self.configure(width=Constants.SECONDARY_WINDOW_FRAME_WIDTH,
                           height=Constants.SECONDARY_WINDOW_FRAME_HEIGHT,
                           fg_color=Colors.SecondaryWindowFrame_background,
                           corner_radius=0)
            self.pack()

            self.logo_frame = customtkinter.CTkFrame(master=self,
                                                     width=300,
                                                     height=90,
                                                     fg_color=Colors.SecondaryWindowFrame_logo_background)
            self.logo_frame.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

            self._logo_label = customtkinter.CTkLabel(master=self.logo_frame,
                                                      text='',
                                                      image=logo_image)
            self._logo_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

            self.widgets_frame = customtkinter.CTkFrame(master=self,
                                                        width=Constants.SECONDARY_WIDGETS_FRAME_WIDTH,
                                                        height=Constants.SECONDARY_WIDGETS_FRAME_HEIGHT,
                                                        fg_color=Colors.test_color1)
            self.widgets_frame.place(relx=0.5, rely=0.66, anchor=tkinter.CENTER)

        def DisplayWidgetsFrame(self, widgets_frame):
            self.widgets_frame.destroy()
            self.widgets_frame = widgets_frame
            self.widgets_frame.place(relx=0.5, rely=0.66, anchor=tkinter.CENTER)

    class MainWindowFrame(customtkinter.CTkFrame):

        def __init__(self, geometry_manager=True, *args, **kwargs):
            super().__init__(*args, **kwargs)

            #  Master window settings:
            self.master = kwargs["master"]
            logo_image = Images.logo_image()
            logo_image.configure(size=(166, 90))

            self._logo_frame = customtkinter.CTkFrame(master=self,
                                                      height=105,
                                                      corner_radius=0,
                                                      fg_color=Colors.MainWindowFrame_background)

            self.title_menu_frame = customtkinter.CTkFrame(master=self,
                                                           height=105,
                                                           width=200,
                                                           corner_radius=0,
                                                           fg_color=Colors.MainWindowFrame_app_background)

            self.window_frame = customtkinter.CTkFrame(master=self,
                                                       corner_radius=8,
                                                       fg_color=Colors.MainWindowFrame_app_background)

            self.menu_frame = customtkinter.CTkFrame(master=self,
                                                     width=200,
                                                     corner_radius=0,
                                                     fg_color=Colors.MainWindowFrame_app_background)

            self._logo_label = customtkinter.CTkLabel(master=self._logo_frame,
                                                      text='',
                                                      height=100,
                                                      image=logo_image,
                                                      fg_color=Colors.MainWindowFrame_logo_background,
                                                      corner_radius=8)

            if geometry_manager:
                self.GeometryAndLanguageManager()

        def GeometryAndLanguageManager(self):
            self.master.geometry_and_display_center_screen(window_width=Constants.APP_WINDOW_FRAME_WIDTH,
                                                           window_height=Constants.APP_WINDOW_FRAME_HEIGHT)
            self.master.minsize(Constants.APP_WINDOW_FRAME_WIDTH, Constants.APP_WINDOW_FRAME_HEIGHT)
            """ Which box (column, row) can expand when resizing the window: """
            self.master.grid_rowconfigure(0, weight=1)
            self.master.grid_columnconfigure(0, weight=1)

            # Frame:
            self.configure(fg_color=Colors.MainWindowFrame_background, corner_radius=0)
            self.grid(row=0, column=0, sticky="NSWE")
            """ Which box (column, row) can expand when resizing the window: """
            self.grid_rowconfigure(1, weight=1)
            self.grid_columnconfigure(1, weight=1)
            self.grid_columnconfigure(0, weight=0)

            self._logo_frame.grid(row=0, column=1, sticky="NSWE")
            self._logo_frame.grid_columnconfigure(0, weight=1)
            self.title_menu_frame.grid(row=0, column=0, sticky="NSWE")
            self.window_frame.grid(row=1, column=1, sticky="NSWE", padx=20, pady=20)
            self.menu_frame.grid(row=1, column=0, sticky="NSWE")

            self._logo_label.grid(row=0, column=0, sticky="nswe", padx=5, pady=6)

            if LM.language_dict['justify'] == 'right':
                # Frame:
                self.grid_columnconfigure(1, weight=0)
                self.grid_columnconfigure(0, weight=1)

                self._logo_frame.grid(row=0, column=0, sticky="NSWE")
                self.title_menu_frame.grid(row=0, column=1, sticky="NSWE")
                self.window_frame.grid(row=1, column=0, sticky="NSWE", padx=20, pady=20)
                self.menu_frame.grid(row=1, column=1, sticky="NSWE")

        def DisplayWindowsFrame(self, windows_frame):
            self.window_frame.destroy()
            self.window_frame = windows_frame
            self.window_frame.grid(row=1, column=1, sticky="NSWE", padx=20, pady=20)
            if LM.language_dict['justify'] == 'right':
                self.window_frame.grid(row=1, column=0, sticky="NSWE", padx=20, pady=20)