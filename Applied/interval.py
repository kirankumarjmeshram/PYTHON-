# import time
# import threading

# def print_hello_world():
#     while True:
#         print("Hello World")
#         time.sleep(0.3)

# # Instead of importing the Thread class from the threading module, we create our own thread class
# class MyThread(threading.Thread):
#     def __init__(self):
#         super().__init__()

#     def run(self):
#         print_hello_world()

# thread = MyThread()
# thread.start()


import time
import threading

def print_hello_world():
    try:
        while True:
            print("Hello World")
            time.sleep(0.3)
    except KeyboardInterrupt:
        print("Exiting...")

# Instead of importing the Thread class from the threading module, we create our own thread class
class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print_hello_world()

thread = MyThread()
thread.start()
