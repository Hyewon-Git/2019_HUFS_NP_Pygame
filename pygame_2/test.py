import threading

def a():
    time = threading.Timer(1, a)
    print('123')
    time.start()

a()