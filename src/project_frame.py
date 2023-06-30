import customtkinter
from PIL import Image
import os
from two_scrollable_frame import TwoScrollableFrame


class ProjectFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.plus_image = customtkinter.CTkImage(light_image=Image.open("icons/plus_light.png"),
                                                 dark_image=Image.open("icons/plus_dark.png"),
                                                 size=(20, 20))
        self.minus_image = customtkinter.CTkImage(light_image=Image.open("icons/minus_light.png"),
                                                  dark_image=Image.open("icons/minus_dark.png"),
                                                  size=(20, 20))

        self.project_name_frame = customtkinter.CTkFrame(self, width=210)
        self.project_name_frame.grid_columnconfigure(0, weight=1)
        self.project_name_frame.grid(row=0, column=0, padx=10, pady=(10,5), sticky="nsew")

        self.project_main_frame = customtkinter.CTkFrame(self)
        self.project_main_frame.grid_columnconfigure(0, weight=1)
        self.project_main_frame.grid_columnconfigure(1, weight=1)
        self.project_main_frame.grid_columnconfigure(2, weight=1)

        self.project_label = customtkinter.CTkLabel(self.project_name_frame, text='Project')
        self.project_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")

        self.project_check = False

        self.project_button = customtkinter.CTkButton(self.project_name_frame, width=30, fg_color='transparent', text='', image=self.plus_image, command=self.project_button_event)
        self.project_button.grid(row=0, column=1, padx=10, pady=10, sticky="nse")

        self.files_list_scrollable_frame = TwoScrollableFrame(self.project_main_frame, fg_color='transparent')
        self.files_list_scrollable_frame.grid(row=1, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")

        self.add_files_button = customtkinter.CTkButton(self.project_main_frame, text='Add Files', command=self.add_files_button_event)
        self.add_files_button.grid(row=2, column=0, padx=(5,2), pady=10, sticky="nsew")

        self.remove_files_button = customtkinter.CTkButton(self.project_main_frame, text='Removes', command=self.remove_files_button_event)
        self.remove_files_button.grid(row=2, column=1, padx=(5,2), pady=10, sticky="nsew")

        self.remove_file_button = customtkinter.CTkButton(self.project_main_frame, text='Remove', command=self.remove_file_button_event)
        self.remove_file_button.grid(row=2, column=2, padx=(5,2), pady=10, sticky="nsew")

        self.button_clicked_name = None
        self.files_list_buttons = {}

    def project_button_event(self):
        if self.project_check:
            self.project_button.configure(image=self.plus_image)
            self.configure(height=30)
            self.project_main_frame.grid_forget()
        else:
            self.project_button.configure(image=self.minus_image)
            self.configure(height=60)
            self.project_main_frame.grid(row=1, column=0, padx=10, pady=(5,10), sticky="nsew")
        self.project_check = not self.project_check

    def add_files_button_event(self):
        filetypes = (("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*"))
        images = customtkinter.filedialog.askopenfilenames(filetypes=filetypes)

        if images:
            self.create_files_list_button(images)

    def create_files_list_button(self, filenames):
        for file in filenames:
            if file not in self.files_list_buttons.keys():
                self.files_list_buttons[file] = customtkinter.CTkButton(self.files_list_scrollable_frame, text=file, anchor='w', command=lambda m=file: self.files_list_button_event(m))
        self.update_grid_button()

    def extract_image_names(self, images):
        image_names = []
        for image in images:
            image_name = os.path.basename(image)
            image_names.append(image_name)
        return image_names
    
    def files_list_button_event(self, name):
        if self.button_clicked_name is not None:
            self.files_list_buttons[self.button_clicked_name].configure(fg_color=['#3B8ED0', '#1F6AA5'])
        self.files_list_buttons[name].configure(fg_color='gray')
        self.button_clicked_name = name
        self.master.master.master.master.main_frame.update_label(image_path=name)

    def remove_files_button_event(self):
        for key, value in self.files_list_buttons.items():
            value.destroy()
        self.button_clicked_name = None
        self.files_list_buttons = {}
        self.master.master.master.master.main_frame.update_label(empty=True)

    def remove_file_button_event(self):
        if self.button_clicked_name is not None:
            self.files_list_buttons[self.button_clicked_name].destroy()
            del self.files_list_buttons[self.button_clicked_name]
            self.button_clicked_name = None
            if len(list(self.files_list_buttons.keys())) > 0:
                self.files_list_button_event(list(self.files_list_buttons.keys())[0])
                self.update_grid_button()
            else:
                self.master.master.master.master.main_frame.update_label(empty=True)

    def update_grid_button(self):
        idx_row = 0
        for key, value in self.files_list_buttons.items():
            value.grid_forget()
        for key, value in self.files_list_buttons.items():
            value.grid(row=idx_row, column=0, padx=10, pady=0, sticky="nsew")
            idx_row += 1