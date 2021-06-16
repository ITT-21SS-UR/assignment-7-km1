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

left = [300,400]
right = [700,400]
up = [500,200]
down = [500,600]

directions = [left, right, up, down]

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
        self.current_sensor_data = 0.0
        self.current_target = " "

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
        self.timer.singleShot(2000, self.get_sensor_data_from_random)
        self.timer.singleShot(3000, self.move_to_anchor)
        self.timer.singleShot(4000, self.get_sensor_data_from_anchor)
        self.timer.singleShot(5000, self.move_to_random)
        self.timer.singleShot(6000, self.get_sensor_data_from_random)
        self.timer.singleShot(7000, self.move_to_anchor)
        self.timer.singleShot(8000, self.get_sensor_data_from_anchor)
        self.timer.singleShot(9000, self.move_to_random)
        self.timer.singleShot(10000, self.get_sensor_data_from_random)
        self.timer.singleShot(11000, self.move_to_anchor)
        self.timer.singleShot(12000, self.get_sensor_data_from_anchor)
        self.timer.singleShot(13000, self.move_to_random)
        self.timer.singleShot(14000, self.get_sensor_data_from_random)
        self.timer.singleShot(15000, self.move_to_anchor)
        self.timer.singleShot(16000, self.get_sensor_data_from_anchor)
        self.timer.singleShot(17000, self.move_to_random)
        self.timer.singleShot(18000, self.get_sensor_data_from_random)
        self.timer.singleShot(19000, self.move_to_anchor)
        self.timer.singleShot(20000, self.get_sensor_data_from_anchor)

    def move_to_random(self):
        random_direction = random.choice(directions)
        if(random_direction[0] == 500 and random_direction[1] == 200):
            self.current_target = "up"
        if(random_direction[0] == 500 and random_direction[1] == 600):
            self.current_target = "down"
        if(random_direction[0] == 300 and random_direction[1] == 400):
            self.current_target = "left"
        if(random_direction[0] == 700 and random_direction[1] == 400):
            self.current_target = "right"
        self.circle.move(random_direction[0], random_direction[1])


    def move_to_anchor(self):
         #   print(anchor_x_pos, anchor_y_pos)
            self.circle.move(anchor_x_pos, anchor_y_pos)

    def get_sensor_data_from_random(self):

        if(self.current_target == "left"):
            self.current_sensor_data = sensor.get_value('accelerometer')['x']
            if(self.current_sensor_data >= 7.0):
                self.is_target_hit = True
                print("left hit!")
            else:
                print("left missed!")

        if(self.current_target == "right"):
            self.current_sensor_data = sensor.get_value('accelerometer')['x']
            if (self.current_sensor_data <= -7.0):
                print("right hit!")
            else:
                print("right missed!")

        if(self.current_target == "up"):
            self.current_sensor_data = sensor.get_value('accelerometer')['z']
            if (self.current_sensor_data >= 7.0):
               print("up hit!")
            else:
               print("up missed!")

        if(self.current_target == "down"):
            self.current_sensor_data = sensor.get_value('accelerometer')['z']
            if(self.current_sensor_data <= -7.0):
                print("down hit!")
            else:
                print("down missed")

    def get_sensor_data_from_anchor(self):
        self.current_sensor_data = sensor.get_value('accelerometer')['y']
        if(self.current_sensor_data >= 5.0):
            print("middle hit!")
        else:
            print("middle missed!")


def main():
    app = QApplication(sys.argv)
    win = GameWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
