import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")

# 12:22:33: Main    : before creating thread
# 12:22:33: Main    : before running thread
# 12:22:33: Thread 1: starting
# 12:22:33: Main    : wait for the thread to finish
# 12:22:33: Main    : all done
# 12:22:35: Thread 1: finishing