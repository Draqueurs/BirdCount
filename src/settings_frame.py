import customtkinter
from PIL import Image


class SettingsFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.plus_image = customtkinter.CTkImage(light_image=Image.open("icons/plus_light.png"),
                                                 dark_image=Image.open("icons/plus_dark.png"),
                                                 size=(20, 20))
        self.minus_image = customtkinter.CTkImage(light_image=Image.open("icons/minus_light.png"),
                                                  dark_image=Image.open("icons/minus_dark.png"),
                                                  size=(20, 20))

        self.settings_name_frame = customtkinter.CTkFrame(self, width=210)
        self.settings_name_frame.grid_columnconfigure(0, weight=1)
        self.settings_name_frame.grid(row=0, column=0, padx=10, pady=(10,5), sticky="nsew")

        self.settings_main_frame = customtkinter.CTkFrame(self)
        self.settings_main_frame.grid_columnconfigure(0, weight=1)
        self.settings_main_frame.grid_columnconfigure(1, weight=1)
        self.settings_main_frame.grid_columnconfigure(2, weight=1)

        self.settings_label = customtkinter.CTkLabel(self.settings_name_frame, text='settings')
        self.settings_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")

        self.settings_check = False

        self.settings_button = customtkinter.CTkButton(self.settings_name_frame, width=30, fg_color='transparent', text='', image=self.plus_image, command=self.settings_button_event)
        self.settings_button.grid(row=0, column=1, padx=10, pady=10, sticky="nse")

        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(self.settings_main_frame, values=["system", "dark", "light"], command=self.appearance_mode_optionmenu_event)
        self.appearance_mode_optionmenu.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

    def settings_button_event(self):
        if self.settings_check:
            self.settings_button.configure(image=self.plus_image)
            self.configure(height=30)
            self.settings_main_frame.grid_forget()
        else:
            self.settings_button.configure(image=self.minus_image)
            self.configure(height=60)
            self.settings_main_frame.grid(row=1, column=0, padx=10, pady=(5,10), sticky="nsew")
        self.settings_check = not self.settings_check
                                                                      
    def appearance_mode_optionmenu_event(self, value):
        customtkinter.set_appearance_mode(value)