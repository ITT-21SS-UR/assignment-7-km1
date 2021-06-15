from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
import sys
import random
from DIPPID import SensorUDP
import time

win_width = 1000
win_height = 800
anchor_x_pos = 500
anchor_y_pos = 400
random_x_pos = [300,700]
random_y_pos = [200,600]

selected_random_values_x = []
selected_random_values_y = []

measured_sensor_values_x = []
measured_sensor_values_y = []

PORT = 5700
sensor = SensorUDP(PORT)

won = "0"
played = "0"

class GameWindow(QMainWindow):
    def __init__(self, port=5700):
        super(GameWindow, self).__init__()
        self.setGeometry(100,100,1000,800)
        self.initUIComponents()
        self.timer = QTimer(self)

    def initUIComponents(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Keep your device steady in front of you on the table")
        self.label1.setMinimumSize(500,100)
        self.label1.move(0,0)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Try to follow the circle as good as you can! The x represents your position")
        self.label2.setMinimumSize(500,100)
        self.label2.move(0,20)

        self.score_counter = QtWidgets.QLabel(self)
        self.score_counter.setText(won + "/" + played)
        self.score_counter.move(700,100)

        self.circle = QtWidgets.QDial(self)
        self.circle.setStyleSheet("background-color:red;")
        self.circle.setMinimumSize(100, 100)
        self.circle.move(anchor_x_pos, anchor_y_pos)

        start_button = QtWidgets.QPushButton(self)
        start_button.setText("Start it!")
        start_button.move(800, 100)
        start_button.clicked.connect(self.start_clicked)

    def start_clicked(self):
        self.timer.singleShot(1000, self.move_to_random)
        self.timer.singleShot(1500, self.get_sensor_data)
        self.timer.singleShot(2500, self.move_to_anchor)
        self.timer.singleShot(4000, self.move_to_random)
        self.timer.singleShot(4500, self.get_sensor_data)
        self.timer.singleShot(5500, self.move_to_anchor)
        self.timer.singleShot(7000, self.move_to_random)
        self.timer.singleShot(7500, self.get_sensor_data)
        self.timer.singleShot(8500, self.move_to_anchor)
        self.timer.singleShot(10000, self.move_to_random)
        self.timer.singleShot(10500, self.get_sensor_data)
        self.timer.singleShot(11500, self.move_to_anchor)
        self.timer.singleShot(13000, self.move_to_random)
        self.timer.singleShot(13500, self.get_sensor_data)
        self.timer.singleShot(14500, self.move_to_anchor)
        self.timer.singleShot(15000, self.get_sensor_data)
        self.timer.singleShot(15500, self.print_sensor_data)

    def print_sensor_data(self):
        print(measured_sensor_values_x)
        print(measured_sensor_values_y)
        print("und")
        print(selected_random_values_x)
        print(selected_random_values_y)

    def move_to_random(self):
            random_x = random.choice(random_x_pos)
            random_y = random.choice(random_y_pos)
            selected_random_values_x.append(random_x)
            selected_random_values_y.append(random_y)
            self.circle.move(random_x,random_y)
       #     print(random_x, random_y)
            self.get_sensor_data()


    def move_to_anchor(self):
            self.circle.move(anchor_x_pos, anchor_y_pos)

    def get_sensor_data(self):
        if (sensor.has_capability('accelerometer')):
         #   print('accelerometer X: ', sensor.get_value('accelerometer')['x'])
          #  print('accelerometer Y: ', sensor.get_value('accelerometer')['y'])

            delta_x = sensor.get_value('accelerometer')['x']
            delta_y = sensor.get_value('accelerometer')['y']
         #   print(delta_x, delta_y)
            measured_sensor_values_x.append(delta_x)
            measured_sensor_values_y.append(delta_y)


def main():
    app = QApplication(sys.argv)
    win = GameWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
