#Example.py
'''
Standard Producer/Consumer Threading Pattern
'''

import time
import threading
import queue

class Consumer(threading.Thread):
    def __init__(self, my_queue):
        threading.Thread.__init__(self)
        self._my_queue = my_queue

    def run(self):
        while True:
            # my_queue.get() blocks the current thread until
            # an item is retrieved.
            msg = self._my_queue.get()
            # Checks if the current message is
            # the "Poison Pill"
            if isinstance(msg, str) and msg == 'quit':
                # if so, exists the loop
                break
            # "Processes" (or in our case, prints) the queue item
            print("I'm a thread, and I received %s!!" % msg)
        # Always be friendly!
        print('Bye byes!')


def Producer():
    # Queue is used to share items between
    # the threads.
    my_queue = queue.Queue()

    # Create an instance of the worker
    worker = Consumer(my_queue)

    # start calls the internal run() method to
    # kick off the thread
    worker.start()

    # variable to keep track of when we started
    start_time = time.time()

    # While under 5 seconds..
    while time.time() - start_time < 5:
        # "Produce" a piece of work and stick it in
        # the queue for the Consumer to process
        my_queue.put('something at %s' % time.time())
        # Sleep a bit just to avoid an absurd number of messages
        time.sleep(1)

    # This the "poison pill" method of killing a thread.
    my_queue.put('quit')
    # wait for the thread to close down
    worker.join()


if __name__ == '__main__':
    Producer()