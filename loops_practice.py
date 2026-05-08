import random
import time

class Loops:
    TARGET = 5
    KFC_LOAD = 85
    ITER = 10
    PAUSE = 0.2
    MESSAGE = 'АСССТАНАВИТЕЕЕЕСЬ!!!'

    def task1(self):
        numbers = list(range(1,8))
        for n in numbers:
            if n != Loops.TARGET:
                print(n)
            else:
                print(n)

    def task2(self):
        words = [f"str{i}" for i in range(10)]
        for word in words:
            print(word, sep=', ')

    def task3(self):
        iter = 1
        while iter <= Loops.ITER:
            load = random.randint(0,100)
            if load >= Loops.KFC_LOAD:
                print(Loops.MESSAGE)
            time.sleep(Loops.PAUSE)
            iter+=1




if __name__ == "__main__":
    pass