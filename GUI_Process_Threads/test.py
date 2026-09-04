'''
##thats single process has only single thread
# import time

# print("starting time")

# time.sleep(1000)
'''
if False:
    import threading
    import time

    def t1():
        print("thread 1 is running")
        time.sleep(1000)
        print("thread 1 :is finished")


    def t2():
        print("thread 2 is running")
        time.sleep(1000)
        print("thread 2 :is finished")

    t1:threading.Thread=threading.Thread(target=t1)
    t2:threading.Thread=threading.Thread(target=t2)
    t1.start()
    t2.start()

    '''
    With Join
    thread 1 is running
    thread 2 is running
    ... (waits 1000 seconds) ...
    thread 1 :is finished
    thread 2 :is finished
    All threads are finished
    '''


    t1.join()##join mean : the main thread please wait untill t1 is finished
    t2.join()##join mean : the main thread please wait untill t2 is finished


    print("All threads are finished")


    '''
    without join 
    thread 1 is running
    thread 2 is running
    All threads are finished    <-- Prints in less than 1 second! ##all processes are terminated 
    ... (1000 seconds pass in the background) ...
    thread 1 :is finished
    thread 2 :is finished


    '''
if False :
    import time
    import threading


    def tick():
        print(f"Tick ! the time si {time.strftime('%H:%M:%S')}")
        threading.Timer(1,tick).start()

    threading.Timer(1,tick).start()
    # t1:threading.Thread=threading.Timer(1,tick)



