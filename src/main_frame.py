import customtkinter
import image_utils
from image_analyzer import ImageAnalyzer


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.image_analyzer = None

        self.label = customtkinter.CTkLabel(self, text='')
        self.label.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.label_image = None

        self.label.bind('<Configure>', self.resize_label)
        
    def update_label(self, image_path=None, empty=False):
        if empty:
            self.image_analyzer = None
            self.label.configure(image='')
        if image_path is not None:
            self.image_analyzer = ImageAnalyzer(image_path=image_path)
        if self.image_analyzer is not None:
            img = image_utils.convert_opencv_to_pil(self.image_analyzer.get_image2display())
            self.size = image_utils.get_optimal_size((self.image_analyzer.get_width(), self.image_analyzer.get_height()), 
                                                (self.label.winfo_width(), self.label.winfo_height()))
            self.label_image = customtkinter.CTkImage(img, size=self.size)
            self.label.configure(image=self.label_image)
            

    def resize_label(self, event):
        self.update_label()

    # Mouse event rectangle
    def create_rectangle_with_mouse(self):
        # Variables pour stocker les coordonnées du rectangle
        self.X1 = None
        self.Y1 = None
        self.X2 = None
        self.Y2 = None

        # Associer les fonctions aux événements de la souris
        self.label._label.bind("<Button-1>", self.mouse_down)
        self.label._label.bind("<ButtonRelease-1>", self.mouse_up)

    # Fonction pour gérer l'événement de clic de souris
    def mouse_down(self, event):
        self.X1 = event.x
        self.Y1 = event.y

    # Fonction pour gérer l'événement de relâchement de souris
    def mouse_up(self, event):
        self.X2 = event.x
        self.Y2 = event.y
        # Dessiner le rectangle
        x1 = int((self.image_analyzer.get_width() * self.X1) / self.size[0]) 
        y1 = int((self.image_analyzer.get_height() * self.Y1) / self.size[1])
        x2 = int((self.image_analyzer.get_width() * self.X2) / self.size[0]) 
        y2 = int((self.image_analyzer.get_height() * self.Y2) / self.size[1])

        self.image_analyzer.set_image_process(image_utils.extract_image_portion(self.image_analyzer.get_image(), x1, y1, x2, y2))
        self.image_analyzer.set_image2display(self.image_analyzer.get_image_process())
        self.update_label()

    # Mouse event polygon
    def create_polygon_with_mouse(self):
        # Variables pour stocker les coordonnées du rectangle
        self.points = []

        # Associer les fonctions aux événements de la souris
        self.label._label.bind("<Button-1>", self.mouse_down_polygon)
        self.label._label.bind("<Button-3>", self.enter_down)

    def mouse_down_polygon(self, event):
        self.points.append((event.x,event.y))

    def enter_down(self, event):
        # Dessiner le rectangle
        for i in range(len(self.points)):
            self.points[i] = (int((self.image_analyzer.get_width() * self.points[i][0]) / self.size[0]),
                              int((self.image_analyzer.get_height() * self.points[i][1]) / self.size[1]))

        self.image_analyzer.set_image(image=image_utils.mask_polygon(self.image_analyzer.get_image(), self.points))
        self.image_analyzer.set_image2display(self.image_analyzer.get_image_process())
        self.update_label()


    def unbind_all(self):
        # Associer les fonctions aux événements de la souris
        self.label._label.unbind("<Button-1>")
        self.label._label.unbind("<ButtonRelease-1>")
        self.label._label.unbind("<Button-3>")

