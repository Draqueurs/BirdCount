import customtkinter
from region_shape_frame import RegionShapeFrame
from project_frame import ProjectFrame
from attributes_frame import AttributesFrame
from settings_frame import SettingsFrame

class OptionFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        
        self.region_shape_frame = RegionShapeFrame(self)
        self.region_shape_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.project_frame = ProjectFrame(self)
        self.project_frame.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")

        self.attributes_frame = AttributesFrame(self)
        self.attributes_frame.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")

        self.settings_frame = SettingsFrame(self)
        self.settings_frame.grid(row=3, column=0, padx=0, pady=0, sticky="nsew")