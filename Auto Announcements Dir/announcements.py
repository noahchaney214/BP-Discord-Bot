import time


class Announcement:
    message = ""
    t = "2023"

    def __init__(self, message, t):
        self.message = message
        self.t = t

    def announce(self):
        print(self.message)

    def change_msg(self, new_msg):
        self.message = new_msg

    def change_time(self, new_time):
        self.t = new_time

