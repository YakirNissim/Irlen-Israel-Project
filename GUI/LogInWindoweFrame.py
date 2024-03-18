import os
from Modules.GUI.GUIDesign import *
from Modules.GUI.LanguageManager import LanguageManager as LM


class LogInFrame(Frames.SecondaryWindowFrame):

    def __init__(self,
                 command_case: Any,
                 title_case: str,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__login_attempts = 0
        self.command_case = command_case
        self.title_case = title_case
        self.DisplaySignInWidgetsFrame()

    def DisplaySignInWidgetsFrame(self):
        self.DisplayWidgetsFrame(SignInWidgetsFrame(master=self,
                                                    command_add_user_button=self.DisplaySignUpWidgetsFrame,
                                                    command_sign_in_button=self.__SignIn_sign_in_button,
                                                    command_language_definition_button=self.DisplaySettingWidgetsFrame))

    def DisplaySignUpWidgetsFrame(self):
        self.DisplayWidgetsFrame(SignUpWidgetsFrame(master=self,
                                                    command_back_button=self.DisplaySignInWidgetsFrame,
                                                    command_add_user_button=self.__SignUp_add_user_button,
                                                    command_language_definition_button=self.DisplaySettingWidgetsFrame))

    def DisplaySettingWidgetsFrame(self):
        self.DisplayWidgetsFrame(SettingFrame(master=self,
                                              command_back_button=self.DisplaySignInWidgetsFrame))

    def __SignIn_sign_in_button(self):
        username = LM.FixString(self.widgets_frame.username_entry.get())
        self.widgets_frame.username_entry.delete(0, END)
        if username is None:    return
        self.widgets_frame.username_entry.insert(0, username)
        self.__login_attempts += 1
        if not self.command_case(Case=self.title_case + 'sign_in',
                                 Username=username,
                                 Password=self.widgets_frame.password_entry.get()):
            if self.__login_attempts == 1:
                mb.showinfo(LM.language_dict['Note'], LM.language_dict['Message 1'])
            elif self.__login_attempts == 2:
                mb.showwarning(LM.language_dict['Warning'],
                               LM.linebreak_string(LM.language_dict['Message 2'], char_linebreak=True))
            else:
                self.master.quit()

    def __SignUp_add_user_button(self):
        username = LM.FixString(self.widgets_frame.username_entry.get())
        self.widgets_frame.username_entry.delete(0, END)
        if username is None:    return
        self.widgets_frame.username_entry.insert(0, username)
        if self.widgets_frame.security_switch.get():
            answer = mb.askquestion(LM.language_dict['Notice'],
                                    LM.linebreak_string(LM.language_dict['Message 3'], char_linebreak=True))
            if answer == 'yes':
                if not self.command_case(Case=self.title_case + 'sign_up', Username=username, Password=None):
                    self.Username_already_taken_message()

        elif self.widgets_frame.password_entry.get() == '':
            mb.showinfo(LM.language_dict['Note'],
                        LM.linebreak_string(LM.language_dict['Message 4'] +
                                            f"'{LM.language_dict['Create an unsecured account']}'!.",
                                            char_linebreak=True))

        elif self.widgets_frame.password_entry.get() == self.widgets_frame.confirm_password_entry.get():
            if not self.command_case(Case=self.title_case + 'sign_up',
                                     Username=username,
                                     Password=self.widgets_frame.password_entry.get()):
                self.Username_already_taken_message()

        elif self.widgets_frame.password_entry.get() != self.widgets_frame.confirm_password_entry.get():
            mb.showinfo(LM.language_dict['Notice'], LM.language_dict['Message 5'])

    def __Setting_button(self):
        print('setting_button')
        self.DisplayWidgetsFrame(SettingFrame(master=self))

    @staticmethod
    def Username_already_taken_message():
        mb.showinfo(LM.language_dict['Note'],
                    LM.linebreak_string(LM.language_dict['Message 6'], char_linebreak=True))


class SignInWidgetsFrame(customtkinter.CTkFrame):
    # public methods:
    def __init__(self, master, command_sign_in_button, command_add_user_button, command_language_definition_button,
                 *args, **kwargs):
        super().__init__(*args, **kwargs, master=master, width=Constants.SECONDARY_WIDGETS_FRAME_WIDTH,
                         height=Constants.SECONDARY_WIDGETS_FRAME_HEIGHT)

        self.language_dict = LM.get_language_dictionary()

        self.command_sign_in_button = command_sign_in_button
        self.command_add_user_button = command_add_user_button

        self.setting_button = Buttons.SettingButton(master=self, command=command_language_definition_button,
                                                    fg_color=Colors.SecondaryWindowFrame_background)
        self.setting_button.place(relx=0.95, rely=0.92, anchor=tkinter.CENTER)

        self.username_entry = Entries.WindowLoginEntry(master=self,
                                                       text=self.language_dict['Username'],
                                                       justify=self.language_dict['justify'])
        self.username_entry.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

        self.password_entry = Entries.WindowLoginEntry(master=self,
                                                       text=self.language_dict['Password'],
                                                       justify=self.language_dict['justify'])
        self.password_entry.place(relx=0.5, rely=0.43, anchor=tkinter.CENTER)

        self.eye_button = Buttons.EntryButtonShow(master=self,
                                                  entry=self.password_entry,
                                                  fg_color=Colors.SecondaryWindowFrame_background,
                                                  on_image=Images.eye_button_on_image,
                                                  off_image=Images.eye_button_off_image,
                                                  show='*')
        self.eye_button.show_button.place(relx=0.09, rely=0.43, anchor=tkinter.CENTER)

        self.sign_in_button = Buttons.WindowSignInButtons(self,
                                                          color=Colors.SignInWindowFrame_sign_in_button,
                                                          command=self.command_sign_in_button,
                                                          text=self.language_dict['Sign in'],
                                                          font=("Arial" + self.language_dict['justify'], 15))
        self.sign_in_button.place(relx=0.5, rely=0.62, anchor=tkinter.CENTER)

        self.add_user_button = Buttons.WindowSignInButtons(self,
                                                           color=Colors.SignInWindow_add_user_button,
                                                           command=self.command_add_user_button,
                                                           text=self.language_dict['Create New Account'],
                                                           font=("Arial" + self.language_dict['justify'], 15))
        self.add_user_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        if self.language_dict['justify'] == 'right':
            self.eye_button.show_button.place(relx=0.92, rely=0.43, anchor=tkinter.CENTER)

    def __repr__(self):
        return "Login Window"

    # private methods:


class SignUpWidgetsFrame(customtkinter.CTkFrame):
    # public methods:
    def __init__(self, master, command_add_user_button, command_back_button, command_language_definition_button,
                 *args, **kwargs):
        super().__init__(*args, **kwargs, master=master, width=Constants.SECONDARY_WIDGETS_FRAME_WIDTH,
                         height=Constants.SECONDARY_WIDGETS_FRAME_HEIGHT)
        self.language_dict = LM.get_language_dictionary()

        self.command_add_user_button = command_add_user_button
        self.command_back_button = command_back_button

        self.setting_button = Buttons.SettingButton(master=self, command=command_language_definition_button,
                                                    fg_color=Colors.SecondaryWindowFrame_background)
        self.setting_button.place(relx=0.95, rely=0.92, anchor=tkinter.CENTER)

        self.security_switch = customtkinter.CTkSwitch(master=self,
                                                       text=self.language_dict['Create an unsecured account'],
                                                       font=Fonts.WindowLoginLabel(),
                                                       command=self.__security_switch)
        self.security_switch.place(relx=0.49, rely=0.1, anchor=tkinter.CENTER)

        self.username_entry = Entries.WindowLoginEntry(master=self,
                                                       text=self.language_dict['Username'],
                                                       justify=self.language_dict['justify'])
        self.username_entry.place(relx=0.5, rely=0.27, anchor=tkinter.CENTER)

        self.__security()

        self.add_user_button = Buttons.WindowSignUpButtons(self,
                                                           color=Colors.SignUpWindow_add_user_button,
                                                           command=self.command_add_user_button,
                                                           text=self.language_dict['Create account'],
                                                           font=Fonts.WindowLoginLabel())
        self.add_user_button.place(relx=0.68, rely=0.85, anchor=tkinter.CENTER)

        self.back_button = Buttons.WindowSignUpButtons(self,
                                                       color=Colors.SignUpWindow_back_button,
                                                       command=self.command_back_button,
                                                       text=self.language_dict['Back'],
                                                       font=Fonts.WindowLoginLabel())
        self.back_button.place(relx=0.32, rely=0.85, anchor=tkinter.CENTER)

        if self.language_dict['justify'] == 'right':
            self.security_switch.configure(text='')
            self.security_switch.place(relx=0.85, rely=0.11, anchor=tkinter.CENTER)
            self.security_switch_text = customtkinter.CTkLabel(master=self,
                                                               font=Fonts.WindowLoginLabel(),
                                                               text=self.language_dict['Create an unsecured account'])
            self.security_switch_text.place(relx=0.42, rely=0.1, anchor=tkinter.CENTER)

    def __repr__(self):
        return "Sign Up Window"

    # private methods:
    def __security(self):
        self.password_entry = Entries.WindowLoginEntry(master=self,
                                                       text=self.language_dict['Password'],
                                                       justify=self.language_dict['justify'],
                                                       show='*')
        self.password_entry.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

        self.confirm_password_entry = Entries.WindowLoginEntry(master=self,
                                                               text=self.language_dict['Confirm password'],
                                                               justify=self.language_dict['justify'])
        self.confirm_password_entry.place(relx=0.5, rely=0.63, anchor=tkinter.CENTER)

        self.eye_button = Buttons.EntryButtonShow(master=self,
                                                  entry=self.confirm_password_entry,
                                                  fg_color=Colors.SecondaryWindowFrame_background,
                                                  on_image=Images.eye_button_on_image,
                                                  off_image=Images.eye_button_off_image,
                                                  show='*')
        self.eye_button.show_button.place(relx=0.09, rely=0.63, anchor=tkinter.CENTER)

        if self.language_dict['justify'] == 'right':
            self.eye_button.show_button.place(relx=0.92, rely=0.63, anchor=tkinter.CENTER)

    # button method
    def __security_switch(self):
        if self.security_switch.get():
            self.password_entry.destroy()
            self.confirm_password_entry.destroy()
            self.eye_button.show_button.destroy()
        else:
            self.__security()


class SettingFrame(Frames.SettingFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs,
                         width=Constants.SECONDARY_WIDGETS_FRAME_WIDTH,
                         height=Constants.SECONDARY_WIDGETS_FRAME_HEIGHT,
                         fg_color=Colors.SecondaryWindowFrame_background)

    def GeometryAndLanguageManager(self):
        self.language_combo_box_pack_frame.place(relx=0.09, rely=0.1)
        self.OK_button.place(relx=0.68, rely=0.85, anchor=tkinter.CENTER)
        self.back_button.place(relx=0.32, rely=0.85, anchor=tkinter.CENTER)
        if LM.language_dict['justify'] == 'right':
            self.language_combo_box_pack_frame.place(relx=0.3, rely=0.1)
