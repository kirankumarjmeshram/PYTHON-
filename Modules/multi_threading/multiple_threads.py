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

    threads = list()
    for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)

# 12:42:30: Main    : create and start thread 0.
# 12:42:30: Thread 0: starting
# 12:42:30: Main    : create and start thread 1.
# 12:42:30: Thread 1: starting
# 12:42:30: Main    : create and start thread 2.
# 12:42:30: Thread 2: starting
# 12:42:30: Main    : before joining thread 0.
# 12:42:32: Thread 0: finishing
# 12:42:32: Main    : thread 0 done
# 12:42:32: Main    : before joining thread 1.
# 12:42:32: Thread 1: finishing
# 12:42:32: Thread 2: finishing
# 12:42:32: Main    : thread 1 done
# 12:42:32: Main    : before joining thread 2.
# 12:42:32: Main    : thread 2 done