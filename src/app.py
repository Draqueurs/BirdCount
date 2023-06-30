import customtkinter
from option_frame import OptionFrame
from main_frame import MainFrame


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("BiredCount")
        self.iconbitmap('./icones/dove.ico')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, minsize=250, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.option_frame = OptionFrame(self)
        self.option_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.main_frame = MainFrame(self)
        self.main_frame.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")

app = App()
app.mainloop()