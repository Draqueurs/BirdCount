import customtkinter
from PIL import Image


class KeyboardShortcutsFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.plus_image = customtkinter.CTkImage(light_image=Image.open("icones/plus_light.png"),
                                                 dark_image=Image.open("icones/plus_dark.png"),
                                                 size=(20, 20))
        self.minus_image = customtkinter.CTkImage(light_image=Image.open("icones/minus_light.png"),
                                                  dark_image=Image.open("icones/minus_dark.png"),
                                                  size=(20, 20))

        self.region_shape_name_frame = customtkinter.CTkFrame(self, width=210)
        self.region_shape_name_frame.grid_columnconfigure(0, weight=1)
        self.region_shape_name_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.region_shape_main_frame = customtkinter.CTkFrame(self)

        self.region_shape_label = customtkinter.CTkLabel(self.region_shape_name_frame, text='Keyboard Shortcuts')
        self.region_shape_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")

        self.region_shape_check = False

        self.region_shape_button = customtkinter.CTkButton(self.region_shape_name_frame, width=30, fg_color='transparent', text='', image=self.plus_image, command=self.region_shape_button_event)
        self.region_shape_button.grid(row=0, column=1, padx=10, pady=10, sticky="nse")

        self.rectangle_button = customtkinter.CTkButton(self.region_shape_main_frame, width=30, fg_color='transparent', text='', image=self.plus_image)
        self.rectangle_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.circle_button = customtkinter.CTkButton(self.region_shape_main_frame, width=30, fg_color='transparent', text='', image=self.plus_image)
        self.circle_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.ellipse_button = customtkinter.CTkButton(self.region_shape_main_frame, width=30, fg_color='transparent', text='', image=self.plus_image)
        self.ellipse_button.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        self.polygon_button = customtkinter.CTkButton(self.region_shape_main_frame, width=30, fg_color='transparent', text='', image=self.plus_image)
        self.polygon_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.point_button = customtkinter.CTkButton(self.region_shape_main_frame, width=30, fg_color='transparent', text='', image=self.plus_image)
        self.point_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.polyline_button = customtkinter.CTkButton(self.region_shape_main_frame, width=30, fg_color='transparent', text='', image=self.plus_image)
        self.polyline_button.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

    def region_shape_button_event(self):
        if self.region_shape_check:
            self.region_shape_button.configure(image=self.plus_image)
            self.configure(height=30)
            self.region_shape_main_frame.grid_forget()
        else:
            self.region_shape_button.configure(image=self.minus_image)
            self.configure(height=60)
            self.region_shape_main_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.region_shape_check = not self.region_shape_check