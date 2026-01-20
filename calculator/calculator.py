from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon, QFontDatabase, QFont


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.resize(350, 450)
        self.setWindowIcon(QIcon("assets/calc.jpg"))

        font_id = QFontDatabase.addApplicationFont("assets/digital-7.ttf")
        family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.font_family = family

        self.text_box = QLineEdit("0")
        self.text_box.setAlignment(Qt.AlignRight)
        self.text_box.setFont(QFont(self.font_family, 60))

        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(0)
        self.create_buttons()

        self.clear_button = QPushButton("Clear")
        self.clear_button.setObjectName("cleardel")
        self.clear_button.clicked.connect(self.button_clicked)

        self.delete_button = QPushButton("Del")
        self.delete_button.setObjectName("cleardel")
        self.delete_button.clicked.connect(self.button_clicked)

        self.button_row_layout = QHBoxLayout()
        self.button_row_layout.setContentsMargins(0, 0, 0, 0)
        self.button_row_layout.addWidget(self.clear_button)
        self.button_row_layout.addWidget(self.delete_button)

        self.master_layout = QVBoxLayout()
        self.master_layout.addWidget(self.text_box)
        self.master_layout.addLayout(self.grid_layout)
        self.master_layout.addLayout(self.button_row_layout)
        self.setLayout(self.master_layout)

        self.setStyleSheet("""
            QWidget{
                background-color: white;
            }
            QLineEdit{
                background-color: #505050;
                border-radius: 0px;
                padding-top: 20px;
                padding-left: 5px;
                padding-right: 5px;
                padding-bottom: 5px;
                font-size: 70px;
                color: white;
            }
            QPushButton{
                padding-top: 15px;
                padding-bottom: 15px;
                border-radius: 0px;
                background-color: #D4D4D2;
                border: 1px solid black;
            }
            QPushButton#operator {
                background-color: #FF9500;
                color: white;
                font-weight: bold;
            }
            QPushButton#cleardel{
                font-size: 25px;
            }
        """)

    def create_buttons(self):
        buttons = ["7", "8", "9", "/",
                   "4", "5", "6", "*",
                   "1", "2", "3", "-",
                   "0", ".", "=", "+"]
        row = 0
        col = 0
        self.button_widgets = []  
        for text in buttons:
            button = QPushButton(text)
            button.setFont(QFont(self.font_family, 25))
            button.clicked.connect(self.button_clicked)

            if col == 3 or (col == 2 and row == 3):
                button.setObjectName("operator")

            self.grid_layout.addWidget(button, row, col)
            self.button_widgets.append(button)  # Sprema se za kasniju upotrebu
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_clicked(self):
        button = self.sender()
        value = button.text()
        current_text = self.text_box.text()

        if value == "=":
            try:
                value_result = round(eval(current_text), 5)
                result = str(value_result).rstrip("0").rstrip(".")
                self.text_box.setText(result)
            except:
                self.text_box.setText("Error")
        elif value == "Clear":
            self.text_box.setText("0")
        elif value == "Del":
            new_text = current_text[:-1] if len(current_text) > 1 else "0"
            self.text_box.setText(new_text)
        else:
            if current_text == "0":
                self.text_box.setText(value)
            else:
                self.text_box.setText(current_text + value)


if __name__ == "__main__":
    app = QApplication([])
    calc = Calculator()
    calc.show()
    app.exec_()
