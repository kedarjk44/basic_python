import threading
import datetime
from time import sleep


def print_time(num):
    print(datetime.datetime.now())
    print("Thread number is %s" % num)
    sleep(2)
    print(datetime.datetime.now())
    print("Thread number is %s" % num)


def create_thread(thread_num):
    # print(datetime.datetime.now())
    thread = threading.Thread(target=print_time, args=(thread_num,))
    # thread.start()
    return thread


thread_list = list()
for i in range(1, 4):
    thread = create_thread(i)
    thread_list.append(thread)
    thread.start()

for th in thread_list:
    th.join()
print("End of all threads")

