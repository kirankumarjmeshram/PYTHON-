 # The difference here is that the final line of the output is missing. thread_function() did not get a 
    # chance to complete. It was a daemon thread, so when __main__ 
    # reached the end of its code and the program wanted to finish, the daemon was killed.


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
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)    
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")

# 12:34:32: Main    : before creating thread
# 12:34:32: Main    : before running thread
# 12:34:32: Thread 1: starting
# 12:34:32: Main    : wait for the thread to finish
# 12:34:32: Main    : all done
    
#IF WE UNCOMMENT x.join()
# 12:39:48: Main    : before creating thread
# 12:39:48: Main    : before running thread
# 12:39:48: Thread 1: starting
# 12:39:48: Main    : wait for the thread to finish
# 12:39:50: Thread 1: finishing
# 12:39:50: Main    : all done
    

   