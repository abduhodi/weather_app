from PyQt6.QtWidgets import QLabel, QApplication, QMainWindow, QPushButton, QComboBox
from PyQt6.QtGui import QIcon
from config.weather import get_weather
import google

class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Weather 1.0.1")
        self.setWindowIcon(QIcon("./img/cloudy.png"))
        self.setFixedSize(500, 500)
        self.setGeometry(500, 200, 500, 500)
        self.update_btn = QPushButton("UPDATE", self)
        self.update_btn.setGeometry(10, 400, 150, 40)
        self.update_btn.clicked.connect(self.get_weather)


        self.send_btn = QPushButton("SEND", self)
        self.send_btn.setGeometry(175, 400, 150, 40)
        # self.send_btn.clicked.connect(self.send_bot)

        self.exit_btn = QPushButton("EXIT", self)
        self.exit_btn.setGeometry(340, 400, 150, 40)
        self.exit_btn.clicked.connect(self.exit)

        self.city_name_label = QLabel("CITY NAME:  ", self)
        self.city_name_label.setGeometry(20, 50, 450, 40)
        city_name_style = """
        font-size: 20px;
        """
        self.city_name_label.setStyleSheet(city_name_style)

        self.city_list = QComboBox(self)
        cities = [
            "Andijan", "Fergana", "Namangan", "Tashkent", "Sirdaryo", "Samarqand", "Jizzax",
            "Qashqadaryo", "Buxoro", "Navoiy",
        ]
        self.city_list.addItems(cities)
        city_list_style = """
        font-size: 18px;
        """
        self.city_list.setStyleSheet(city_list_style)
        self.city_list.setGeometry(140, 50, 200, 40)
        self.city_list.setCurrentText("Please select Region")

        self.text_weather = "WEATHER:  "
        self.weather_label = QLabel(self.text_weather, self)
        self.weather_label.setGeometry(20, 150, 450, 40)
        self.setStyleSheet(city_name_style)

        self.text_temp = "TEMERATURA:  "
        self.temp_label = QLabel(self.text_temp, self)
        self.temp_label.setGeometry(20, 250, 450, 40)
        self.setStyleSheet(city_name_style)



    def get_weather(self):
        city_name = self.city_list.currentText()
        weather_list = get_weather(city_name)
        weather = weather_list[0]
        temp = weather_list[-1]
        self.weather_label.setText('')
        self.weather_label.setText(self.text_weather + str(weather))

        self.temp_label.setText('')
        self.temp_label.setText(self.text_temp + str(temp) + ' °C')

        weathers = ["Clouds", "Rain", "Sun", "Drizzle", "Mist"]


    # def send_bot(self):
    #     self.weather_label.setText('')
    #     self.weather_label.setText(self.text_weather + str(weather))

    def exit(self):
        QApplication.quit()
        

        