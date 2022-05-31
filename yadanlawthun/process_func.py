from multiprocessing import Process


def hello():
    print("Hello Process")


p1 = Process(target=hello)
p1.start()
