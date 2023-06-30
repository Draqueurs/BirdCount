import customtkinter
from PIL import Image
from int_spinbox import IntSpinbox
from float_spinbox import FloatSpinbox
import configparser


class AttributesFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.plus_image = customtkinter.CTkImage(light_image=Image.open("icones/plus_light.png"),
                                                 dark_image=Image.open("icones/plus_dark.png"),
                                                 size=(20, 20))
        self.minus_image = customtkinter.CTkImage(light_image=Image.open("icones/minus_light.png"),
                                                  dark_image=Image.open("icones/minus_dark.png"),
                                                  size=(20, 20))

        self.attributes_name_frame = customtkinter.CTkFrame(self, width=210)
        self.attributes_name_frame.grid_columnconfigure(0, weight=1)
        self.attributes_name_frame.grid(row=0, column=0, padx=10, pady=(10,5), sticky="nsew")

        self.attributes_main_frame = customtkinter.CTkFrame(self)
        self.attributes_main_frame.grid_columnconfigure(0, weight=1)
        self.attributes_main_frame.grid_columnconfigure(1, weight=1)

        self.attributes_label = customtkinter.CTkLabel(self.attributes_name_frame, text='Attributes')
        self.attributes_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")

        self.attributes_check = False

        self.attributes_button = customtkinter.CTkButton(self.attributes_name_frame, width=30, fg_color='transparent', text='', image=self.plus_image, command=self.attributes_button_event)
        self.attributes_button.grid(row=0, column=1, padx=10, pady=10, sticky="nse")

        #======================================================================#
        #                              HSV Frame                               #
        #======================================================================#
        self.hsv_frame = customtkinter.CTkFrame(self.attributes_main_frame, fg_color='transparent')
        self.hsv_frame.grid(row=0, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")

        self.hsv_switch = customtkinter.CTkSwitch(self.hsv_frame, text='HSV', command=self.hsv_switch_event)
        self.hsv_switch.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.count_label = customtkinter.CTkLabel(self.hsv_frame, text='Count: ')
        self.count_label.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        #-----------------------------------H-----------------------------------#
        self.min_hue_intspinbox = IntSpinbox(self.hsv_frame, text='Min Hue', min=0, max=255, command=self.hsv_switch_event)
        self.min_hue_intspinbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        self.max_hue_intspinbox = IntSpinbox(self.hsv_frame, text='Max Hue', min=0, max=255, command=self.hsv_switch_event)
        self.max_hue_intspinbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        self.min_hue_intspinbox.set(0)
        self.max_hue_intspinbox.set(255)

        #-----------------------------------H-----------------------------------#
        self.min_saturation_intspinbox = IntSpinbox(self.hsv_frame, text='Min Saturation', min=0, max=255, command=self.hsv_switch_event)
        self.min_saturation_intspinbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        self.max_saturation_intspinbox = IntSpinbox(self.hsv_frame, text='Max Saturation', min=0, max=255, command=self.hsv_switch_event)
        self.max_saturation_intspinbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.min_saturation_intspinbox.set(0)
        self.max_saturation_intspinbox.set(255)

        #-----------------------------------H-----------------------------------#
        self.min_value_intspinbox = IntSpinbox(self.hsv_frame, text='Min Value', min=0, max=255, command=self.hsv_switch_event)
        self.min_value_intspinbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        self.max_value_intspinbox = IntSpinbox(self.hsv_frame, text='Max Value', min=0, max=255, command=self.hsv_switch_event)
        self.max_value_intspinbox.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.min_value_intspinbox.set(0)
        self.max_value_intspinbox.set(255)
        
        #------------------------------Threshold-------------------------------#
        self.min_threshold_intspinbox = IntSpinbox(self.hsv_frame, text='Min Threshold', min=0, max=255, command=self.hsv_switch_event)
        self.min_threshold_intspinbox.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        self.max_threshold_intspinbox = IntSpinbox(self.hsv_frame, text='Max Threshold', min=0, max=255, command=self.hsv_switch_event)
        self.max_threshold_intspinbox.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.min_threshold_intspinbox.set(0)
        self.max_threshold_intspinbox.set(255)

        #---------------------------------Area---------------------------------#
        self.min_area_intspinbox = IntSpinbox(self.hsv_frame, text='Min Area', min=1, max=1000, command=self.hsv_switch_event)
        self.min_area_intspinbox.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        self.max_area_intspinbox = IntSpinbox(self.hsv_frame, text='Max Area', min=1, max=1000, command=self.hsv_switch_event)
        self.max_area_intspinbox.grid(row=10, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
       
        self.min_area_intspinbox.set(1)
        self.max_area_intspinbox.set(100)

        #---------------------------------Blur---------------------------------#
        self.blur_intspinbox = IntSpinbox(self.hsv_frame, text='Blur', step_size=2, min=1, max=1000, command=self.hsv_switch_event)
        self.blur_intspinbox.grid(row=11, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
       
        self.blur_intspinbox.set(1)

        #---------------------------------Erode---------------------------------#
        self.erode_intspinbox = IntSpinbox(self.hsv_frame, text='Erode', min=1, max=1000, command=self.hsv_switch_event)
        self.erode_intspinbox.grid(row=12, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
       
        self.erode_intspinbox.set(1)

        #---------------------------------Dilate---------------------------------#
        self.dilate_intspinbox = IntSpinbox(self.hsv_frame, text='Dilate', min=1, max=1000, command=self.hsv_switch_event)
        self.dilate_intspinbox.grid(row=13, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
       
        self.dilate_intspinbox.set(1)

        #---------------------------------Inverse--------------------------------#
        self.inverse_switch = customtkinter.CTkSwitch(self.hsv_frame, text='Inverse', command=self.hsv_switch_event)
        self.inverse_switch.grid(row=14, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        #---------------------------------Save---------------------------------#
        self.save_button = customtkinter.CTkButton(self.attributes_main_frame, text='Save', command=self.save_buton_event)
        self.save_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        #---------------------------------Load---------------------------------#
        self.load_button = customtkinter.CTkButton(self.attributes_main_frame, text='Load', command=self.load_buton_event)
        self.load_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")


    def hsv_switch_event(self):
        if self.hsv_switch.get():
            self.analyze()

    def analyze(self):
        if self.master.master.master.master.main_frame.image_analyzer is not None:
            image = self.master.master.master.master.main_frame.image_analyzer.analyze(
                min_hue=self.min_hue_intspinbox.get(),
                max_hue=self.max_hue_intspinbox.get(),
                min_saturation=self.min_saturation_intspinbox.get(),
                max_saturation=self.max_saturation_intspinbox.get(),
                min_value=self.min_value_intspinbox.get(),
                max_value=self.max_value_intspinbox.get(),
                min_threshold=self.min_threshold_intspinbox.get(), 
                max_threshold=self.max_threshold_intspinbox.get(),
                min_area=self.min_area_intspinbox.get(), 
                max_area=self.max_area_intspinbox.get(),
                blur=self.blur_intspinbox.get(),
                erode=self.erode_intspinbox.get(),
                dilate=self.dilate_intspinbox.get(),
                inverse=self.inverse_switch.get(),
                save_path=None
            )
        
            self.master.master.master.master.main_frame.update_label()
            self.count_label.configure(text='Count: '+str(self.master.master.master.master.main_frame.image_analyzer.count))


    def attributes_button_event(self):
        if self.attributes_check:
            self.attributes_button.configure(image=self.plus_image)
            self.configure(height=30)
            self.attributes_main_frame.grid_forget()
        else:
            self.attributes_button.configure(image=self.minus_image)
            self.configure(height=60)
            self.attributes_main_frame.grid(row=1, column=0, padx=10, pady=(5,10), sticky="nsew")
        self.attributes_check = not self.attributes_check

    def save_buton_event(self):
        filetypes = [
            ('PNG Image', '*.png'),
            ('All Files', '*.*')
        ]
        file = customtkinter.filedialog.askdirectory()

        if file != '':
            image = self.master.master.master.master.main_frame.image_analyzer.analyze(
                min_hue=self.min_hue_intspinbox.get(),
                max_hue=self.max_hue_intspinbox.get(),
                min_saturation=self.min_saturation_intspinbox.get(),
                max_saturation=self.max_saturation_intspinbox.get(),
                min_value=self.min_value_intspinbox.get(),
                max_value=self.max_value_intspinbox.get(),
                min_threshold=self.min_threshold_intspinbox.get(), 
                max_threshold=self.max_threshold_intspinbox.get(),
                min_area=self.min_area_intspinbox.get(), 
                max_area=self.max_area_intspinbox.get(),
                blur=self.blur_intspinbox.get(),
                erode=self.erode_intspinbox.get(),
                dilate=self.dilate_intspinbox.get(),
                inverse=self.inverse_switch.get(),
                save_path=file
            )

    def load_buton_event(self):
        file = customtkinter.filedialog.askopenfilename()

        if file != '':
            config = configparser.ConfigParser()
            config.read(file)

            self.min_hue_intspinbox.set(int(config['HUE']['min']))
            self.max_hue_intspinbox.set(int(config['HUE']['max']))

            self.min_saturation_intspinbox.set(int(config['SATURATION']['min']))
            self.max_saturation_intspinbox.set(int(config['SATURATION']['max']))

            self.min_value_intspinbox.set(int(config['VALUE']['min']))
            self.max_value_intspinbox.set(int(config['VALUE']['max']))

            self.min_threshold_intspinbox.set(int(config['THRESHOLD']['min']))
            self.max_threshold_intspinbox.set(int(config['THRESHOLD']['max']))

            self.min_area_intspinbox.set(int(config['AREA']['min']))
            self.max_area_intspinbox.set(int(config['AREA']['max']))

            self.blur_intspinbox.set(int(config['BLUR']['value']))
            self.erode_intspinbox.set(int(config['ERODE']['value']))
            self.dilate_intspinbox.set(int(config['DILATE']['value']))

