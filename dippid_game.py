# The entire task 7.2 was written by Marco Beetz
# Commented every function

import sys
import random
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from DIPPID import SensorUDP

# Size of the window
win_width = 1000
win_height = 800

# Position of our most crucial circle, the starting circle
# You have to return to it every few seconds
anchor_x_pos = 500
anchor_y_pos = 400

# Positions of the other circles are stored in a list
# Easier to access later instead of e.g. a tuple
left = [300, 400]
right = [700, 400]
up = [500, 200]
down = [500, 600]
directions = [left, right, up, down]

# Connect the sensor
PORT = 5700
sensor = SensorUDP(PORT)


# Constructor inherits from QMainWindow
class GameWindow(QMainWindow):
    def __init__(self, port=5700):
        super(GameWindow, self).__init__()
        self.setGeometry(100, 100, 1000, 800)
        self.initUIComponents()
        self.timer = QTimer(self)
        self.current_sensor_data = 0.0
        self.current_target = " "

# We do not load an extra PyQt5 UI and create everything ourself in the script
# Easier to run from terminal since you do not need an extra .ui file

    def initUIComponents(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Welcome to the best game ever! It's like a workout for your wrist! :-)")
        self.label1.setMinimumSize(900, 100)
        self.label1.move(20, 0)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Hold your device steady in front of you  with the camera facing to your laptop and you looking into the screen")
        self.label2.setMinimumSize(900, 100)
        self.label2.move(20, 40)

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText("Spin your phone to the right or the left to get the horizontal circle left or right")
        self.label3.setMinimumSize(900, 100)
        self.label3.move(20, 60)

        self.label4 = QtWidgets.QLabel(self)
        self.label4.setText("Spin your phone with the screen facing upwards to the sky or the screen facing down to your desk to get a vertical circle up or down")
        self.label4.setMinimumSize(900, 100)
        self.label4.move(20, 80)

        self.label5 = QtWidgets.QLabel(self)
        self.label5.setText("When you have your device ready press the button to start the game!")
        self.label5.setMinimumSize(500, 100)
        self.label5.move(20, 100)

        self.circle = QtWidgets.QDial(self)
        self.circle.setStyleSheet("background-color:red;")
        self.circle.setMinimumSize(100, 100)
        self.circle.move(anchor_x_pos, anchor_y_pos)

        start_button = QtWidgets.QPushButton(self)
        start_button.setText("Start it!")
        start_button.move(400, 180)
        start_button.clicked.connect(self.start_clicked)

        self.score_counter = QtWidgets.QLabel(self)
        self.score_counter.setText("Let's go!")
        self.score_counter.move(800, 500)

# Got the idea to use a sequence of single shots from the link above
# Single Shots are not elegant but very easy to use and suitable for our problem
# More easy than threading, time.sleep() didn't work sufficiently
# We added some error handling to provide the script from crashing
# https://programtalk.com/python-examples/PyQt5.QtCore.QTimer.singleShot/
    def start_clicked(self):
        security_check = sensor.get_capabilities()
        if not security_check:
            print("please start the DIPPID app and enable the send data function !")
        else:
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
            self.timer.singleShot(20500, self.show_final_text)

# Just setting the final text
    def show_final_text(self):
        self.score_counter.setText("It's over! Wanna try again? Press the button!")
        self.score_counter.setMinimumSize(500, 100)
        self.score_counter.move(600, 600)

# Calculate which target will be chosen next and then move the circle
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

# Always move the circle back to the beginning
# To guarantee a proper starting point for the accelerometer data
    def move_to_anchor(self):
            self.circle.move(anchor_x_pos, anchor_y_pos)

# With gravity being 9.81ms² we argue that 5.0 or above is an appropriate value
# If the phone was spinned correctly
    def get_sensor_data_from_random(self):
        if(self.current_target == "left"):
            self.current_sensor_data = sensor.get_value('accelerometer')['x']
            if(self.current_sensor_data >= 0.8):
                self.score_counter.setText("you made it!")
            else:
                self.score_counter.setText("try it again!")

# Do it again for all four possible target positions.
# Could also use a switch case or something else but it works fine
        if(self.current_target == "right"):
            self.current_sensor_data = sensor.get_value('accelerometer')['x']
            if (self.current_sensor_data <= -0.8):
                self.score_counter.setText("you made it!")
            else:
                self.score_counter.setText("try again!")

        if(self.current_target == "up"):
            self.current_sensor_data = sensor.get_value('accelerometer')['z']
            if (self.current_sensor_data >= 0.8):
                self.score_counter.setText("you made it!")
            else:
                self.score_counter.setText("try again!")

        if(self.current_target == "down"):
            self.current_sensor_data = sensor.get_value('accelerometer')['z']
            if(self.current_sensor_data <= -0.8):
                self.score_counter.setText("you made it!")
            else:
                self.score_counter.setText("try again!")

# We read Y-Data for the anchor since you need to hold the pone steady
# In front of you (z and x being irrelevant)
    def get_sensor_data_from_anchor(self):
        self.current_sensor_data = sensor.get_value('accelerometer')['y']
        if(self.current_sensor_data >= 0.8):
            self.score_counter.setText("stay ready...")
        else:
            print("oh...to slow!")

# Execute the script with the pythonic conventions
def main():
    app = QApplication(sys.argv)
    win = GameWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
