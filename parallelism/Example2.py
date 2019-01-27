# Example2.py
'''
A more realistic thread pool example
'''

import time
import threading
import queue
import urllib


class Consumer(threading.Thread):
    def __init__(self, my_queue):
        threading.Thread.__init__(self)
        self._my_queue = my_queue

    def run(self):
        while True:
            content = self._my_queue.get()
            if isinstance(content, str) and content == 'quit':
                break
            response = urllib.request.urlopen(content)
            print("website {} has status {}".format(content, response.status))
        print('Bye byes!')


def Producer():
    urls = ['http://www.python.org', 'http://www.yahoo.com', 'http://www.google.com']
    my_queue = queue.Queue()
    worker_threads = build_worker_pool(my_queue, 4)
    start_time = time.time()

    # Add the urls to process
    for url in urls:
        my_queue.put(url)

    # Add the poison pillv
    for worker in worker_threads:
        my_queue.put('quit')

    my_queue.task_done()

    for worker in worker_threads:
        worker.join()

    print('Done! Time taken: {}'.format(time.time() - start_time))


def build_worker_pool(my_queue, size):
    workers = []
    for _ in range(size):
        worker = Consumer(my_queue)
        worker.start()
        workers.append(worker)
    return workers


if __name__ == '__main__':
    Producer()
