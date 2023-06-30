import customtkinter
from PIL import Image


class RegionShapeFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        #======================================================================#
        #                                Images                                #
        #======================================================================#
        self.plus_image = customtkinter.CTkImage(
            light_image=Image.open("icones/plus_light.png"),
            dark_image=Image.open("icones/plus_dark.png"),
            size=(20, 20)
        )
        self.minus_image = customtkinter.CTkImage(
            light_image=Image.open("icones/minus_light.png"),
            dark_image=Image.open("icones/minus_dark.png"),
            size=(20, 20)
        )
        self.rectangle_image = customtkinter.CTkImage(
            light_image=Image.open("icones/rectangle_light.png"),
            dark_image=Image.open("icones/rectangle_dark.png"),
            size=(20, 20)
        )
        self.polygon_image = customtkinter.CTkImage(
            light_image=Image.open("icones/polygon_light.png"),
            dark_image=Image.open("icones/polygon_dark.png"),
            size=(20, 20)
        )
        self.rectangle_red_image = customtkinter.CTkImage(
            Image.open("icones/rectangle_red.png"),
            size=(20, 20)
        )
        self.polygon_red_image = customtkinter.CTkImage(
            Image.open("icones/polygon_red.png"),
            size=(20, 20)
        )
        #======================================================================#
        #                                Frames                                #
        #======================================================================#
        self.region_shape_name_frame = customtkinter.CTkFrame(self, width=200)
        self.region_shape_name_frame.grid_columnconfigure(0, weight=1)
        self.region_shape_name_frame.grid(row=0, column=0, padx=10, pady=(10,5), sticky="nsew")

        self.region_shape_main_frame = customtkinter.CTkFrame(self)
        self.region_shape_main_frame.grid_columnconfigure((0,1), weight=1)

        self.region_shape_label = customtkinter.CTkLabel(self.region_shape_name_frame, text='Region Shape')
        self.region_shape_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")

        self.region_shape_button = customtkinter.CTkButton(self.region_shape_name_frame, width=30, fg_color='transparent', text='', image=self.plus_image, command=self.region_shape_button_event)
        self.region_shape_button.grid(row=0, column=1, padx=10, pady=10, sticky="nse")

        self.rectangle_button = customtkinter.CTkButton(self.region_shape_main_frame, width=30, fg_color='transparent', text='', image=self.rectangle_image, command=self.rectangle_button_event)
        self.rectangle_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.polygon_button = customtkinter.CTkButton(self.region_shape_main_frame, width=30, fg_color='transparent', text='', image=self.polygon_image, command=self.polygon_button_event)
        self.polygon_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.region_shape_check = False
        self.region_forme_check = False

    def region_shape_button_event(self):
        if self.region_shape_check:
            self.region_shape_button.configure(image=self.plus_image)
            self.configure(height=30)
            self.region_shape_main_frame.grid_forget()
        else:
            self.region_shape_button.configure(image=self.minus_image)
            self.configure(height=60)
            self.region_shape_main_frame.grid(row=1, column=0, padx=10, pady=(5,10), sticky="nsew")
        self.region_shape_check = not self.region_shape_check

    def update_button_image(self, button_name):
        button_image_mapping = {
            self.rectangle_button: (self.rectangle_image,self.rectangle_red_image),
            self.polygon_button: (self.polygon_image,self.polygon_red_image)
        }

        for button, image in button_image_mapping.items():
            if button != button_name:
                button.configure(image=image[0])
            else:
                button.configure(image=image[1])

    def rectangle_button_event(self):
        if self.region_forme_check:
            self.update_button_image(None)
            self.master.master.master.master.main_frame.unbind_all()
        else:
            self.update_button_image(self.rectangle_button)
            self.master.master.master.master.main_frame.create_rectangle_with_mouse()
        self.region_forme_check = not self.region_forme_check

    def polygon_button_event(self):
        if self.region_forme_check:
            self.update_button_image(None)
            self.master.master.master.master.main_frame.unbind_all()
        else:
            self.update_button_image(self.polygon_button)
            self.master.master.master.master.main_frame.create_polygon_with_mouse()
        self.region_forme_check = not self.region_forme_check