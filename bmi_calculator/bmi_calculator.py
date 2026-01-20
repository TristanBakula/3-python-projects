import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QHBoxLayout,
                            QVBoxLayout, QLineEdit, QPushButton)
from PyQt5.QtCore import Qt


class BMI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.resize(700, 300)

#LIJEVA STRANA
        self.title_left = QLabel("BMI CALCULATOR")
        self.title_left.setObjectName("title_left")

        self.height_text = QLabel("Height")
        self.height_text.setObjectName("height_text")
        self.weight_text = QLabel("Weight")
        self.weight_text.setObjectName("weight_text")

        self.centimeter_ql = QLineEdit()
        self.kilogram_ql = QLineEdit()

        self.centimeter_text = QLabel("Centimeters")
        self.centimeter_text.setObjectName("centimeter_text")
        self.kilogram_text = QLabel("Kilograms")
        self.kilogram_text.setObjectName("kilogram_text")

        self.calculate_button = QPushButton("Calculate Your BMI")
                            #KRAJ LIJEVE STRANE

#DESNA STRANA
        self.title_right = QLabel("BMI CATEGORIES")
        self.title_right.setObjectName("title_right")
        self.text11 = QLabel("BMI Category")
        self.text11.setObjectName("text11")
        self.text12 = QLabel("Underweight")
        self.text12.setObjectName("text12")
        self.text13 = QLabel("Healthy")
        self.text13.setObjectName("text13")
        self.text14 = QLabel("Overweight")
        self.text14.setObjectName("text14")
        self.text15 = QLabel("Obesity")
        self.text15.setObjectName("text15")

        self.text21 = QLabel("BMI Range")
        self.text21.setObjectName("text21")
        self.text22 = QLabel("Below 18.5")
        self.text22.setObjectName("text22")
        self.text23 = QLabel("18.5 - 24.9")
        self.text23.setObjectName("text23")
        self.text24 = QLabel("25.0 - 29.9")
        self.text24.setObjectName("text24")
        self.text25 = QLabel("30.0 or above")
        self.text25.setObjectName("text25")

                            #KRAJ DESNE STRANE

        master_layout = QHBoxLayout()
        
        col1 = QVBoxLayout()
        col1.setAlignment(Qt.AlignTop)
        col2 = QVBoxLayout()
        col2.setAlignment(Qt.AlignTop)

        col_mid = QVBoxLayout()


        col1_hor = QHBoxLayout()

        height_col = QVBoxLayout()
        height_col.addWidget(self.height_text)
        height_col1_input = QHBoxLayout()
        height_col1_input.addWidget(self.centimeter_ql)
        height_col1_input.addWidget(self.centimeter_text)
        height_col.addLayout(height_col1_input)
        col1_hor.addLayout(height_col)

        col1.addWidget(self.title_left)
        col1.addLayout(col1_hor)
        col1.addWidget(self.calculate_button)


        weight_col = QVBoxLayout()
        weight_col.addWidget(self.weight_text)
        weight_col1_input = QHBoxLayout()
        weight_col1_input.addWidget(self.kilogram_ql)
        weight_col1_input.addWidget(self.kilogram_text)
        weight_col.addLayout(weight_col1_input)
        col1_hor.addLayout(weight_col)

        col2_hor1 = QHBoxLayout()
        col2_hor1.addWidget(self.text11)
        col2_hor1.addWidget(self.text21)

        col2_hor2 = QHBoxLayout()
        col2_hor2.addWidget(self.text12)
        col2_hor2.addWidget(self.text22)

        col2_hor3 = QHBoxLayout()
        col2_hor3.addWidget(self.text13)
        col2_hor3.addWidget(self.text23)

        col2_hor4 = QHBoxLayout()
        col2_hor4.addWidget(self.text14)
        col2_hor4.addWidget(self.text24)

        col2_hor5 = QHBoxLayout()
        col2_hor5.addWidget(self.text15)
        col2_hor5.addWidget(self.text25)


        col2.addWidget(self.title_right)
        col2.addLayout(col2_hor1)
        col2.addLayout(col2_hor2)
        col2.addLayout(col2_hor3)
        col2.addLayout(col2_hor4)
        col2.addLayout(col2_hor5)
        
        
        
        master_layout.addLayout(col1, 45)
        master_layout.addLayout(col_mid, 10)
        master_layout.addLayout(col2, 45)
        self.setLayout(master_layout)


        self.title_left.setAlignment(Qt.AlignCenter)
        self.title_right.setAlignment(Qt.AlignCenter)

        self.calculate_button.clicked.connect(self.bmi_button_clicked)

        self.setStyleSheet("""
                QLabel{
                    background-color: white;
                    color: black;
                    font-size: 20px;
                }
                QLabel#title_left{
                    background: qlineargradient(
                         x1:0, y1:0, x2:1, y2:1,
                         stop:0 #87CEFA,
                         stop:1 #00008B
                        );
                    padding: 20px;
                    border-radius: 10px;
                    color: white;
                    font-family: Arial;
                    font-weight: bold;
                }
                QLabel#title_right{
                    background: qlineargradient(
                         x1:0, y1:0, x2:1, y2:1,
                         stop:0 #00008B,
                         stop:1 #87CEFA
                        );
                    padding: 20px;
                    border-radius: 10px;
                    color: white;
                    font-family: Arial;
                    font-weight: bold;
                    
                }
                QLabel#height_text, QLabel#weight_text{
                        padding-top: 50px;
                        padding-left: 10px;
                        padding-right: 10px;
                        padding-bottom: 5px;
                        background-color: none;
                        font-size: 20px;
                }
                QLineEdit{
                        font-size: 15px;
                        border-radius: 5px;
                        outline: 2px solid;
                        border: 1px solid;
                        margin-left: 10px;
                        padding-top: 5px;
                        padding-bottom: 5px;
                }
                QLabel#centimeter_text, QLabel#kilogram_text{
                        background-color: none;
                        font-size: 15px;
                        font-family: Arial;
                }
                QPushButton{
                        border-radius: 20px;
                        background-color: #87CEFA;
                        max-width: 155px;
                        padding: 15px;
                        margin-top: 50px;
                        font-size: 15px;
                        color: white;
                }
                QPushButton:hover{
                        background-color: white;
                        border: 2px solid #87CEFA;
                        border-radius: 20px;
                        color: #87CEFA;
                }
                QLabel#text12, QLabel#text13, QLabel#text14, QLabel#text15{
                    background: none;
                    color: black;
                    font-family: Arial;
                    padding-left: 5px;
                    padding-top: 15px;
                    padding-right: 0px;
                    padding-bottom: 5px;
                    font-size: 15px;
                }
                QLabel#text11, QLabel#text21{
                    background: none;
                    color: black;
                    font-family: Arial;
                    padding-left: 5px;
                    padding-top: 15px;
                    padding-right: 0px;
                    padding-bottom: 5px;
                    font-weight: bold;
                    font-size: 15px;
                }
                QLabel#text22, QLabel#text23, QLabel#text24, QLabel#text25{
                   background: none;
                    color: black;
                    font-family: Arial;
                    padding-left: 5px;
                    padding-top: 15px;
                    padding-right: 0px;
                    padding-bottom: 5px;
                    font-size: 15px;
                }
        """)
 
    def bmi_button_clicked(self):
        
       
        try:
                height = float(self.centimeter_ql.text())
                weight = float(self.kilogram_ql.text())
        except ValueError:
                self.title_right.setText("Invalid input!")
                return

    
        if height <= 0 or weight <= 0:
                self.title_right.setText("Invalid input!")
                return

        
        bmi = float(weight / ((height / 100) ** 2))

        self.title_right.setText(f"Your BMI is: {bmi:.1f}")


       
        for lbl in [self.text12, self.text13, self.text14, self.text15,
                   self.text22, self.text23, self.text24, self.text25]:
              lbl.setStyleSheet("background: none; font-weight: normal;")



        if bmi > 0 and bmi < 18.5:
                self.text12.setStyleSheet("background-color: #9be4f2; font-weight: bold;")
                self.text22.setStyleSheet("background-color: #9be4f2; font-weight: bold;")
        elif bmi >= 18.5 and bmi <= 24.9:
                self.text13.setStyleSheet("background-color: #9be4f2; font-weight: bold;")
                self.text23.setStyleSheet("background-color: #9be4f2; font-weight: bold;")
        elif bmi >= 25.0 and bmi <= 29.9:
                self.text14.setStyleSheet("background-color: #9be4f2; font-weight: bold;")
                self.text24.setStyleSheet("background-color: #9be4f2; font-weight: bold;")
        elif bmi > 30:
                self.text15.setStyleSheet("background-color: #9be4f2; font-weight: bold;")
                self.text25.setStyleSheet("background-color: #9be4f2; font-weight: bold;")
        else:
               self.title_right.setText("Invalid input!") 


        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMI()
    window.show()
    sys.exit(app.exec_())




