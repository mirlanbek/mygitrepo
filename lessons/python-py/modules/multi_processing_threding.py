# # -------------------------------------------------------------

import multiprocessing

def worker(num):
    """thread worker function"""
    print 'Worker:', num
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()

# -------------------------------------

import multiprocessing 
import os 
  
def worker1(): 
    # printing process id 
    print("ID of process running worker1: {}".format(os.getpid())) 
  
def worker2(): 
    # printing process id 
    print("ID of process running worker2: {}".format(os.getpid())) 
  
if __name__ == "__main__": 
    # printing main program process id 
    print("ID of main process: {}".format(os.getpid())) 
  
    # creating processes 
    p1 = multiprocessing.Process(target=worker1) 
    p2 = multiprocessing.Process(target=worker2) 
  
    # starting processes 
    p1.start() 
    p2.start() 
  
    # process IDs 
    print("ID of process p1: {}".format(p1.pid)) 
    print("ID of process p2: {}".format(p2.pid)) 
  
    # wait until processes are finished 
    p1.join() 
    p2.join() 
  
    # both processes finished 
    print("Both processes finished execution!") 
  
    # check if processes are alive 
    print("Process p1 is alive: {}".format(p1.is_alive())) 
    print("Process p2 is alive: {}".format(p2.is_alive())) 



# importing the multiprocessing module 
import multiprocessing 
  
def print_cube(num): 
    """ 
    function to print cube of given num 
    """
    print("Cube: {}".format(num * num * num)) 
  
def print_square(num): 
    """ 
    function to print square of given num 
    """
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__": 
    # creating processes 
    p1 = multiprocessing.Process(target=print_square, args=(10, )) 
    p2 = multiprocessing.Process(target=print_cube, args=(10, )) 

 #  t1 = threading.Thread(target=task1, name='t1') 
  # t2 = threading.Thread(target=task2, name='t2')   
  
  
    # starting process 1 
    p1.start() 
    # starting process 2 
    p2.start() 
  
    # wait until process 1 is finished 
    p1.join() 
    # wait until process 2 is finished 
    p2.join() 
  
    # both processes finished 
    print("Done!") 



# *********************************  MULTITHRTEDING ***********************************************88


# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading 
  
def print_cube(num): 
    """ 
    function to print cube of given num 
    """
    print("Cube: {}".format(num * num * num)) 
  
def print_square(num): 
    """ 
    function to print square of given num 
    """
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=print_square, args=(10,)) 
    t2 = threading.Thread(target=print_cube, args=(10,)) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!") 


# # --------------------------------------------------



# Python program to illustrate the concept 
# of threading 
import threading 
import os 
  
def task1(): 
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name)) 
    print("ID of process running task 1: {}".format(os.getpid())) 
  
def task2(): 
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name)) 
    print("ID of process running task 2: {}".format(os.getpid())) 
  
if __name__ == "__main__": 
  
    # print ID of current process 
    print("ID of process running main program: {}".format(os.getpid())) 
  
    # print name of main thread 
    print("Main thread name: {}".format(threading.current_thread().name)) 
  
    # creating threads 
    t1 = threading.Thread(target=task1, name='t1') 
    t2 = threading.Thread(target=task2, name='t2')   
  
    # starting threads 
    t1.start() 
    t2.start() 
  
    # wait until all threads finish 
    t1.join() 
    t2.join() 


# ----------------------------CONCURRENT-FEATURES--------------------

import concurrent.futures
import time

def do_something(seconds):
    print(f"Sleeping {seconds} seconds ... ")
    time.sleep(seconds)
    return "done sleeping"

with concurrent.futures.ProcessPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 1)
    print(f1.result())
    print(f2.result())
import multiprocessing
import concurrent.futures
import time

def do_something(seconds):
    print(f"Sleeping {seconds} seconds ... ")
    time.sleep(seconds)

    return "done sleeping"

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)


# with concurrent.futures.ProcessPoolExecutor() as executor:    
#     f1 = executor.submit(do_something, 1)
#     f2 = executor.submit(do_something, 1)


#     print(f1.result())
#     print(f2.result())

