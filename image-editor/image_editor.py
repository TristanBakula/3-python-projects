import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QHBoxLayout,
                             QVBoxLayout, QLineEdit, QPushButton,
                             QListWidget, QComboBox, QFileDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter, ImageEnhance


class ImageEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Editor")
        self.resize(900, 700)

        self.btn_folder = QPushButton("Select Folder")
        self.file_list = QListWidget()

        self.btn_left = QPushButton("Left")
        self.btn_right = QPushButton("Right")
        self.mirror = QPushButton("Mirror")
        self.sharpness = QPushButton("Sharpen")
        self.gray = QPushButton("B/W")
        self.saturation = QPushButton("Color")
        self.contrast = QPushButton("Contrast")
        self.blur = QPushButton("Blur")

        self.filter_box = QComboBox()
        self.filter_box.addItem("Original")
        self.filter_box.addItem("Left")
        self.filter_box.addItem("Right")
        self.filter_box.addItem("Mirror")
        self.filter_box.addItem("Sharpen")
        self.filter_box.addItem("B/W")
        self.filter_box.addItem("Color")
        self.filter_box.addItem("Contrast")
        self.filter_box.addItem("Blur")

        self.picture_box = QLabel("Image will apear here!")
        self.picture_box.setAlignment(Qt.AlignCenter)

        master_layout = QHBoxLayout()

        col1 = QVBoxLayout()
        col2 = QVBoxLayout()

        col1.addWidget(self.btn_folder)
        col1.addWidget(self.file_list)
        col1.addWidget(self.filter_box)
        col1.addWidget(self.btn_left)
        col1.addWidget(self.btn_right)
        col1.addWidget(self.mirror)
        col1.addWidget(self.sharpness)
        col1.addWidget(self.gray)
        col1.addWidget(self.saturation)
        col1.addWidget(self.contrast)
        col1.addWidget(self.blur)

        col2.addWidget(self.picture_box)

        master_layout.addLayout(col1, 20)  #koliko posto zauzima ekrana
        master_layout.addLayout(col2, 80)
        self.setLayout(master_layout)

        self.working_directory = ""
        self.image = None
        self.original = None
        self.filename = None
        self.save_folder = "edits/"

        self.btn_folder.clicked.connect(self.getWorkDirectory)

        self.file_list.currentRowChanged.connect(self.display_image)

        self.gray.clicked.connect(self.gray_filter)

        self.btn_left.clicked.connect(self.rotate_left)

        self.btn_right.clicked.connect(self.rotate_right)

        self.mirror.clicked.connect(self.mirror_filter)

        self.sharpness.clicked.connect(self.sharpen_image)

        self.saturation.clicked.connect(self.color_image)

        self.contrast.clicked.connect(self.contrast_image)

        self.blur.clicked.connect(self.blur_image)

        self.filter_box.currentTextChanged.connect(self.handle_filter)

    def filter(self, files, extensions):
        results = []  
        for file in files:
            for ext in extensions:
                if file.lower().endswith(ext):
                    results.append(file)
        return results
        
    def getWorkDirectory(self):
        self.working_directory = QFileDialog.getExistingDirectory()
        extensions = ['.jpg', '.jpeg', '.png', '.svg']
        filenames = self.filter(os.listdir(self.working_directory), extensions)
        self.file_list.clear()
        for filename in filenames:
            self.file_list.addItem(filename)

        
    def load_image(self, filename):
        self.filename = filename
        fullname = os.path.join(self.working_directory, self.filename)
        self.image = Image.open(fullname)
        self.original = self.image.copy()


    def save_image(self):
        path = os.path.join(self.working_directory, self.save_folder)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)

        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)

    def show_image(self, path):
        self.picture_box.hide()
        image = QPixmap(path)
        w, h = self.picture_box.width(), self.picture_box.height()
        image = image.scaled(w, h, Qt.KeepAspectRatio)
        self.picture_box.setPixmap(image)
        self.picture_box.show()

    def display_image(self):
        if self.file_list.currentRow() >= 0:
            self.filename = self.file_list.currentItem().text()
            self.load_image(self.filename)
            self.show_image(os.path.join(self.working_directory, self.filename))


    def gray_filter(self):
        self.image = self.image.convert("L")
        self.save_image()
        self.image_path = os.path.join(self.working_directory, self.save_folder, self.filename)
        self.show_image(self.image_path)

    def rotate_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.save_image()
        self.image_path = os.path.join(self.working_directory, self.save_folder, self.filename)
        self.show_image(self.image_path)

    def rotate_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.save_image()
        self.image_path = os.path.join(self.working_directory, self.save_folder, self.filename)
        self.show_image(self.image_path)

    def mirror_filter(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
        self.image_path = os.path.join(self.working_directory, self.save_folder, self.filename)
        self.show_image(self.image_path)

    def sharpen_image(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.save_image()
        self.image_path = os.path.join(self.working_directory, self.save_folder, self.filename)
        self.show_image(self.image_path)

    def color_image(self):
        self.image = ImageEnhance.Color(self.image).enhance(1.2)
        self.save_image()
        self.image_path = os.path.join(self.working_directory, self.save_folder, self.filename)
        self.show_image(self.image_path)

    def contrast_image(self):
        self.image = ImageEnhance.Contrast(self.image).enhance(1.2)
        self.save_image()
        self.image_path = os.path.join(self.working_directory, self.save_folder, self.filename)
        self.show_image(self.image_path)

    def blur_image(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.save_image()
        self.image_path = os.path.join(self.working_directory, self.save_folder, self.filename)
        self.show_image(self.image_path)

    def apply_filter(self, filter_name):
        if filter_name == "Original":
            self.image = self.original.copy()
        else:
            mapping = {
                "B/W": lambda image: self.image.convert("L"),
                "Color": lambda image: ImageEnhance.Color(image).enhance(1.2),
                "Left": lambda image: image.transpose(Image.ROTATE_90),
                "Right": lambda image: image.transpose(Image.ROTATE_270),
                "Mirror": lambda image: image.transpose(Image.FLIP_LEFT_RIGHT),
                "Sharpen": lambda image: image.filter(ImageFilter.SHARPEN),
                "Blur": lambda image: image.filter(ImageFilter.BLUR),
                "Contrast": lambda image: ImageEnhance.Contrast(image).enhance(1.2)
            }
            filter_function = mapping.get(filter_name)
            if filter_function:
                self.image = filter_function(self.image)
                self.save_image()
                self.image_path = os.path.join(self.working_directory, self.save_folder, self.filename)
                self.show_image(self.image_path)
            pass
        
        self.save_image()
        self.image_path = os.path.join(self.working_directory, self.save_folder, self.filename)
        self.show_image(self.image_path)

    def handle_filter(self):
        if self.file_list.currentRow() >= 0:
            select_filter = self.filter_box.currentText()
            self.apply_filter(select_filter)
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageEditor()
    window.show()
    sys.exit(app.exec_())
