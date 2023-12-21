import logging
import concurrent.futures as cf
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    with cf.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))

# 12:51:16: Thread 0: starting
# 12:51:16: Thread 1: starting
# 12:51:16: Thread 2: starting
# 12:51:18: Thread 0: finishing
# 12:51:18: Thread 1: finishing
# 12:51:18: Thread 2: finishing